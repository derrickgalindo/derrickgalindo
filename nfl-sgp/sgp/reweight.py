"""Rake simulated games so the margin and total distributions match the market's ladders.

The play-level sim gets the dependence between stats right (game script, shared
form) but not every detail of the score distribution (e.g. how often games land
on 3). Iterative proportional fitting assigns each simulated game a weight so the
weighted margin and total match the market at every listed line while changing
the games as little as possible; every leg and combo is then priced with these
weights. Effective sample size is reported so heavy reweighting is visible.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _bins(values: np.ndarray, ladder: dict[float, float]):
    """ladder: {line: P(X > line)} -> (bin index per sim row, target prob per bin)."""
    lines = sorted(ladder)
    probs = np.array([ladder[x] for x in lines])
    probs = np.minimum.accumulate(np.clip(probs, 1e-4, 1 - 1e-4))  # enforce monotone survival
    surv = np.concatenate([[1.0], probs, [0.0]])
    target = surv[:-1] - surv[1:]
    idx = np.searchsorted(np.array(lines), values, side="left")  # X <= line -> bin of that line
    return idx, np.maximum(target, 1e-5)


def rake(df: pd.DataFrame, constraints: list[tuple[str, dict[float, float]]], iters: int = 200) -> np.ndarray:
    w = np.ones(len(df)) / len(df)
    parts = [_bins(df[col].to_numpy(), ladder) for col, ladder in constraints]
    for _ in range(iters):
        for idx, target in parts:
            cur = np.bincount(idx, weights=w, minlength=len(target))
            ratio = np.where(cur > 0, target / np.maximum(cur, 1e-12), 1.0)
            w = w * ratio[idx]
            w /= w.sum()
    return w


def ess(w: np.ndarray) -> float:
    return float(w.sum() ** 2 / (w ** 2).sum())


def wprob(mask: np.ndarray, w: np.ndarray) -> float:
    return float((w * mask).sum() / w.sum())


def wquantile(x: np.ndarray, w: np.ndarray, q: float) -> float:
    o = np.argsort(x)
    c = np.cumsum(w[o]) / w.sum()
    return float(x[o][np.searchsorted(c, q)])
