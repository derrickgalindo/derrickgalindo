"""Monte Carlo adoption model for an AI film-tagging add-on among Texas UIL 11-man programs.

This is a model of stated assumptions, not evidence. Every prior below is labelled and is meant
to be replaced by interview and pilot data (see the 90-day plan). What it is good for: showing
which levers dominate (price, core-column accuracy, Hudl's automation date) and how wide the
uncertainty is.

Structure (one draw = one possible world; each world simulates every program):
  value_i  = WTP_i * (w_speed*S + w_cols*C + w_corr*K(acc))   per season, in $
  adopt    if aware and value_i - price > friction_i and not vetoed
  aware    follows annual Bass diffusion (p, q) across the population
  churn    adopters re-decide each season with the same rule plus annual random churn
  Hudl     from its automation season on, S -> 0, K -> 0, C -> C * keep_cols

Usage: python -I adoption_sim.py OUT_DIR
"""

import csv
import json
import os
import sys

import numpy as np

# UIL 2024-26 alignment, 11-man football programs by conference (counted from
# https://www.uiltexas.org/files/alignments/All_post_alpha_by_conf.pdf).
PROGRAMS = {"6A": 247, "5A": 250, "4A": 200, "3A": 201, "2A": 197, "1A": 9}

# Prior: median willingness to pay per program per season ($), by conference.
# Anchors: whole-school Hudl packages run $8.7k-$15.5k/yr (procurement section);
# MaxPreps Advantage human breakdowns sell for $600/team; Balltime HS volleyball $499/season.
WTP_MEDIAN = {"6A": 1400, "5A": 1100, "4A": 800, "3A": 600, "2A": 450, "1A": 350}
WTP_SIGMA = 0.6  # lognormal spread across programs

SEASONS = [2027, 2028, 2029, 2030]  # 2027 = free pilot season; paid from 2028
N_DRAWS = 1000


def draw_world(rng):
    """Parameter uncertainty: one plausible set of market facts."""
    return {
        "p": rng.uniform(0.02, 0.08),       # Bass innovation coef. (annual); meta-analysis mean 0.03
        "q": rng.uniform(0.20, 0.50),       # Bass imitation coef.; meta-analysis mean 0.38
        "w_speed": rng.uniform(0.25, 0.50),  # share of value from Saturday-morning delivery
        "w_cols": rng.uniform(0.20, 0.45),   # share from columns Assist skips (personnel, D, own terms)
        "parity": rng.uniform(0.92, 0.97),   # Assist's core-column accuracy (unpublished; prior)
        "floor_lo": 0.82, "floor_hi": 0.93,  # range of the accuracy below which a coach quits
        "friction_med": rng.uniform(150, 500),  # $-equivalent switching/approval friction
        "veto": rng.uniform(0.05, 0.25),     # AD/district says "we already pay Hudl"
        "churn": rng.uniform(0.08, 0.25),    # random annual churn among satisfied users
        "keep_cols": rng.uniform(0.3, 0.8),  # share of column value left after Hudl automates
    }


def simulate(rng, world, price, acc, hudl_season, programs):
    conf = np.concatenate([[c] * n for c, n in programs.items()])
    n = len(conf)
    wtp = np.array([WTP_MEDIAN[c] for c in conf]) * np.exp(rng.normal(0, WTP_SIGMA, n))
    floor = rng.uniform(world["floor_lo"], world["floor_hi"], n)
    friction = world["friction_med"] * np.exp(rng.normal(0, 0.5, n))
    veto = rng.random(n) < world["veto"]
    w_corr = max(0.0, 1 - world["w_speed"] - world["w_cols"])

    # Accuracy: below a coach's floor the tool is worthless; corrections value grows past parity.
    usable = acc >= floor
    corr = np.clip((acc - floor) / np.maximum(world["parity"] - floor, 1e-6), 0, 1.5)

    aware = np.zeros(n, bool)
    active = np.zeros(n, bool)
    out = []
    for s in SEASONS:
        # Bass awareness update on the population, seeded by the pilot season.
        frac_aware = aware.mean()
        p_new = world["p"] + world["q"] * frac_aware
        aware |= rng.random(n) < p_new

        hudl_on = hudl_season is not None and s >= hudl_season
        speed = 0.0 if hudl_on else 1.0
        cols = world["keep_cols"] if hudl_on else 1.0
        k = np.zeros(n) if hudl_on else corr
        value = wtp * (world["w_speed"] * speed + world["w_cols"] * cols + w_corr * k)
        value = np.where(usable, value, 0.0)

        eff_price = 0.0 if s == SEASONS[0] else price  # pilot season is free
        wants = aware & ~veto & (value - eff_price > friction)
        stays = active & wants & (rng.random(n) > world["churn"])
        joins = ~active & wants
        active = stays | joins
        out.append({"season": s, "adopters": int(active.sum()),
                    "arr": float(active.sum() * eff_price)})
    return out


def main():
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    rng = np.random.default_rng(20261023)
    worlds = [draw_world(rng) for _ in range(N_DRAWS)]
    total = sum(PROGRAMS.values())

    prices = [300, 600, 900, 1200, 1800]
    accs = [0.85, 0.90, 0.93, 0.95, 0.97]
    hudls = {"never": None, "2029": 2029, "2028": 2028}

    rows = []
    for hname, hs in hudls.items():
        for price in prices:
            for acc in accs:
                a30, r30 = [], []
                for w in worlds:
                    res = simulate(rng, w, price, acc, hs, PROGRAMS)
                    a30.append(res[-1]["adopters"])
                    r30.append(res[-1]["arr"])
                a30 = np.array(a30)
                r30 = np.array(r30)
                rows.append({
                    "hudl_automates": hname, "price": price, "accuracy": acc,
                    "adopters_2030_p10": int(np.percentile(a30, 10)),
                    "adopters_2030_p50": int(np.percentile(a30, 50)),
                    "adopters_2030_p90": int(np.percentile(a30, 90)),
                    "share_2030_p50": float(np.percentile(a30, 50) / total),
                    "arr_2030_p10": float(np.percentile(r30, 10)),
                    "arr_2030_p50": float(np.percentile(r30, 50)),
                    "arr_2030_p90": float(np.percentile(r30, 90)),
                })
    with open(os.path.join(out_dir, "adoption_grid.csv"), "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0]))
        wr.writeheader()
        wr.writerows(rows)

    # Trajectory for the base case, by Hudl scenario.
    traj = {}
    for hname, hs in hudls.items():
        per = {s: [] for s in SEASONS}
        for w in worlds:
            for r in simulate(rng, w, 900, 0.95, hs, PROGRAMS):
                per[r["season"]].append(r["adopters"])
        traj[hname] = {s: [int(np.percentile(v, q)) for q in (10, 50, 90)] for s, v in per.items()}
    with open(os.path.join(out_dir, "adoption_trajectory.json"), "w") as fh:
        json.dump({"total_programs": total, "base_price": 900, "base_accuracy": 0.95,
                   "trajectory_p10_p50_p90": traj}, fh, indent=1)

    print("programs:", total)
    for r in rows:
        if r["hudl_automates"] == "never" and r["accuracy"] in (0.90, 0.95):
            print(r)
    print(json.dumps(traj, indent=1))


if __name__ == "__main__":
    main()
