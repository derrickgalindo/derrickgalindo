"""DAU arithmetic and share-driven k-factor (epidemiology) for the 1M-DAU-in-90-days target.

Model: share-on-play virality. Every active player-day produces kappa new installs (kappa = shares seen x
conversion). With retention curve ret(d) = fraction of an install cohort active d days after install:
    installs(t) = seed(t) + kappa * DAU(t-1)
    DAU(t)      = sum_{s<=t} installs(s) * ret(t-s)
Reproduction number (k-factor) R = kappa * L, where L = sum_d ret(d) = expected active days per install.
Growth rate r solves Euler-Lotka: 1 = kappa * sum_{d>=1} ret(d-1) * exp(-r d).

The point: for share-on-play games, retention multiplies virality. The same kappa gives a far higher
k-factor in a daily-habit game than in a 2-day novelty.
"""
import json, os, sqlite3
import numpy as np
import pandas as pd
from scipy.optimize import brentq

OUT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(OUT)
H = 365

# Retention profiles (D1, D7, D30). Median/top-quartile from GameAnalytics benchmarks (as cited in the DB);
# "daily habit" is an assumption for Wordle-like ritual games (NYT does not publish retention).
PROFILES = {
    "median_mobile_game": (0.22, 0.04, 0.008),
    "top_quartile_casual": (0.32, 0.12, 0.04),
    "strong_casual_hit": (0.45, 0.20, 0.10),
    "daily_habit_ritual (assumption)": (0.55, 0.40, 0.28),
}


def retention_curve(d1, d7, d30, horizon=H):
    """Power law ret(d) = d1 * d^-b fitted through D7 and D30 (log-log least squares), ret(0)=1."""
    x = np.log([1, 7, 30]); y = np.log([d1, d7, d30])
    b, a = np.polyfit(x, y, 1)
    d = np.arange(horizon + 1, dtype=float)
    r = np.exp(a) * np.maximum(d, 1) ** b
    r[0] = 1.0
    return np.clip(r, 0, 1)


def simulate(ret, kappa, seed_total=1000, seed_days=7, days=90):
    installs = np.zeros(days + 1); dau = np.zeros(days + 1)
    for t in range(days + 1):
        seed = seed_total / seed_days if t < seed_days else 0
        installs[t] = seed + (kappa * dau[t - 1] if t > 0 else 0)
        dau[t] = sum(installs[s] * ret[t - s] for s in range(t + 1))
    return installs, dau


def kappa_needed(ret, target=1_000_000, seed_total=1000, days=90):
    f = lambda k: simulate(ret, k, seed_total, days=days)[1][-1] - target
    return brentq(f, 1e-4, 5.0)


def growth_rate(ret, kappa):
    # installs(t) = kappa * DAU(t-1): an install made at lag d >= 1 comes from a player active at age d-1
    g = lambda r: kappa * np.sum(ret[:-1] * np.exp(-r * np.arange(1, len(ret)))) - 1
    try:
        return brentq(g, -0.5, 3.0)
    except ValueError:
        return np.nan


def k_from_growth(r_per_day, tg_days):
    """Fixed generation interval approximation R = exp(r * Tg)."""
    return float(np.exp(r_per_day * tg_days))


def main():
    rows = []
    for name, (d1, d7, d30) in PROFILES.items():
        ret = retention_curve(d1, d7, d30)
        L90 = ret[:91].sum()
        for seed in (1_000, 10_000, 100_000):
            k = kappa_needed(ret, seed_total=seed)
            inst, dau = simulate(ret, k, seed)
            rows.append({"retention_profile": name, "D1": d1, "D7": d7, "D30": d30, "lifetime_active_days_90d": round(L90, 2),
                         "seed_installs": seed, "kappa_needed_per_active_day": round(k, 4), "k_factor_R": round(k * ret.sum(), 2),
                         "cumulative_installs_by_day90_M": round(inst.sum() / 1e6, 1),
                         "growth_rate_per_day": round(growth_rate(ret, k), 3),
                         "doubling_days": round(np.log(2) / growth_rate(ret, k), 1)})
    tab = pd.DataFrame(rows)
    tab.to_csv(os.path.join(OUT, "dau_math.csv"), index=False)

    # Observed growth rates -> k-factor ranges
    obs = [
        ("wordle", "players 90 (2021-11-01) -> 300,000 (2022-01-02)", np.log(300000 / 90) / 62, 1, 3, "share grid posted daily; generation = 1-3 days"),
        ("wordle", "players 300,000 (2022-01-02) -> ~2,000,000 (~2022-01-14)", np.log(2e6 / 3e5) / 12, 1, 3, "includes NYT Jan 3 profile (broadcast, not person-to-person)"),
        ("growagarden", "CCU ~1,000 (mid-Apr 2025) -> 5,000,000 (2025-05-18)", np.log(5e6 / 1e3) / 33, 1, 4, "includes Roblox algorithm + creator promotion"),
        ("growagarden", "CCU 5.0M (05-18) -> 21.3M (06-21)", np.log(21.3e6 / 5e6) / 34, 1, 4, "weekly update spikes"),
        ("amongus", "Twitch avg viewers 460 (Jun 2020) -> 53,000 (Aug 2020)", np.log(53000 / 460) / 61, 2, 7, "streamer-driven: broadcast + friend lobbies"),
        ("farmville", "DAU ~0 -> 11M in 63 days (linear ~1M/week)", np.nan, np.nan, np.nan, "linear, platform-fed (Facebook feed + Zynga cross-promo): not an epidemic curve"),
        ("drawsomething", "DAU 14.3M (04-02) -> 10.4M (05-02)", np.log(10.4 / 14.3) / 30, 3, 7, "post-peak decline: effective R < 1"),
        ("king", "avg DAU 15M (Q4'12) -> 124M (Q4'13)", np.log(124 / 15) / 365, 7, 14, "paid UA seeded (King F-1) => not pure k"),
    ]
    k_rows = []
    for gid, window, r, tlo, thi, note in obs:
        k_rows.append({"game_id": gid, "window": window, "growth_rate_per_day": None if np.isnan(r) else round(r, 4),
                       "doubling_days": None if (np.isnan(r) or r <= 0) else round(np.log(2) / r, 1),
                       "gen_days_low": tlo, "gen_days_high": thi,
                       "k_low": None if np.isnan(r) else round(k_from_growth(r, tlo), 2),
                       "k_high": None if np.isnan(r) else round(k_from_growth(r, thi), 2), "notes": note})
    kt = pd.DataFrame(k_rows)
    kt.to_csv(os.path.join(OUT, "k_factor_estimates.csv"), index=False)
    con = sqlite3.connect(os.path.join(ROOT, "data", "viral_games.db"))
    con.execute("DELETE FROM k_factor_estimates")
    for r in k_rows:
        con.execute("INSERT INTO k_factor_estimates VALUES (?,?,?,?,?,?,?,?,?)",
                    (r["game_id"], "growth_rate->R=exp(r*Tg)", r["window"], r["growth_rate_per_day"], r["gen_days_low"], r["gen_days_high"], r["k_low"], r["k_high"], r["notes"]))
    con.commit(); con.close()
    need = np.log(1e6 / 1e3) / 90
    print(f"Pure arithmetic: from 1,000 DAU to 1,000,000 DAU in 90 days needs r >= {need:.3f}/day (doubling every {np.log(2)/need:.1f} days) sustained.")
    print(tab.to_string(index=False))
    print(kt.to_string(index=False))


if __name__ == "__main__":
    main()
