"""Compare the two most recent chart snapshots and list what changed this week:
new entries on Roblox's charts, games launched in the last 60 days with real traction, and the biggest risers.
Writes analysis/weekly/<date>.md and prints it."""
import glob, gzip, json, os
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
snaps = sorted(glob.glob(os.path.join(ROOT, "data", "charts", "charts_*.json.gz")))
cur = json.load(gzip.open(snaps[-1], "rt"))
prev = json.load(gzip.open(snaps[-2], "rt")) if len(snaps) > 1 else None


def chart(snap, sort_id):
    for s in snap["sorts_computer"].get("sorts", []):
        if s.get("sortId") == sort_id:
            return {str(g["universeId"]): (g["name"], g.get("playerCount") or 0) for g in s.get("games") or []}
    return {}


date = cur["taken_at"][:10]
L = [f"# Weekly Roblox chart check: {date}", "", f"Compared with: {prev['taken_at'][:10] if prev else 'no earlier snapshot'}", ""]
for sid, title in [("top-playing-now", "Top Playing Now"), ("up-and-coming", "Up-and-Coming"), ("top-trending", "Top Trending")]:
    now = chart(cur, sid); before = chart(prev, sid) if prev else {}
    new = [(n, p) for u, (n, p) in now.items() if u not in before]
    L += [f"## {title}: {len(new)} new entries this week", ""] + [f"- {n}: {p:,} playing" for n, p in sorted(new, key=lambda x: -x[1])[:15]] + [""]
games_csv = os.path.join(ROOT, "data", "roblox_games.csv")
if os.path.exists(games_csv):
    df = pd.read_csv(games_csv); df["created"] = pd.to_datetime(df.created, utc=True, format="mixed")
    fresh = df[(df.created >= pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=60)) & (df.playing_now >= 10000)].sort_values("playing_now", ascending=False)
    L += ["## Launched in the last 60 days and above 10k players now", ""] + [f"- {r['name']} (launched {r.created.date()}): {int(r.playing_now):,} playing" for _, r in fresh.head(20).iterrows()] + [""]
os.makedirs(os.path.join(ROOT, "analysis", "weekly"), exist_ok=True)
open(os.path.join(ROOT, "analysis", "weekly", f"{date}.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
