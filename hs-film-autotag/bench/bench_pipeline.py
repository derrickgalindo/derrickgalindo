"""Measure CPU cost of a minimal HS-film auto-tagging pipeline.

Stages timed (all on CPU, onnxruntime + OpenCV + ffmpeg):
  1. Full-resolution H.264 decode (ffmpeg -benchmark), 1 thread and all threads.
  2. Play segmentation signal: 5 fps, 320x180 grayscale, global-motion-compensated
     frame differencing -> candidate snap times.
  3. Field-line detection on full-res snap frames (white mask + Canny + HoughLinesP).
  4. Player detection on snap frames with several open-source detectors.

Outputs a JSON of measurements plus annotated frames for a visual sanity check.

Usage:
  python -I bench_pipeline.py VIDEO MODELS_DIR OUT_DIR [--max-snaps N]
"""

import argparse
import json
import os
import re
import subprocess
import time

import cv2
import numpy as np
import onnxruntime as ort


def ffmpeg_decode_benchmark(video, threads):
    cmd = ["ffmpeg", "-nostdin", "-hide_banner", "-benchmark", "-threads", str(threads),
           "-i", video, "-an", "-f", "null", "-"]
    out = subprocess.run(cmd, capture_output=True, text=True).stderr
    m = re.search(r"bench: utime=([\d.]+)s stime=([\d.]+)s rtime=([\d.]+)s", out)
    frames = re.findall(r"frame=\s*(\d+)", out)
    return {
        "threads": threads,
        "user_s": float(m.group(1)), "sys_s": float(m.group(2)), "wall_s": float(m.group(3)),
        "frames": int(frames[-1]) if frames else None,
    }


def probe(video):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,r_frame_rate:format=duration", "-of", "json", video],
                         capture_output=True, text=True).stdout
    d = json.loads(out)
    s = d["streams"][0]
    num, den = s["r_frame_rate"].split("/")
    return {"width": s["width"], "height": s["height"], "fps": float(num) / float(den),
            "duration_s": float(d["format"]["duration"])}


def lowres_stream(video, fps=5, w=320, h=180):
    """Yield (t, gray uint8 frame) at reduced rate; decode cost is measured separately."""
    cmd = ["ffmpeg", "-nostdin", "-loglevel", "error", "-i", video, "-vf",
           f"fps={fps},scale={w}:{h},format=gray", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    n = 0
    while True:
        buf = p.stdout.read(w * h)
        if len(buf) < w * h:
            break
        yield n / fps, np.frombuffer(buf, np.uint8).reshape(h, w)
        n += 1
    p.wait()


def motion_signal(video, fps=5):
    """Residual motion after removing global camera translation (phase correlation)."""
    t_proc = 0.0
    times, motion = [], []
    prev = None
    win = None
    t_wall0 = time.perf_counter()
    for t, g in lowres_stream(video, fps):
        t0 = time.perf_counter()
        f = g.astype(np.float32)
        if prev is not None:
            if win is None:
                win = cv2.createHanningWindow(f.shape[::-1], cv2.CV_32F)
            # phaseCorrelate applies the window in place, so hand it copies.
            (dx, dy), _ = cv2.phaseCorrelate(prev.copy(), f.copy(), win)
            M = np.float32([[1, 0, dx], [0, 1, dy]])
            aligned = cv2.warpAffine(prev, M, f.shape[::-1], borderMode=cv2.BORDER_REPLICATE)
            r = np.abs(f - aligned)[10:-10, 10:-10]
            motion.append(float(np.mean(r > 18)))
            times.append(t)
        prev = f
        t_proc += time.perf_counter() - t0
    wall = time.perf_counter() - t_wall0
    return np.array(times), np.array(motion), {"proc_s": t_proc, "wall_incl_decode_s": wall,
                                               "frames": len(motion) + 1, "fps": fps}


def find_snaps(times, motion, fps=5, still_s=1.2, rise=2.5):
    """Snap candidate = end of a >=still_s quiet window followed by a sharp motion rise."""
    k = max(1, int(round(0.6 * fps)))
    sm = np.convolve(motion, np.ones(k) / k, mode="same")
    quiet_thr = np.percentile(sm, 35)
    snaps = []
    n_still = int(still_s * fps)
    i = n_still
    while i < len(sm) - fps:
        pre = sm[i - n_still:i]
        post = sm[i:i + fps]
        if pre.max() <= quiet_thr * 1.3 and post.mean() > rise * max(pre.mean(), 1e-4):
            snaps.append(float(times[i]))
            i += 8 * fps  # refractory: plays are >= ~8 s apart
        else:
            i += 1
    return snaps, float(quiet_thr)


def grab_frame(video, t):
    cmd = ["ffmpeg", "-nostdin", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", video,
           "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"]
    buf = subprocess.run(cmd, capture_output=True).stdout
    return cv2.imdecode(np.frombuffer(buf, np.uint8), cv2.IMREAD_COLOR)


def field_lines(img):
    """White painted-line candidates on grass; returns segments and dominant yard-line angle."""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    grass = cv2.inRange(hsv, (30, 40, 30), (90, 255, 255))
    grass = cv2.morphologyEx(grass, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    white = cv2.inRange(hsv, (0, 0, 170), (180, 60, 255))
    white = cv2.bitwise_and(white, grass)
    edges = cv2.Canny(white, 50, 150)
    segs = cv2.HoughLinesP(edges, 1, np.pi / 360, threshold=80,
                           minLineLength=img.shape[0] // 8, maxLineGap=12)
    segs = [] if segs is None else segs.reshape(-1, 4)
    angles = [np.degrees(np.arctan2(y2 - y1, x2 - x1)) % 180 for x1, y1, x2, y2 in segs]
    hist, edges_a = np.histogram(angles, bins=36, range=(0, 180)) if angles else (np.zeros(36), None)
    dom = float(edges_a[np.argmax(hist)] + 2.5) if angles else None
    return segs, dom


class Yolo:
    def __init__(self, path, threads):
        so = ort.SessionOptions()
        so.intra_op_num_threads = threads
        so.inter_op_num_threads = 1
        self.s = ort.InferenceSession(path, so, providers=["CPUExecutionProvider"])
        self.inp = self.s.get_inputs()[0].name
        self.size = 640

    def prep(self, img):
        h, w = img.shape[:2]
        r = self.size / max(h, w)
        nh, nw = int(round(h * r)), int(round(w * r))
        canvas = np.full((self.size, self.size, 3), 114, np.uint8)
        canvas[:nh, :nw] = cv2.resize(img, (nw, nh))
        x = canvas[:, :, ::-1].transpose(2, 0, 1)[None].astype(np.float32) / 255.0
        return x, r

    def __call__(self, img, conf=0.25):
        x, r = self.prep(img)
        out = self.s.run(None, {self.inp: x})[0][0]  # (84, 8400)
        scores = out[4:, :]
        cls = scores.argmax(0)
        sc = scores.max(0)
        keep = (cls == 0) & (sc > conf)
        b = out[:4, keep].T
        if out[:4].max() <= 2.0:  # this export emits normalized xywh; convert to input pixels
            b = b * self.size
        sc = sc[keep]
        boxes = np.stack([b[:, 0] - b[:, 2] / 2, b[:, 1] - b[:, 3] / 2, b[:, 2], b[:, 3]], 1) / r
        idx = cv2.dnn.NMSBoxes(boxes.tolist(), sc.tolist(), conf, 0.5)
        idx = np.array(idx).reshape(-1)
        return boxes[idx] if len(idx) else np.zeros((0, 4)), sc[idx] if len(idx) else np.zeros(0)


class RFDetr:
    MEAN = np.array([0.485, 0.456, 0.406], np.float32)
    STD = np.array([0.229, 0.224, 0.225], np.float32)

    def __init__(self, path, size, threads):
        so = ort.SessionOptions()
        so.intra_op_num_threads = threads
        so.inter_op_num_threads = 1
        self.s = ort.InferenceSession(path, so, providers=["CPUExecutionProvider"])
        self.size = size

    def __call__(self, img, conf=0.3):
        h, w = img.shape[:2]
        x = cv2.resize(img, (self.size, self.size))[:, :, ::-1].astype(np.float32) / 255.0
        x = ((x - self.MEAN) / self.STD).transpose(2, 0, 1)[None]
        boxes, logits = self.s.run(None, {"pixel_values": x})
        p = 1 / (1 + np.exp(-logits[0]))
        person = p[:, 1]  # COCO id 1 == person in this export
        keep = person > conf
        cx, cy, bw, bh = boxes[0][keep].T
        out = np.stack([(cx - bw / 2) * w, (cy - bh / 2) * h, bw * w, bh * h], 1)
        return out, person[keep]


def tiled(det, img, tiles=2, overlap=0.15):
    """Split a wide frame into horizontal tiles so small players get more pixels."""
    h, w = img.shape[:2]
    tw = int(w / (tiles - (tiles - 1) * overlap))
    step = int(tw * (1 - overlap))
    boxes, scores = [], []
    for i in range(tiles):
        x0 = min(i * step, w - tw)
        b, s = det(img[:, x0:x0 + tw])
        if len(b):
            b = b.copy()
            b[:, 0] += x0
            boxes.append(b)
            scores.append(s)
    if not boxes:
        return np.zeros((0, 4)), np.zeros(0)
    b = np.concatenate(boxes)
    s = np.concatenate(scores)
    idx = np.array(cv2.dnn.NMSBoxes(b.tolist(), s.tolist(), 0.0, 0.5)).reshape(-1)
    return b[idx], s[idx]


def time_fn(fn, frames, warmup=2):
    for f in frames[:warmup]:
        fn(f)
    ts, counts = [], []
    for f in frames:
        t0 = time.perf_counter()
        b, _ = fn(f)
        ts.append(time.perf_counter() - t0)
        counts.append(int(len(b)))
    return {"ms_mean": 1000 * float(np.mean(ts)), "ms_p50": 1000 * float(np.median(ts)),
            "persons_mean": float(np.mean(counts)), "persons_per_frame": counts}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("models")
    ap.add_argument("out")
    ap.add_argument("--max-snaps", type=int, default=24)
    ap.add_argument("--snap-times", default="",
                    help="comma-separated hand-labelled pre-snap times (s); overrides the heuristic")
    ap.add_argument("--extra-frames", type=int, default=0,
                    help="also time detectors on N evenly spaced frames")
    ap.add_argument("--skip-decode", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    res = {"video": os.path.basename(a.video), "probe": probe(a.video),
           "cpu": open("/proc/cpuinfo").read().split("model name")[1].split("\n")[0].strip(": "),
           "vcpus": os.cpu_count()}

    if not a.skip_decode:
        res["decode_full_1thread"] = ffmpeg_decode_benchmark(a.video, 1)
        res["decode_full_allthreads"] = ffmpeg_decode_benchmark(a.video, 0)

    times, motion, seg = motion_signal(a.video)
    snaps, thr = find_snaps(times, motion)
    res["segmentation"] = seg | {"snap_candidates": snaps, "quiet_thr": thr}
    np.save(os.path.join(a.out, "motion.npy"), np.stack([times, motion]))

    # Frames just before each snap (players set) for per-play stages.
    if a.snap_times:
        picks = [float(x) for x in a.snap_times.split(",")]
        frames = [grab_frame(a.video, t) for t in picks]
    else:
        picks = snaps[: a.max_snaps]
        frames = [grab_frame(a.video, max(0.0, t - 0.4)) for t in picks]
    if a.extra_frames:
        dur = res["probe"]["duration_s"]
        frames += [grab_frame(a.video, dur * (i + 0.5) / a.extra_frames) for i in range(a.extra_frames)]
    frames = [f for f in frames if f is not None]
    res["n_snap_frames"] = len(frames)

    lt = []
    for f in frames:
        t0 = time.perf_counter()
        segs, dom = field_lines(f)
        lt.append(time.perf_counter() - t0)
    res["field_lines_ms_mean"] = 1000 * float(np.mean(lt))

    m = a.models
    dets = {}
    for threads in (1, os.cpu_count()):
        for name, mk in [
            ("yolo11n_640", lambda: Yolo(f"{m}/yolo11n-det-fp32.onnx", threads)),
            ("yolo11s_640", lambda: Yolo(f"{m}/yolo11s-det-fp32.onnx", threads)),
            ("yolo11m_640", lambda: Yolo(f"{m}/yolo11m-det-fp32.onnx", threads)),
            ("rfdetr_nano_384", lambda: RFDetr(f"{m}/rfdetr_nano-ONNX/model.onnx", 384, threads)),
            ("rfdetr_medium_576", lambda: RFDetr(f"{m}/rfdetr_medium-ONNX/model.onnx", 576, threads)),
        ]:
            det = mk()
            dets[f"{name}_t{threads}"] = time_fn(det, frames)
            if name in ("yolo11s_640", "rfdetr_medium_576"):
                dets[f"{name}_tiled3_t{threads}"] = time_fn(lambda im: tiled(det, im, 3), frames)
            if threads == os.cpu_count() and name in ("yolo11s_640", "rfdetr_medium_576"):
                for i, f in enumerate(frames[:4]):
                    b, _ = tiled(det, f, 3)
                    vis = f.copy()
                    for x, y, w, h in b.astype(int):
                        cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    cv2.imwrite(os.path.join(a.out, f"snap{i}_{name}_tiled3.jpg"), vis)
    res["detectors"] = dets
    for i, f in enumerate(frames):
        cv2.imwrite(os.path.join(a.out, f"snapframe{i:02d}.jpg"), cv2.resize(f, (640, 360)))
    with open(os.path.join(a.out, "results.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "detectors"}, indent=1)[:3000])
    for k, v in dets.items():
        print(f"{k:32s} {v['ms_mean']:8.1f} ms  persons={v['persons_mean']:.1f}")


if __name__ == "__main__":
    main()
