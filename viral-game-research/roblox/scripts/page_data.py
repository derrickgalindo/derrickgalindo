"""Chart data for the Roblox playbook page -> report/roblox_data.json"""
import json, os, glob
import numpy as np, pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
df = pd.read_csv(os.path.join(ROOT, "data", "roblox_games.csv")); df["created"] = pd.to_datetime(df.created, utc=True, format="mixed")
lm = pd.read_csv(os.path.join(ROOT, "data", "roblox_launches.csv"))
out = {}
def hist(uid):
    r = json.load(open(os.path.join(RAW, "rowatcher", f"{uid}.json")))
    h = pd.DataFrame(r["rw_history"]); h["time"] = pd.to_datetime(h.time, utc=True); h["playing"] = pd.to_numeric(h.playing)
    return h
# launch curves: daily max CCU vs days since creation for top launches
curves = []
for name in lm.sort_values("peak_ccu", ascending=False).name.head(10):
    row = df[df.name == name].iloc[0]; h = hist(row.universe_id)
    d = ((h.time - row.created).dt.total_seconds() / 86400).round()
    s = h.groupby(d).playing.max(); s = s[s.index >= 0]
    curves.append({"name": name, "created": str(row.created.date()), "pts": [[int(k), int(v)] for k, v in s.items()]})
out["curves"] = curves
# concentration
p = np.array(sorted(json.load(open(os.path.join(RAW, "rolimons_snapshot.json")))["rolimons_players"].values(), reverse=True), float)
out["concentration"] = {"n": len(p), "total": int(p.sum()), "shares": {str(k): float(p[:k].sum() / p.sum()) for k in [1, 10, 50, 100, 500, 1000]},
                        "ge": {str(t): int((p >= t).sum()) for t in [1000, 10000, 75000, 100000]}}
# waves: steal/egg family
low = df.name.fillna("").str.lower()
w = df[low.str.contains("steal|egg|brainrot")].copy()
w["peak"] = w[["peak_ccu_since_jun", "playing_now"]].max(axis=1)
out["wave"] = [{"name": r["name"], "created": str(r.created.date()), "peak": int(r.peak) if pd.notna(r.peak) else None, "now": int(r.playing_now or 0) if pd.notna(r.playing_now) else 0} for _, r in w.sort_values("created").iterrows() if pd.notna(r.created)]
# funnel
r1 = lm[lm.days_to_1k.notna()]
out["funnel"] = [{"t": t, "n": int((r1.peak_ccu >= t).sum())} for t in [1000, 10000, 50000, 75000, 100000, 1000000]]
out["launch_stats"] = {"n": int(len(lm)), "days_to_1k_median": float(lm.days_to_1k.median()), "jump_median": float((lm.days_to_10k - lm.days_to_1k).median()),
                       "days_to_peak_median": float(lm.days_to_peak.median())}
# retained after peak (launches peak>=20k, >=14d past peak)
x = lm[lm.peak_ccu >= 20000].copy()
x["past"] = (pd.Timestamp("2026-10-22") - pd.to_datetime(x.created)).dt.days - x.days_to_peak
x = x[x.past >= 14]
out["retained"] = [{"name": r["name"], "peak": int(r.peak_ccu), "ratio": float(r.now_over_peak)} for _, r in x.sort_values("now_over_peak").iterrows()]
# top 20 now
t = df.sort_values("playing_now", ascending=False).head(20)
out["top"] = [{"name": r["name"], "playing": int(r.playing_now), "created": str(r.created.date()), "genre": r.genre, "max_players": int(r.max_players) if pd.notna(r.max_players) else None, "like": float(r.like_ratio)} for _, r in t.iterrows()]
# concept analogs
out["analogs"] = [{"name": r["name"], "created": str(r.created.date()), "peak": int(r.peak_ccu_since_jun), "now": int(r.playing_now), "like": float(r.like_ratio)}
                  for _, r in df[df.name.str.contains("Paint Or Seek|Hide In Pixels|Paint to Get Rich|Draw Me!", regex=True, na=False)].iterrows()]
os.makedirs(os.path.join(ROOT, "report"), exist_ok=True)
json.dump(out, open(os.path.join(ROOT, "report", "roblox_data.json"), "w"))
print({k: len(v) if hasattr(v, "__len__") else v for k, v in out.items()})
print([ (c["name"], len(c["pts"])) for c in curves])
