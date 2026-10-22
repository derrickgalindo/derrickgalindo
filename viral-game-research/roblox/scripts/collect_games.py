"""Collect a dataset of ~600 Roblox experiences.

Universe set = every game on Roblox's discovery charts in the latest snapshot (computer + phone)
             + the top N games by live players in Rolimons' tracked list (place IDs mapped to universes).
Per game:
  Roblox (official): metadata (created/updated, visits, playing, maxPlayers, genre), votes, favorites, game passes.
  RoWatcher (third-party, robots.txt allows, welcomes AI assistants): game record incl. its revenue *model estimate*,
  player-count history since tracking began (2026-06-30), and the change log (title/thumbnail edits).
Resumable: per-game files are skipped if present. Polite pacing (~1 request/second to RoWatcher).
"""
import glob, gzip, json, os, sys, time
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
RW = os.path.join(RAW, "rowatcher")
os.makedirs(RW, exist_ok=True)
UA = {"User-Agent": "viral-game-research (derrickgalindo7@gmail.com)"}
S = requests.Session(); S.headers.update(UA)
TOP_N = int(sys.argv[1]) if len(sys.argv) > 1 else 500


def get(url, params=None, tries=5):
    for a in range(tries):
        try:
            r = S.get(url, params=params, timeout=60)
            if r.status_code == 429:
                time.sleep(15 * (a + 1)); continue
            if r.ok:
                return r.json()
            if r.status_code == 404:
                return None
        except Exception:
            pass
        time.sleep(3 * (a + 1))
    return None


def universe_set():
    snap = sorted(glob.glob(os.path.join(ROOT, "data", "charts", "charts_*.json.gz")))[-1]
    d = json.load(gzip.open(snap, "rt"))
    ids, chart_hits = set(), {}
    for dev in ("computer", "phone"):
        for s in d[f"sorts_{dev}"].get("sorts", []):
            for rank, g in enumerate(s.get("games") or []):
                ids.add(g["universeId"])
                chart_hits.setdefault(str(g["universeId"]), []).append({"device": dev, "sort": s.get("sortId"), "rank": rank + 1, "playing": g.get("playerCount")})
    games = d["rolimons_gamelist"]["games"]
    top = sorted(games.items(), key=lambda kv: -kv[1][1])[:TOP_N]
    mp_path = os.path.join(RAW, "place_to_universe.json")
    mp = json.load(open(mp_path)) if os.path.exists(mp_path) else {}
    for pid, _ in top:
        if pid not in mp:
            u = get(f"https://apis.roblox.com/universes/v1/places/{pid}/universe")
            mp[pid] = u.get("universeId") if u else None
            time.sleep(0.3)
    json.dump(mp, open(mp_path, "w"))
    for pid, _ in top:
        if mp.get(pid):
            ids.add(mp[pid])
    json.dump(chart_hits, open(os.path.join(RAW, "chart_positions.json"), "w"))
    json.dump({"snapshot": os.path.basename(snap), "rolimons_tracked": len(games),
               "rolimons_players": {pid: v[1] for pid, v in games.items()}}, open(os.path.join(RAW, "rolimons_snapshot.json"), "w"))
    return sorted(ids)


def roblox_batch(ids):
    meta, votes = {}, {}
    for i in range(0, len(ids), 50):
        chunk = ",".join(map(str, ids[i:i + 50]))
        m = get("https://games.roblox.com/v1/games", {"universeIds": chunk}) or {}
        for g in m.get("data", []):
            meta[str(g["id"])] = g
        v = get("https://games.roblox.com/v1/games/votes", {"universeIds": chunk}) or {}
        for g in v.get("data", []):
            votes[str(g["id"])] = g
        time.sleep(0.5)
    json.dump(meta, open(os.path.join(RAW, "roblox_meta.json"), "w"))
    json.dump(votes, open(os.path.join(RAW, "roblox_votes.json"), "w"))


def per_game(uid):
    path = os.path.join(RW, f"{uid}.json")
    if os.path.exists(path):
        return
    rec = {"universeId": uid}
    rec["favorites"] = (get(f"https://games.roblox.com/v1/games/{uid}/favorites/count") or {}).get("favoritesCount")
    gp = get(f"https://apis.roblox.com/game-passes/v1/universes/{uid}/game-passes", {"passView": "Full", "pageSize": 100}) or {}
    rec["gamepasses"] = [{"name": p.get("name"), "price": p.get("price"), "forSale": p.get("isForSale"), "created": p.get("created")} for p in gp.get("gamePasses", [])]
    base = "https://rowatcher.com/api/games"
    g = get(f"{base}/{uid}"); time.sleep(1)
    rec["rw_game"] = (g or {}).get("data", {}).get("game") if g else None
    h = get(f"{base}/{uid}/history", {"from": "2026-06-01T00:00:00Z"}); time.sleep(1)
    rec["rw_history"] = (h or {}).get("data") if h else None
    c = get(f"{base}/{uid}/changes"); time.sleep(1)
    rec["rw_changes"] = c if isinstance(c, list) else (c or {}).get("data") if c else None
    json.dump(rec, open(path, "w"))


if __name__ == "__main__":
    ids = universe_set()
    print("universes:", len(ids), flush=True)
    roblox_batch(ids)
    for n, uid in enumerate(ids):
        per_game(uid)
        if n % 25 == 0:
            print(n, uid, flush=True)
    print("done", flush=True)
