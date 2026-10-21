"""Base rate for Wordle-likes: every English-language domain-specific, twist and non-linguistic
variant listed in the 'Wordles of the World' census (rwmpelstilzchen.gitlab.io/wordles), queried
in Google Trends in batches of 4 alongside the anchor 'nerdle' over 2022-01-01..2024-12-31.
Peak interest is then converted to Wordle units using anchor ratios [nerdle vs wordle]."""
import json, os, random, time
import pandas as pd
from pytrends.request import TrendReq
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
games = json.load(open(os.path.join(ROOT, "data/raw/wordles_of_the_world_parsed.json")))
names = []
for g in games:
    if g["section"] in ("domain", "twist", "nonling") and g["lang"] in ("English", None):
        n = g["name"].strip()
        if n.lower() not in [x.lower() for x in names] and len(n) < 40:
            names.append(n)
OUT = os.path.join(ROOT, "data/raw/wordle_census_trends.csv")
done = set(pd.read_csv(OUT)["name"]) if os.path.exists(OUT) else set()
py = TrendReq(hl="en-US", tz=0, timeout=(10, 30))
TF = "2022-01-01 2024-12-31"
def fetch(terms):
    for a in range(8):
        try:
            py.build_payload(terms, timeframe=TF, geo="")
            df = py.interest_over_time(); time.sleep(8 + random.random() * 5); return df
        except Exception as e:
            print("retry", a, str(e)[:60], flush=True); time.sleep(25 * (a + 1))
rows = []
# anchor ladder: nerdle vs wordle
anc = fetch(["wordle", "nerdle"])
pd.DataFrame({"name": ["__anchor__"], "peak": [anc["nerdle"].max() / anc["wordle"].max()], "mean": [anc["nerdle"].mean()]}).to_csv(OUT + ".anchor.csv", index=False)
todo = [n for n in names if n not in done]
for i in range(0, len(todo), 4):
    batch = todo[i:i + 4]
    df = fetch(["nerdle"] + batch)
    if df is None or df.empty:
        res = [{"name": n, "peak_vs_nerdle": 0.0, "weeks_nonzero": 0} for n in batch]
    else:
        res = [{"name": n, "peak_vs_nerdle": df[n].max() / max(df["nerdle"].max(), 1), "weeks_nonzero": int((df[n] > 0).sum())} for n in batch]
    pd.DataFrame(res).to_csv(OUT, mode="a", header=not os.path.exists(OUT), index=False)
    print(i, batch, flush=True)
