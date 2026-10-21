"""Turn raw Google Trends CSVs into per-game curve metrics.

Conventions (Google Trends returns integers 0-100 normalised to the max within each payload):
  * solo series: shape of a game's own attention curve.
  * scale series: [game, sudoku]; peak_sudoku_units = max(game) / mean(sudoku) in the same payload.
    If max(game) <= 5 there, rung 2 [game, nonogram] is used and converted with the sudoku/nonogram
    ratio for the overlapping period from _anchor_ladder.csv.
"""
import glob, json, os
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(ROOT, "data", "raw", "trends")


def _read(path):
    if not os.path.exists(path):
        return None
    df = pd.read_csv(path, parse_dates=["date"])
    return None if df.empty else df.set_index("date")


def ladder_ratio(start, end):
    """mean(sudoku)/mean(nonogram) for the window overlapping [start, end]."""
    lad = _read(os.path.join(TR, "_anchor_ladder.csv"))
    if lad is None:
        return np.nan
    best = None
    for w, g in lad.groupby("window"):
        ov = g.loc[(g.index >= start) & (g.index <= end)]
        if len(ov) > 10 and (best is None or len(ov) > len(best)):
            best = ov
    if best is None:
        best = lad
    return best["sudoku"].mean() / max(best["nonogram"].mean(), 0.5)


def scale_units(gid):
    sc = _read(os.path.join(TR, f"{gid}.scale.csv"))
    if sc is None:
        return np.nan, "missing"
    peak = sc["game"].max()
    if peak > 5:
        return peak / max(sc["sudoku"].mean(), 0.5), "rung1_sudoku"
    s2 = _read(os.path.join(TR, f"{gid}.scale2.csv"))
    if s2 is None:
        return peak / max(sc["sudoku"].mean(), 0.5), "rung1_low_resolution"
    nono_mean = max(s2["nonogram"].mean(), 0.5)
    r = ladder_ratio(s2.index.min(), s2.index.max())
    if s2["game"].max() == 0:
        return 0.5 / nono_mean / r, "below_detection_upper_bound"
    return s2["game"].max() / nono_mean / r, "rung2_nonogram"


def curve_metrics(s: pd.Series):
    """s: weekly solo series 0-100."""
    s = s.astype(float)
    out = {}
    if s.max() <= 0:
        return {k: np.nan for k in ["peak_date", "weeks_to_peak", "early_momentum", "growth_rate_wk", "doubling_days", "half_life_weeks", "retained_share_52w", "rise_type"]}
    ip = int(np.argmax(s.values))
    out["peak_date"] = s.index[ip].date().isoformat()
    nz = np.where(s.values >= 1)[0]
    first = int(nz[0])
    out["weeks_to_peak"] = ip - first
    out["early_momentum"] = np.nan  # filled by early_momentum_abs() once the absolute scale is known
    # rise phase: weeks before the peak with 10..90% of peak, contiguous run ending at peak
    rise = []
    for i in range(ip, -1, -1):
        v = s.values[i]
        if v < 10:
            break
        rise.append(i)
    rise = sorted(rise)
    pts = [i for i in rise if s.values[i] <= 95] + [ip]
    pts = sorted(set(pts))
    if len(pts) >= 3:
        y = np.log(s.values[pts])
        r = np.polyfit(np.array(pts, float), y, 1)[0]
        out["growth_rate_wk"] = float(r)
        out["doubling_days"] = float(7 * np.log(2) / r) if r > 0 else np.nan
        out["rise_type"] = "gradual"
    else:
        out["growth_rate_wk"] = np.nan
        out["doubling_days"] = np.nan
        out["rise_type"] = "step"  # went from <10% to peak in <=2 weeks: launch spike / feature / IP / press
    roll = pd.Series(s.values[ip:]).rolling(4, min_periods=1).mean().values
    below = np.where(roll <= 50)[0]
    out["half_life_weeks"] = float(below[0]) if len(below) else np.nan
    if ip + 54 < len(s):
        out["retained_share_52w"] = float(s.values[ip + 50:ip + 55].mean() / 100)
    else:
        out["retained_share_52w"] = np.nan
    return out


ABS_THRESHOLD = 0.02  # sudoku-units; pre-registered (model/PREREGISTRATION.md)


def early_momentum_abs(s: pd.Series, peak_units: float):
    """log ratio of mean absolute interest in weeks 5-8 vs 1-4 after the series first crosses a FIXED
    absolute threshold. Independent of the eventual peak except through the unit conversion."""
    if s.max() <= 0 or not np.isfinite(peak_units) or peak_units <= 0:
        return np.nan
    a = s.values.astype(float) / 100.0 * peak_units
    idx = np.where(a >= ABS_THRESHOLD)[0]
    if len(idx) == 0 or idx[0] + 8 > len(a):
        return np.nan
    f = idx[0]
    eps = ABS_THRESHOLD / 10
    return float(np.log((a[f + 4:f + 8].mean() + eps) / (a[f:f + 4].mean() + eps)))


def all_metrics():
    meta = json.load(open(os.path.join(TR, "_meta.json")))
    rows = []
    for gid, m in meta.items():
        solo = _read(os.path.join(TR, f"{gid}.solo.csv"))
        if solo is None:
            continue
        cm = curve_metrics(solo["game"])
        su, method = scale_units(gid)
        cm["early_momentum"] = early_momentum_abs(solo["game"], su)
        rows.append({"game_id": gid, "term": m["term"], "topic": m.get("topic"), "peak_sudoku_units": su, "scale_method": method, **cm})
    return pd.DataFrame(rows)


def series_rows():
    meta = json.load(open(os.path.join(TR, "_meta.json")))
    for gid in meta:
        for kind in ("solo", "scale", "scale2"):
            df = _read(os.path.join(TR, f"{gid}.{kind}.csv"))
            if df is None:
                continue
            for col in df.columns:
                if col in ("isPartial",):
                    continue
                for d, v in df[col].items():
                    yield (gid, kind, d.date().isoformat(), col, float(v))
    for f in glob.glob(os.path.join(TR, "daily", "*.csv")):
        name = os.path.basename(f)[:-4]
        df = _read(f)
        if df is None:
            continue
        for d, v in df["value"].items():
            yield (name.split(".")[0], "daily_" + name.split(".")[1], d.date().isoformat(), "value", float(v))


if __name__ == "__main__":
    pd.set_option("display.width", 220)
    print(all_metrics().sort_values("peak_sudoku_units", ascending=False).to_string())
