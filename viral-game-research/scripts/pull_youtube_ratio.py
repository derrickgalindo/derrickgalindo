"""Pre-registered N2b watch_ratio: YouTube-search vs web-search interest, both anchored on 'sudoku'.
Pulls [term, 'sudoku'] with gprop='youtube' over the same window as the web scale payload."""
import json, os, random, time
import pandas as pd
from pytrends.request import TrendReq
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(ROOT, "data", "raw", "trends")
OUT = os.path.join(TR, "youtube"); os.makedirs(OUT, exist_ok=True)
meta = json.load(open(os.path.join(TR, "_meta.json")))
py = TrendReq(hl="en-US", tz=0, timeout=(10, 30))
for gid, m in meta.items():
    path = os.path.join(OUT, f"{gid}.yt.csv")
    if os.path.exists(path) or m["start"] < "2008-01-01":
        continue
    for a in range(8):
        try:
            py.build_payload([m["term"], "sudoku"], timeframe=f"{m['start']} {m['end']}", geo="", gprop="youtube")
            df = py.interest_over_time(); break
        except Exception as e:
            print("retry", a, str(e)[:60], flush=True); time.sleep(25 * (a + 1))
    if df is None or df.empty:
        open(path, "w").write("date\n"); continue
    df = df.drop(columns=["isPartial"], errors="ignore")
    df.columns = ["game" if c == m["term"] else c for c in df.columns]
    df.to_csv(path); print(gid, flush=True)
    time.sleep(7 + random.random() * 5)
