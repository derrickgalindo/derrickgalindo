"""Revenue per daily player by model, value at 1M DAU, and sell-vs-keep arithmetic.
Every input is either derived from a filing in the DB or labelled as an assumption. Writes analysis/business_model.md."""
import os, sqlite3
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
con = sqlite3.connect(os.path.join(ROOT, "data", "viral_games.db"))
bench = pd.read_sql("SELECT * FROM monetization_benchmarks", con)
acq = pd.read_sql("SELECT * FROM acquisitions", con)

# Net revenue to the developer per DAU-day (USD): low / mid / high
MODELS = [
    ("Web daily game, display + interstitial ads", 0.005, 0.012, 0.027, 0.00002,
     "assumption: 1-2 pageviews x 3 units x $2-6 RPM; cross-checks Flappy Bird ~$0.005 (2014) and Slither.io ~$0.01 (2016) order-of-magnitude estimates"),
    ("Mobile app, ads only (hypercasual-style)", 0.03, 0.05, 0.08, 0.0001,
     "third-party benchmarks $0.03-0.08 blended ad ARPDAU; needs app-store discovery, which is mostly paid now (Rovio UA EUR69.6M in 2017)"),
    ("Mobile app, IAP (casual F2P), net of 30% store fee", 0.7 * 0.035, 0.7 * 0.055, 0.7 * 0.094, 0.0002,
     "King Q4'13 $0.055 and Rovio Q4'17 ~$0.094 gross (filings); Rovio Q2'16 ~$0.035; x0.7 store fee"),
    ("Roblox experience (creator DevEx share)", 0.004, 0.012, 0.031, 0.0,
     "platform bookings/DAU $0.138-0.141 x 22% DevEx = $0.031 per platform DAU (filings); per-experience lower because players visit several experiences a day; hosting is free"),
    ("Subscription funnel (NYT-style), 1-5% of DAU paying $3.5-6/mo", 0.01 * 3.5 / 30, 0.03 * 5 / 30, 0.05 * 6 / 30, 0.00002,
     "NYT other single-product ARPU ~$3.5/mo, bundle higher (10-K FY2025); conversion rate is an assumption"),
]


def L_table(rows, cols):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]
    return out


L = ["# Business model from evidence", "", "## Revenue per daily player (net to developer)", ""]
rows = []
for name, lo, mid, hi, cost, basis in MODELS:
    rows.append((name, f"${lo:.3f}", f"${mid:.3f}", f"${hi:.3f}", f"${mid * 365:.1f}M", f"${(mid - cost) * 365:.1f}M", basis))
L += L_table(rows, ["Model", "low", "mid", "high", "Revenue/yr at 1M DAU (mid)", "minus serving cost", "Basis"])
L += ["", "Filing-derived reference points (gross bookings per DAU-day):", ""]
L += L_table([(r.entity, r.period, f"${r.arpdau_usd:.3f}", r.quality) for r in bench.itertuples()], ["Entity", "Period", "ARPDAU", "Quality"])

# Decay-adjusted lifetime value of a 1M-DAU hit: revenue in year t = R1 * keep^(t-1)
L += ["", "## Keep vs sell", "",
      "A hit's attention decays. Using the Trends result that the median hit keeps about 30% of peak interest a year later (a fad),",
      "versus the roughly 35-50% that durable daily rituals keep (Wordle and Connections in this dataset):", ""]
rows = []
for name, lo, mid, hi, cost, basis in MODELS:
    r1 = (mid - cost) * 365  # $M at 1M avg DAU in year 1
    for label, keep in (("fad (30%/yr)", 0.30), ("ritual (50%/yr)", 0.50)):
        npv = sum(r1 * keep ** t / 1.15 ** t for t in range(5))
        rows.append((name, label, f"${r1:.1f}M", f"${npv:.1f}M"))
L += L_table(rows, ["Model", "Decay", "Year-1 net revenue at 1M avg DAU", "5-yr value kept (15% discount)"])
L += ["", "What buyers actually paid (from the acquisitions table):", ""]
L += L_table([(a.acquirer, a.target, a.deal_date, "undisclosed" if pd.isna(a.price_usd_m) else ("low 7 figures (>= $1M)" if a.deal_id == "nyt_wordle" else f"${a.price_usd_m:,.1f}M"), a.what_bought, a.after_outcome or "")
              for a in acq.itertuples()], ["Acquirer", "Target", "Date", "Price", "What they bought", "What happened"])
L += ["",
      "- Audience-only deals (no revenue) priced low: Wordle went for 'low seven figures' with ~2M daily players, roughly **$0.5-1 per daily player**.",
      "- Buying at the peak backfired: Zynga paid $183.1M for OMGPOP at about 14M DAU (~$13 per daily player), then wrote off $95.5M (52%) six months later as DAU fell.",
      "- Revenue businesses sell on revenue: Scopely paid $3.5B for Niantic's games, which had more than $1B in 2024 revenue (~3.5x).",
      "- Early equity, not exits: Splitting Point bought about half of Grow a Garden at ~1,000 concurrent players, before the run to 22M.",
      "- The metrics buyers disclosed, from the filings: DAU, MAU, unique payers, bookings per DAU (Zynga ABPU, King MUP bookings, Roblox ABPDAU),",
      "  concentration (Candy Crush was 78% of King's bookings), retention, and for subscription buyers, conversion to subscribers (NYT 'tens of millions of new users').",
      ""]
open(os.path.join(ROOT, "analysis", "business_model.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
