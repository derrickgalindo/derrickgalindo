"""Odds conversion, vig removal, Kalshi price pulls."""
from __future__ import annotations

import math

import requests

KALSHI = "https://api.elections.kalshi.com/trade-api/v2"


def am_to_dec(a: float) -> float:
    return 1 + (a / 100 if a > 0 else 100 / -a)


def dec_to_am(d: float) -> float:
    return round((d - 1) * 100) if d >= 2 else round(-100 / (d - 1))


def implied(a: float) -> float:
    return 1 / am_to_dec(a)


def devig_two_way(a_yes: float, a_no: float, method: str = "power") -> float:
    """Fair probability of the 'yes' side from a two-way American price pair."""
    p1, p2 = implied(a_yes), implied(a_no)
    if method == "multiplicative":
        return p1 / (p1 + p2)
    # power method: find k with p1^k + p2^k = 1 (handles favourite-longshot bias better)
    lo, hi = 0.5, 2.5
    for _ in range(60):
        k = (lo + hi) / 2
        if p1 ** k + p2 ** k > 1:
            lo = k
        else:
            hi = k
    return p1 ** k


def devig_one_way(a_yes: float, overround: float) -> float:
    """Fair prob for a one-sided market (e.g. anytime TD) given the book's typical overround on it."""
    return implied(a_yes) / (1 + overround)


def kalshi_markets(event_ticker: str) -> list[dict]:
    r = requests.get(f"{KALSHI}/markets", params={"event_ticker": event_ticker, "limit": 500}, timeout=20)
    r.raise_for_status()
    return r.json().get("markets", [])


def kalshi_mid(m: dict) -> float | None:
    b, a = float(m.get("yes_bid_dollars") or 0), float(m.get("yes_ask_dollars") or 0)
    if a <= 0 or a - b > 0.06:  # empty or too wide to trust
        return None
    return (a + b) / 2


def kalshi_ladder(event_prefix: str, game_suffix: str, series: list[str]) -> dict[str, float]:
    """{market_ticker_tail: mid probability} for every listed Kalshi series on this game."""
    out = {}
    for s in series:
        for m in kalshi_markets(f"{s}-{game_suffix}"):
            mid = kalshi_mid(m)
            if mid is not None:
                out[f"{s}:{m['ticker'].split('-', 2)[-1]}"] = mid
    return out


def kelly_fraction(p: float, dec: float) -> float:
    b = dec - 1
    return max(0.0, (b * p - (1 - p)) / b)


def fair_dec(p: float) -> float:
    return math.inf if p <= 0 else 1 / p
