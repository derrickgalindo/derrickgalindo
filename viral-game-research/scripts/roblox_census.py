"""Census-style base rate for Roblox: uniformly sample universe IDs created in a date band
and record lifetime visits. Every Roblox account gets a default empty place, so we flag
'default' places by name pattern and report base rates both over all universes and over
'real attempts' (renamed and updated after creation)."""
import csv, os, random, re, sys, time
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "raw", "roblox_census.csv")
LO, HI = int(sys.argv[1]) if len(sys.argv) > 1 else 5_400_000_000, int(sys.argv[2]) if len(sys.argv) > 2 else 7_600_000_000
N_BATCHES = int(sys.argv[3]) if len(sys.argv) > 3 else 1200
DEFAULT = re.compile(r"('s Place|^Local de |^Lugar de |^Emplacement de |^Ort von |^Luogo di |^Miejsce |^Место |の場所|^Tempat |Place Number|^\[TITLE UNAVAILABLE\])", re.I)

random.seed(20261021)
new = not os.path.exists(OUT)
f = open(OUT, "a", newline="")
w = csv.writer(f)
if new:
    w.writerow(["universe_id", "name", "visits", "playing", "favorites", "created", "updated", "is_default", "genre"])
s = requests.Session()
for b in range(N_BATCHES):
    ids = [random.randint(LO, HI) for _ in range(50)]
    for attempt in range(5):
        try:
            r = s.get("https://games.roblox.com/v1/games", params={"universeIds": ",".join(map(str, ids))}, timeout=30)
            if r.status_code == 429:
                time.sleep(10 * (attempt + 1)); continue
            r.raise_for_status()
            break
        except Exception as e:
            time.sleep(5 * (attempt + 1))
    else:
        continue
    for g in r.json().get("data", []):
        if not g.get("id"):
            continue
        w.writerow([g["id"], g["name"][:80], g["visits"], g["playing"], g.get("favoritedCount"), g["created"][:10], g["updated"][:10],
                    int(bool(DEFAULT.search(g["name"]))), g.get("genre")])
    if b % 50 == 0:
        f.flush(); print(b, flush=True)
    time.sleep(0.4)
f.close()
