"""Attempts to break the 'repeatable recipe, simplicity at the core' hypothesis.
Writes analysis/premise_tests.md."""
import os, sqlite3
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
con = sqlite3.connect(os.path.join(ROOT, "data", "viral_games.db"))
g = pd.read_sql("SELECT g.*, f.* FROM games g JOIN features f USING(game_id) WHERE g.cohort != 'wordle_census'", con)
g = g.loc[:, ~g.columns.duplicated()]
g["hit"] = (g.outcome_tier >= 2).astype(int)
b = pd.read_sql("SELECT b.*, g.name, g.outcome_tier, g.role FROM breakouts b JOIN games g USING(game_id)", con)
tm = pd.read_sql("SELECT t.*, g.name, g.outcome_tier, g.era, g.platform FROM trends_metrics t JOIN games g USING(game_id)", con)
L = ["# Premise tests: is there a repeatable recipe with simplicity at its core?", ""]


def table(df):
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        out.append("| " + " | ".join("" if pd.isna(v) else (f"{v:.2f}" if isinstance(v, float) else str(v)) for v in r.values) + " |")
    return out


# 1. Simplicity is not discriminating
simple = (g.one_input == 1) & (g.session_min <= 5) & (g.ttff_sec <= 10)
L += ["## 1. Simplicity: present in hits and flops alike", "",
      f"- Games meeting all three simplicity criteria (one input, session <= 5 min, first fun <= 10 s): {simple.sum()} of {len(g)}.",
      f"- Hit rate among the simple games: {g[simple].hit.mean():.0%}. Among the rest: {g[~simple].hit.mean():.0%}.",
      f"- Simple games that were NOT hits: {', '.join(g[simple & (g.hit == 0)].name.tolist())}.",
      f"- Hits that were NOT simple: {', '.join(g[~simple & (g.hit == 1)].name.tolist())}.", ""]

# 2. Clones vs originals
cohorts = []
for c, d in g.groupby("cohort"):
    if len(d) < 2:
        continue
    best = d.sort_values(["outcome_tier"], ascending=False).iloc[0]
    orig = d[d.role.isin(["original_hit", "predecessor"])]
    cohorts.append({"cohort": c, "games": len(d), "hits": int(d.hit.sum()), "biggest": best["name"], "biggest_role": best.role})
cdf = pd.DataFrame(cohorts)
L += ["## 2. Within each cohort, did the original win?", ""] + table(cdf) + [""]
pairs = [("Threes (original, premium)", "2048 (free web clone of a clone)", "clone won"),
         ("Farm Town (Feb 2009)", "FarmVille (Jun 2009)", "clone won (platform cross-promo + paid)"),
         ("Mob Wars (Jan 2008)", "Mafia Wars (Jun 2008)", "clone won"),
         ("Agar.io (2015)", "Slither.io (2016)", "both hits; clone similar or larger"),
         ("Fall Guys (2020)", "Stumble Guys (mobile, 2020-21)", "clone reached 20M DAU on the platform the original skipped"),
         ("Merge Big Watermelon (CN web, Jan 2021)", "Suika Game (Switch Dec 2021, viral Sep 2023)", "clone won globally"),
         ("Ingress (2012, same mechanic, no IP)", "Pokemon GO (2016, IP)", "same studio; IP + channel won"),
         ("Flappy Bird", "300+ clones in 4 days; ~1/3 of new iOS games on 2014-02-27", "original won; clones did not stick"),
         ("Wordle", "~140 English Wordle-likes in census", "original won; see base rates"),
         ("Draw My Thing (OMGPOP web, 2008)", "Draw Something (OMGPOP mobile, 2012)", "same game on a new channel won")]
L += ["Head-to-head pairs where the timing is well documented:", ""] + table(pd.DataFrame(pairs, columns=["first", "follower", "outcome"])) + [""]

# 3. Same-creator follow-ups: skill + recipe + attention held constant
fu = g[g.role == "same_creator"][["name", "developer", "outcome_tier", "paid_ua", "creator_audience"]]
L += ["## 3. The same creators repeating their own recipe", "",
      "Follow-ups hold the creator's skill and recipe constant, and they launch with attention the original never had.", ""] + table(fu) + [
      "", f"Follow-ups that reached hit tier: {int((fu.outcome_tier >= 2).sum())}/{len(fu)}; "
      f"without paid UA or cross-promotion: {int(((fu.outcome_tier >= 2) & (fu.paid_ua == 0)).sum())}/{int((fu.paid_ua == 0).sum())}.", ""]

# 4. Ignition: what actually started each breakout
L += ["## 4. Ignition: what started each documented breakout", ""] + table(
    b[["name", "latent_days", "ignition_type", "first_community", "influencer_timing"]].sort_values("latent_days", ascending=False)) + [""]
zero_aud = b.merge(g[["game_id", "creator_audience", "ip_licensed", "paid_ua"]], on="game_id")
za = zero_aud[(zero_aud.creator_audience == 0) & (zero_aud.ip_licensed == 0) & (zero_aud.paid_ua == 0) & (zero_aud.outcome_tier >= 2)]
L += [f"- Zero-audience, no-IP, no-paid hits with a documented breakout: {len(za)}. Median latent period before breakout: "
      f"**{za.latent_days.median():.0f} days** (range {za.latent_days.min()}-{za.latent_days.max()}).",
      f"- Influencer timing among those: " + ", ".join(f"{k}: {v}" for k, v in za.influencer_timing.value_counts().items()) + ".", ""]

# 5. Channel newness
ch = g.groupby("platform_newness").hit.agg(["count", "mean"]).reset_index().rename(columns={"count": "games", "mean": "hit_rate"})
L += ["## 5. Riding a new channel", ""] + table(ch) + [""]

# 6. Attention decay (Trends)
if len(tm):
    tm["hit"] = (tm.outcome_tier >= 2).astype(int)
    d = tm[tm.hit == 1].dropna(subset=["half_life_weeks"])
    L += ["## 6. How fast hits fade (Google Trends, weekly)", "",
          f"Hits with trends data: {len(d)}. Median weeks from peak until search interest halves: **{d.half_life_weeks.median():.0f}**. "
          f"Median interest one year after peak: **{d.retained_share_52w.median():.0%} of peak**.", ""] + table(
        d.sort_values("retained_share_52w", ascending=False)[["name", "era", "peak_date", "half_life_weeks", "retained_share_52w"]]) + [""]

open(os.path.join(ROOT, "analysis", "premise_tests.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
