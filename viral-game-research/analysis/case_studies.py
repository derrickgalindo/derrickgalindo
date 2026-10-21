"""Causal case studies from daily Google Trends:
  1. Did Wordle's share button (2021-12-16) change the growth rate, or was growth already under way?
  2. When did Flappy Bird's growth start, and what was it doing before PewDiePie (2014-01-27)?
  3. Among Us before and after Sodapoppin (2020-07-15), by country.
Writes analysis/case_studies.md. Daily Trends values are normalised to the window max; zeros are below Google's threshold.
"""
import glob, os
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data", "raw", "trends", "daily")
L = ["# Case studies (daily Google Trends)", ""]


def load(name, geo):
    p = os.path.join(D, f"{name}.{geo}.csv")
    if not os.path.exists(p):
        return None
    d = pd.read_csv(p, parse_dates=["date"])
    return None if d.empty else d.set_index("date")["value"].astype(float)


def slope(s, a, b, floor=1):
    w = s[(s.index >= a) & (s.index <= b)]
    w = w[w >= floor]
    if len(w) < 5:
        return np.nan, len(w)
    x = (w.index - w.index[0]).days.values
    return float(np.polyfit(x, np.log(w.values), 1)[0]), len(w)


def first_day(s, thr):
    hit = s[s >= thr]
    return hit.index[0].date().isoformat() if len(hit) else "never"


def segs(s, cuts, label):
    rows = []
    for (a, b, nm) in cuts:
        r, n = slope(s, a, b)
        rows.append(f"| {label} | {nm} | {a} to {b} | {n} | {'n/a' if np.isnan(r) else f'{r:+.3f}'} | {'n/a' if np.isnan(r) or r <= 0 else f'{np.log(2)/r:.1f}'} |")
    return rows


# 1. Wordle
cuts_w = [("2021-11-01", "2021-12-15", "before share button"), ("2021-12-16", "2022-01-02", "share button -> before NYT profile"),
          ("2022-01-03", "2022-01-20", "after NYT profile (Jan 3)")]
L += ["## 1. Wordle: was the share grid the cause?", "",
      "Timeline (sources in the DB): 90 players on Nov 1 2021. A New Zealand player starts typing emoji grids, and NZ players copy her. Wardle ships the share button on **2021-12-16 14:54 UTC**.",
      "300,000 players on Jan 2. NYT profile on Jan 3. About 2M players by mid-January. Sold Jan 31.", "",
      "| Series | Window | Dates | Days above floor | Growth rate (ln/day) | Doubling (days) |", "|---|---|---|---|---|---|"]
for geo in ["WW", "NZ", "US", "GB", "AU", "CA"]:
    s = load("wordle", geo)
    if s is not None:
        L += segs(s, cuts_w, f"Wordle topic, {geo}")
for geo in ["WW", "NZ", "US"]:
    s = load("wordle_term", geo)
    if s is not None:
        L += segs(s, cuts_w, f"'wordle' term, {geo}")
L.append("")
fd = {geo: (first_day(load("wordle", geo), 1) if load("wordle", geo) is not None else "n/a") for geo in ["NZ", "AU", "GB", "CA", "US"]}
L.append("First day with measurable search interest (topic, >=1): " + ", ".join(f"{k} {v}" for k, v in fd.items()) + ".")
L.append("")
# Player-count arithmetic: growth before the button
r_pre = np.log(300000 / 90) / 62
L += [f"Player counts alone: 90 -> 300,000 between Nov 1 and Jan 2 is {r_pre:.3f}/day (doubling every {np.log(2)/r_pre:.1f} days). "
      "That is the average over a window in which the grid (typed by hand from about late November, NZ first) and then the button (Dec 16) both existed.", ""]

# 1b. Pre-NYT window (normalised to its own max on/near Jan 2, so December is resolvable)
cuts_wp = [("2021-11-15", "2021-12-15", "before share button"), ("2021-12-16", "2022-01-02", "after share button, before NYT profile")]
L += ["### 1b. Pre-press window only (series end 2022-01-02, so December growth is resolvable)", "",
      "| Series | Window | Dates | Days above floor | Growth rate (ln/day) | Doubling (days) |", "|---|---|---|---|---|---|"]
for geo in ["WW", "NZ", "AU", "GB", "US"]:
    s = load("wordle_pre", geo)
    if s is not None:
        L += segs(s, cuts_wp, f"'wordle', {geo}")
for geo in ["WW", "NZ"]:
    s = load("wordle_preNYT2", geo)
    if s is not None:
        L += segs(s, cuts_wp, f"'wordle' (Nov 15-Dec 31 window), {geo}")
fdp = {geo: (first_day(load("wordle_pre", geo), 1) if load("wordle_pre", geo) is not None else "n/a") for geo in ["NZ", "AU", "GB", "US", "WW"]}
L += ["", "First day with measurable interest in the pre-press window: " + ", ".join(f"{k} {v}" for k, v in fdp.items()) + ".", ""]

# 2. Flappy Bird
cuts_f = [("2013-11-01", "2013-12-12", "Nov 1 -> Dec 12 (pre top-250)"), ("2013-12-13", "2014-01-09", "Dec 13 top-250 -> Jan 9"),
          ("2014-01-10", "2014-01-26", "top-10 (Jan 10) -> before PewDiePie"), ("2014-01-27", "2014-02-08", "PewDiePie (Jan 27) -> removal")]
L += ["## 2. Flappy Bird: what changed after months of obscurity?", "",
      "Documented: 13 reviews May 25-Oct 31 2013; a bug-fix update in September; first tweet Nov 4; US game charts at #1,368 in November;",
      "top 250 free on Dec 13 as frustrated tweets begin; US top 10 on Jan 10; #1 on Jan 17; PewDiePie video Jan 27; pulled Feb 9.", "",
      "| Series | Window | Dates | Days above floor | Growth rate (ln/day) | Doubling (days) |", "|---|---|---|---|---|---|"]
for geo in ["WW", "US", "VN", "GB"]:
    s = load("flappybird", geo)
    if s is not None:
        L += segs(s, cuts_f, f"Flappy Bird, {geo}")
for geo in ["WW", "US", "VN", "GB"]:
    s = load("flappy_pre", geo)
    if s is not None:
        L += segs(s, cuts_f[:3], f"Flappy (window to Jan 16), {geo}")
for geo in ["WW", "US"]:
    s = load("flappy_pre2", geo)
    if s is not None:
        L += segs(s, [("2013-10-01", "2013-11-30", "Oct-Nov"), ("2013-12-01", "2013-12-31", "Dec")], f"Flappy (window to Dec 31), {geo}")
fdf = {geo: (first_day(load("flappy_pre", geo), 1) if load("flappy_pre", geo) is not None else "n/a") for geo in ["VN", "US", "GB", "WW"]}
L += ["", "First measurable day: " + ", ".join(f"{k} {v}" for k, v in fdf.items()) + ".", ""]

# 3. Among Us
cuts_a = [("2020-05-01", "2020-07-14", "before Sodapoppin"), ("2020-07-15", "2020-08-31", "Sodapoppin -> end Aug"), ("2020-09-01", "2020-10-31", "Sep-Oct")]
L += ["## 3. Among Us: two years of obscurity, then streamers", "",
      "| Series | Window | Dates | Days above floor | Growth rate (ln/day) | Doubling (days) |", "|---|---|---|---|---|---|"]
for geo in ["WW", "KR", "BR", "MX", "US"]:
    s = load("amongus", geo)
    if s is not None:
        L += segs(s, cuts_a, f"Among Us, {geo}")
for geo in ["WW", "KR", "BR", "US"]:
    s = load("amongus_pre", geo)
    if s is not None:
        L += segs(s, [("2020-04-01", "2020-06-30", "Apr-Jun"), ("2020-07-01", "2020-07-14", "Jul 1-14"), ("2020-07-15", "2020-07-31", "Jul 15-31 (Sodapoppin)")], f"Among Us (window to Jul 31), {geo}")
fda = {geo: (first_day(load("amongus", geo), 5) if load("amongus", geo) is not None else "n/a") for geo in ["KR", "BR", "MX", "US"]}
L += ["", "First day >= 5% of window max: " + ", ".join(f"{k} {v}" for k, v in fda.items()) + ".", ""]

# 4. Other fast breakouts
L += ["## 4. Other breakouts: daily growth in the 3 weeks before each series peaked", "", "| Game | Geo | Peak day | Growth rate (ln/day) over prior 21 days | Doubling (days) |", "|---|---|---|---|---|"]
for f in sorted(glob.glob(os.path.join(D, "*.csv"))):
    nm, geo = os.path.basename(f)[:-4].split(".")
    s = load(nm, geo)
    if s is None:
        continue
    pk = s.idxmax()
    r, n = slope(s, (pk - pd.Timedelta(days=21)).date().isoformat(), pk.date().isoformat())
    L.append(f"| {nm} | {geo} | {pk.date()} | {'n/a' if np.isnan(r) else f'{r:+.3f}'} | {'n/a' if np.isnan(r) or r <= 0 else f'{np.log(2)/r:.1f}'} |")
open(os.path.join(ROOT, "analysis", "case_studies.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
