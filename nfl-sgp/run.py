"""End-to-end SGP finder for one game.

    python run.py games/2026_07_DAL_PHI --sims 30000

Expects in the game folder: teams.py (dallas()/philly()-style builders exposed as
HOME/AWAY via build()), legs.py (LEGS, ladders, TARGET_MEANS, SGP_QUOTES).
Writes results.json and prints the tables the report is built from.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sgp.calibrate import calibrate, check  # noqa: E402
from sgp.markets import dec_to_am, kelly_fraction  # noqa: E402
from sgp.price import Pricer, fit_book_correlation, price_combos, price_legs  # noqa: E402
from sgp.reweight import ess, rake  # noqa: E402
from sgp.sim import GameSim  # noqa: E402


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("game_dir")
    ap.add_argument("--sims", type=int, default=30000)
    ap.add_argument("--cal-sims", type=int, default=6000)
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--model-weight", type=float, default=0.0,
                    help="weight on the raw sim vs market fair for legs without a named edge "
                         "(0 = only legs with a written-down edge source get a probability other than the market's)")
    ap.add_argument("--hold-per-leg", type=float, default=0.05, help="SGP margin per leg the book charges")
    ap.add_argument("--alpha", type=float, default=1.0,
                    help="share of simulated correlation the book prices in for the base case")
    ap.add_argument("--min-ev", type=float, default=0.05, help="pass threshold on estimated EV")
    args = ap.parse_args()

    teams = _load(os.path.join(args.game_dir, "teams.py"), "teams")
    legs_mod = _load(os.path.join(args.game_dir, "legs.py"), "legs")
    home_fn, away_fn = teams.HOME, teams.AWAY
    fav, dog = legs_mod.FAV, legs_mod.DOG
    tm = legs_mod.TARGET_MEANS
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    pd.set_option("display.max_colwidth", 90)

    def make(fm, dm, seed=args.seed):
        h, a = home_fn(), away_fn()
        for t in (h, a):
            m = fm if t.name == fav else dm
            t.pass_yds_mult = t.rush_yds_mult = m
        return GameSim(home=h, away=a, seed=seed)

    print("== 1. calibrate efficiency to market-implied team means")
    fm, dm, _ = calibrate(make, {"fav": fav, "dog": dog, "fav_mean": tm[fav], "dog_mean": tm[dog]}, n=args.cal_sims)
    df = make(fm, dm, seed=args.seed + 1).run(args.sims)
    raw = check(df, fav, dog, legs_mod.SPREAD, legs_mod.TOTAL)
    print("   raw sim:", {k: round(v, 3) for k, v in raw.items()})

    print("== 2. rake to the market's margin and total ladders")
    w = rake(df, [(f"{fav}_margin", legs_mod.MARGIN_LADDER), ("total", legs_mod.TOTAL_LADDER)])
    m = df[f"{fav}_margin"].to_numpy()
    t = df["total"].to_numpy()
    from sgp.reweight import wprob, wquantile
    cal = {
        "median_margin": wquantile(m, w, 0.5), "median_total": wquantile(t, w, 0.5),
        f"P({fav} -{legs_mod.SPREAD})": wprob(m > legs_mod.SPREAD, w),
        f"P(over {legs_mod.TOTAL})": wprob(t > legs_mod.TOTAL, w),
        f"P({fav} win)": wprob(m > 0, w) + 0.5 * wprob(m == 0, w),
        f"mean {fav}": float((df[f'{fav}_pts'] * w).sum()), f"mean {dog}": float((df[f'{dog}_pts'] * w).sum()),
        "ESS": ess(w), "n": len(df),
    }
    print("   raked:", {k: round(v, 3) for k, v in cal.items()})

    pricer = Pricer(df, w)
    print("== 3. legs")
    L = price_legs(pricer, legs_mod.LEGS, model_weight=args.model_weight)
    print(L[["label", "fair", "p_sim", "p_mine", "best_book", "best_am", "ev_best", "edge_named"]].round(3).to_string())

    print("== 4. how books priced correlation on quoted SGPs")
    fits = fit_book_correlation(pricer, legs_mod.SGP_QUOTES, args.hold_per_leg)
    for f in fits:
        print("  ", {k: (round(v, 3) if isinstance(v, float) else v) for k, v in f.items()})
    alphas = [f["alpha"] for f in fits if np.isfinite(f["alpha"])]
    print(f"   implied alpha from quotes (confounded with hold, not trusted): {np.round(alphas, 2).tolist()}")
    alpha = args.alpha
    print(f"   base case alpha={alpha:.2f}; sensitivity alpha=0.5")

    print("== 5. combos")
    pool = legs_mod.POOL
    C = price_combos(pricer, L, legs_mod.LEGS, pool, alpha, args.hold_per_leg)
    C["min_price_am"] = [dec_to_am((1 + args.min_ev) / p) for p in C.p_sim]
    cols = ["legs", "k", "p_sim", "p_mkt_corr", "corr_lift", "fair_am", "min_price_am", "est_book_am", "ev_est", "ev_est_halfedge", "alt_book_am", "ev_alt", "ceiling_book", "ceiling_am", "ev_ceiling", "qkelly"]
    print(C[cols].head(25).round(3).to_string(index=False))
    passing = C[(C.ev_est >= args.min_ev) & (C.ev_est_halfedge > 0) & ~C.thin]
    print("== 6. correlation shopping list: strongest positive correlation, priced at fair (check the app)")
    shop = C[~C.thin & (C.k <= 3) & (C.corr_lift >= 1.25)].sort_values("corr_lift", ascending=False)
    print(shop[["legs", "p_sim", "p_mkt_indep", "corr_lift", "fair_am", "min_price_am", "ceiling_book", "ceiling_am"]].head(15).round(3).to_string(index=False))

    print("== 7. quoted SGPs at their quoted prices")
    for f in fits:
        p = f["p_corr_sim"]
        half = (f["p_corr_sim"] + f["p_indep"]) / 2
        dec = 1 / f["p_quote"]
        print(f"   {f['book']} +{f['price']}: sim {p:.3f} fair {dec_to_am(1 / p)} min {dec_to_am((1 + args.min_ev) / p)} "
              f"EV {p * dec - 1:+.1%}  EV@half-correlation {half * dec - 1:+.1%}  qKelly {min(0.01, 0.25 * kelly_fraction(p, dec)):.2%}")
    print(f"   combos clearing EV>={args.min_ev:.0%} and still +EV at half the edge: {len(passing)} of {len(C)}")

    out = {"shopping_list": shop.head(15).drop(columns=["ids"]).to_dict("records"), "calibration_raw": raw, "calibration_raked": cal, "alpha": alpha, "book_fits": fits,
           "legs": L.drop(columns=["books"]).reset_index().to_dict("records"),
           "top_combos": C.head(40).drop(columns=["ids"]).to_dict("records"),
           "n_combos": len(C), "n_passing": len(passing), "multipliers": {fav: fm, dog: dm}}
    with open(os.path.join(args.game_dir, "results.json"), "w") as f:
        json.dump(out, f, indent=1, default=float)
    C.drop(columns=["ids"]).to_csv(os.path.join(args.game_dir, "combos.csv"), index=False)


if __name__ == "__main__":
    main()
