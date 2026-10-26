"""Fit each offense's efficiency knob so the simulated scores match the market."""
from __future__ import annotations

import math

import numpy as np

from .sim import GameSim


def mean_from_ladder(ladder: dict[float, float]) -> float:
    """E[X] for a non-negative integer score from P(X > line) at half-point lines (linear interp)."""
    xs = sorted(ladder)
    ps = [ladder[x] for x in xs]
    xs, ps = [-0.5] + xs + [xs[-1] + 12], [1.0] + ps + [0.0]
    return float(sum(np.interp(k + 0.5, xs, ps) for k in range(0, 80)))


def calibrate(make_sim, targets: dict, n: int = 6000, iters: int = 8, tol: float = 0.25, log=print):
    """make_sim(dal_mult, phi_mult) -> GameSim. targets: {'fav': 'DAL', 'dog': 'PHI', 'fav_mean': .., 'dog_mean': ..}.

    Adjusts each team's yards multiplier until the simulated mean points sit within `tol` of the
    market-implied means. Returns the multipliers and the last simulated frame."""
    fm, dm = 1.0, 1.0
    df = None
    for i in range(iters):
        sim: GameSim = make_sim(fm, dm)
        df = sim.run(n)
        f_mean, d_mean = df[f"{targets['fav']}_pts"].mean(), df[f"{targets['dog']}_pts"].mean()
        log(f"  iter {i}: mults {targets['fav']}={fm:.3f} {targets['dog']}={dm:.3f} -> "
            f"means {f_mean:.2f}/{d_mean:.2f} (target {targets['fav_mean']:.2f}/{targets['dog_mean']:.2f})")
        if abs(f_mean - targets["fav_mean"]) < tol and abs(d_mean - targets["dog_mean"]) < tol:
            break
        # points scale roughly with yards^1.6 in this sim; damp the step
        fm *= math.exp(0.55 * math.log(targets["fav_mean"] / f_mean))
        dm *= math.exp(0.55 * math.log(targets["dog_mean"] / d_mean))
    return fm, dm, df


def check(df, fav: str, dog: str, spread: float, total: float) -> dict:
    m = df[f"{fav}_pts"] - df[f"{dog}_pts"]
    return {
        "median_margin": float(m.median()), "mean_margin": float(m.mean()), "sd_margin": float(m.std()),
        "median_total": float(df.total.median()), "mean_total": float(df.total.mean()), "sd_total": float(df.total.std()),
        f"P({fav} win)": float((m > 0).mean() + 0.5 * (m == 0).mean()),
        f"P({fav} -{spread})": float((m > spread).mean()),
        f"P(over {total})": float((df.total > total).mean()),
        "P(margin=3)": float((m.abs() == 3).mean()), "P(margin=7)": float((m.abs() == 7).mean()),
        "P(OT tie)": float((m == 0).mean()),
    }
