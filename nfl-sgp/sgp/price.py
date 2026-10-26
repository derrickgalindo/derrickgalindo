"""Price legs and parlays from the raked simulation.

Joint probabilities use the simulation's dependence structure (an empirical copula)
with each leg's marginal pinned to a chosen probability: the market's fair price,
my estimate, or the midpoint. Discrete stats are jittered by U(0,1) so thresholds
can hit any marginal; the jitter is shared per stat column, so two legs on the
same stat stay consistent.
"""
from __future__ import annotations

import itertools
import math

import numpy as np
import pandas as pd

from .markets import am_to_dec, dec_to_am, devig_two_way, implied, kelly_fraction
from .reweight import wprob, wquantile

ONE_WAY_OVERROUND = 0.12  # typical hold baked into a one-sided TD price


def market_fair(leg: dict) -> tuple[float, dict]:
    vals = {}
    for book, (yes, no) in leg["books"].items():
        vals[book] = devig_two_way(yes, no) if no is not None else implied(yes) / (1 + ONE_WAY_OVERROUND)
    books = float(np.mean(list(vals.values())))
    k = leg.get("kalshi")
    one_way = all(no is None for _, no in leg["books"].values())
    if k is None:
        return books, vals
    # one-sided book prices can't be devigged reliably: lean on the exchange there
    return (0.75 * k + 0.25 * books) if one_way else (0.5 * k + 0.5 * books), vals


def best_price(leg: dict) -> tuple[str, float]:
    book, (yes, _) = max(leg["books"].items(), key=lambda kv: am_to_dec(kv[1][0]))
    return book, yes


class Pricer:
    def __init__(self, df: pd.DataFrame, w: np.ndarray, seed: int = 3):
        self.df, self.w = df, w
        rng = np.random.default_rng(seed)
        self._jit, self._hits = {}, {}
        self._rng = rng

    def _x(self, col: str) -> np.ndarray:
        if col not in self._jit:
            x = self.df[col].to_numpy(dtype=float)
            if np.allclose(x, np.round(x)):
                x = x + self._rng.random(len(x))  # spreads integer ties over [k, k+1)
            self._jit[col] = x
        return self._jit[col]

    def raw(self, col: str, side: str, line: float) -> float:
        x = self.df[col].to_numpy(dtype=float)
        return wprob(x > line if side == "over" else x < line, self.w)

    def hit(self, col: str, side: str, p: float) -> np.ndarray:
        key = (col, side, round(p, 6))
        if key not in self._hits:
            x = self._x(col)
            self._hits[key] = x > wquantile(x, self.w, 1 - p) if side == "over" else x < wquantile(x, self.w, p)
        return self._hits[key]

    def joint(self, legs: list[tuple[str, str, float]]) -> float:
        m = np.ones(len(self.df), dtype=bool)
        for col, side, p in legs:
            m &= self.hit(col, side, p)
        return wprob(m, self.w)


def price_legs(pricer: Pricer, legs: list[dict], model_weight: float = 0.3) -> pd.DataFrame:
    rows = []
    for L in legs:
        fair, per_book = market_fair(L)
        book, am = best_price(L)
        dec = am_to_dec(am)
        p_sim = pricer.raw(L["col"], L["side"], L["line"])
        mine = L.get("mine")
        p_mine = mine if mine is not None else model_weight * p_sim + (1 - model_weight) * fair
        rows.append(dict(id=L["id"], label=L["label"], col=L["col"], side=L["side"], line=L["line"],
                         fair=fair, p_sim=p_sim, p_mine=p_mine, best_book=book, best_am=am, best_dec=dec,
                         ev_best=p_mine * dec - 1, edge_named=bool(L.get("source")),
                         source=L.get("source", ""), books=L["books"]))
    return pd.DataFrame(rows).set_index("id")


def fit_book_correlation(pricer: Pricer, quotes: list[dict], hold_per_leg: float = 0.045) -> list[dict]:
    """How much of the true correlation each quoted SGP price passes through (alpha=1: fully priced)."""
    out = []
    for q in quotes:
        legs = q["legs"]
        p_ind = math.prod(p for *_, p in legs)
        p_cor = pricer.joint([(c, s, p) for c, s, _, p in legs])
        p_q = 1 / am_to_dec(q["price"])
        p_book = p_q / (1 + hold_per_leg) ** len(legs)
        alpha = (p_book - p_ind) / (p_cor - p_ind) if abs(p_cor - p_ind) > 1e-6 else float("nan")
        out.append(dict(book=q["book"], price=q["price"], n=len(legs), p_indep=p_ind, p_corr_sim=p_cor,
                        p_quote=p_q, alpha=alpha, ev_at_quote=p_cor * am_to_dec(q["price"]) - 1))
    return out


def same_market(a: dict, b: dict) -> bool:
    # opposite sides of one stat, or a team result priced twice (spread + ML of the same game)
    if a["col"] == b["col"] and a["side"] != b["side"]:
        return True
    return {a["col"], b["col"]} == {"DAL_margin"}


def price_combos(pricer: Pricer, legs: pd.DataFrame, raw_legs: list[dict], pool: list[str],
                 alpha: float, hold_per_leg: float, sizes=(2, 3, 4), alpha_alt: float = 0.5) -> pd.DataFrame:
    """alpha: share of the simulated correlation the book prices in (1 = book prices it exactly as I do).
    The base case is alpha=1, so a combo only shows value from leg edges or extra correlation the book
    misses; alpha_alt shows what happens if the book only prices half the correlation."""
    by_id = {L["id"]: L for L in raw_legs}
    rows = []
    for k in sizes:
        for combo in itertools.combinations(pool, k):
            Ls = [by_id[i] for i in combo]
            if any(same_market(a, b) for a, b in itertools.combinations(Ls, 2)):
                continue
            r = legs.loc[list(combo)]
            mine = [(x.col, x.side, x.p_mine) for x in r.itertuples()]
            mkt = [(x.col, x.side, x.fair) for x in r.itertuples()]
            mid = [(x.col, x.side, (x.p_mine + x.fair) / 2) for x in r.itertuples()]
            p_mine, p_mkt, p_mid = pricer.joint(mine), pricer.joint(mkt), pricer.joint(mid)
            p_ind = float(np.prod(r.fair))
            # best single book that offers every leg: independent product of its own prices = ceiling
            books = set.intersection(*[set(L["books"]) for L in Ls])
            ceil_book, ceil_dec = None, 0.0
            for b in books:
                d = math.prod(am_to_dec(by_id[i]["books"][b][0]) for i in combo)
                if d > ceil_dec:
                    ceil_book, ceil_dec = b, d
            est_dec = 1 / ((p_ind + alpha * (p_mkt - p_ind)) * (1 + hold_per_leg) ** k)
            alt_dec = 1 / ((p_ind + alpha_alt * (p_mkt - p_ind)) * (1 + hold_per_leg) ** k)
            rows.append(dict(
                legs=" + ".join(r.label), k=k, p_sim=p_mine, p_mid=p_mid, p_mkt_corr=p_mkt, p_mkt_indep=p_ind,
                corr_lift=p_mkt / p_ind, fair_am=dec_to_am(1 / p_mine), breakeven_am=dec_to_am(1 / p_mine),
                est_book_am=dec_to_am(est_dec), est_book_dec=est_dec,
                ev_est=p_mine * est_dec - 1, ev_est_halfedge=p_mid * est_dec - 1,
                alt_book_am=dec_to_am(alt_dec), ev_alt=p_mine * alt_dec - 1,
                min_price_am=None,
                ceiling_book=ceil_book, ceiling_am=dec_to_am(ceil_dec) if ceil_dec else None,
                ev_ceiling=p_mine * ceil_dec - 1 if ceil_dec else None,
                qkelly=min(0.01, 0.25 * kelly_fraction(p_mine, est_dec)),
                ids=combo,
            ))
    out = pd.DataFrame(rows)
    # joint probabilities under ~5% rest on too few weighted sims to rank on
    out["thin"] = out.p_sim < 0.05
    return out.sort_values(["thin", "ev_est"], ascending=[True, False])
