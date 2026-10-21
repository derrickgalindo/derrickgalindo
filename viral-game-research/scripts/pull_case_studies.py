"""Daily-resolution Google Trends pulls for the causal case studies (windows < 270 days give daily data).

- Wordle: worldwide, NZ, US, GB, Oct 15 2021 - Feb 15 2022 (share button 2021-12-16; NYT profile 2022-01-03)
- Flappy Bird: worldwide, US, VN, Oct 1 2013 - Feb 28 2014 (US #1 2014-01-17; PewDiePie 2014-01-27)
- Among Us: worldwide, KR, BR, US, May 1 - Oct 31 2020 (Sodapoppin stream 2020-07-15)
- Grow a Garden: worldwide, Mar 15 - Jul 31 2025
- Suika Game: worldwide, JP, Jul 1 - Dec 31 2023
"""
import os, random, time
from pytrends.request import TrendReq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "raw", "trends", "daily")
os.makedirs(OUT, exist_ok=True)
py = TrendReq(hl="en-US", tz=0, timeout=(10, 30))
WORDLE, FLAPPY, AMONG = "/g/11smcj06ct", "flappy bird", "among us"
JOBS = [
    ("wordle", WORDLE, "2021-10-15 2022-02-15", ["", "NZ", "US", "GB", "AU", "CA"]),
    ("wordle_term", "wordle", "2021-10-15 2022-02-15", ["", "NZ", "US"]),
    ("flappybird", FLAPPY, "2013-10-01 2014-02-28", ["", "US", "VN", "GB"]),
    ("amongus", AMONG, "2020-05-01 2020-10-31", ["", "KR", "BR", "US", "MX"]),
    ("growagarden", "grow a garden", "2025-03-15 2025-07-31", ["", "US", "PH"]),
    ("suika", "suika game", "2023-07-01 2023-12-31", ["", "JP", "US"]),
    ("infinitecraft", "infinite craft", "2024-01-15 2024-05-15", [""]),
    ("drawsomething", "draw something", "2012-01-15 2012-07-15", ["", "US"]),
    ("2048", "2048 game", "2014-02-15 2014-07-15", ["", "US"]),
    # pre-spike windows: normalised to the end of the window so early growth is not floored to zero
    ("wordle_pre", "wordle", "2021-10-15 2022-01-02", ["", "NZ", "US", "GB", "AU"]),
    ("wordle_preNYT2", "wordle", "2021-11-15 2021-12-31", ["", "NZ"]),
    ("flappy_pre", FLAPPY, "2013-09-01 2014-01-16", ["", "US", "VN", "GB"]),
    ("flappy_pre2", FLAPPY, "2013-09-01 2013-12-31", ["", "US"]),
    ("amongus_pre", AMONG, "2020-04-01 2020-07-31", ["", "KR", "BR", "US"]),
    ("growagarden_pre", "grow a garden", "2025-03-20 2025-05-10", [""]),
]
for name, term, tf, geos in JOBS:
    for geo in geos:
        path = os.path.join(OUT, f"{name}.{geo or 'WW'}.csv")
        if os.path.exists(path):
            continue
        for a in range(8):
            try:
                py.build_payload([term], timeframe=tf, geo=geo)
                df = py.interest_over_time()
                break
            except Exception as e:
                print("retry", a, str(e)[:60], flush=True)
                time.sleep(25 * (a + 1))
        df = df.drop(columns=["isPartial"], errors="ignore")
        if df.empty:  # below Google's reporting threshold for the whole window
            open(path, "w").write("date,value\n"); print(name, geo, "empty", flush=True); continue
        df.columns = ["value"]
        df.to_csv(path)
        print(name, geo, len(df), flush=True)
        time.sleep(8 + random.random() * 5)
