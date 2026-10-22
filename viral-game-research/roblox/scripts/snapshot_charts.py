"""Snapshot Roblox's discovery charts (explore-api sorts) and Rolimons' tracked-games player counts.
One gzipped JSON per run in data/charts/. Run on a timer to watch games climb the charts."""
import datetime, gzip, json, os, uuid
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "charts")
UA = {"User-Agent": "viral-game-research (derrickgalindo7@gmail.com)"}


def main():
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H%MZ")
    snap = {"taken_at": ts}
    for device in ("computer", "phone"):
        r = requests.get("https://apis.roblox.com/explore-api/v1/get-sorts", headers=UA, timeout=60,
                         params={"sessionId": str(uuid.uuid4()), "device": device, "country": "all"})
        snap[f"sorts_{device}"] = r.json() if r.ok else {"error": r.status_code}
    r = requests.get("https://api.rolimons.com/games/v1/gamelist", headers=UA, timeout=60)
    snap["rolimons_gamelist"] = r.json() if r.ok else {"error": r.status_code}
    with gzip.open(os.path.join(OUT, f"charts_{ts}.json.gz"), "wt") as f:
        json.dump(snap, f)
    print(ts, "saved", flush=True)


if __name__ == "__main__":
    main()
