"""Roblox deep dive: build a per-game table from the collected raw data and answer
   (A) who is on top and how old they are, (B) how new hits launch and how fast, (C) format waves,
   (D) what keeps players coming back (decay vs update cadence), (E) monetization structure,
   (F) the bar for Up-and-Coming. Writes data/roblox_games.csv and analysis/*.md tables."""
import datetime as dt, glob, json, os, re
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
OUT = os.path.join(ROOT, "analysis"); os.makedirs(OUT, exist_ok=True)
NOW = pd.Timestamp("2026-10-22", tz="UTC")
# 1M DAU expressed as peak concurrent players: DAU x minutes-per-DAU / 1440 x peak-to-average (1.8).
# 30 min -> 37.5k, 60 min -> 75k, 120 min -> 150k. Working threshold: 75k peak CCU.
CCU_1M_DAU = 75_000


def clean_name(n):
    n = re.sub(r"\[[^\]]*\]|\([^)]*\)", " ", n or "")
    n = re.sub(r"[^\w\s&'!+-]", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def load():
    meta = json.load(open(os.path.join(RAW, "roblox_meta.json")))
    votes = json.load(open(os.path.join(RAW, "roblox_votes.json")))
    charts = json.load(open(os.path.join(RAW, "chart_positions.json")))
    rows, hist = [], {}
    for f in glob.glob(os.path.join(RAW, "rowatcher", "*.json")):
        r = json.load(open(f)); uid = str(r["universeId"])
        m = meta.get(uid, {}); v = votes.get(uid, {}); g = r.get("rw_game") or {}
        h = pd.DataFrame(r.get("rw_history") or [])
        if len(h):
            h["time"] = pd.to_datetime(h["time"], utc=True); h["playing"] = pd.to_numeric(h["playing"], errors="coerce")
            h = h.sort_values("time"); hist[uid] = h
        created = pd.to_datetime(m.get("created"), utc=True) if m.get("created") else pd.NaT
        up, down = v.get("upVotes", 0), v.get("downVotes", 0)
        passes = [p for p in (r.get("gamepasses") or []) if p.get("forSale") and p.get("price")]
        prices = [p["price"] for p in passes]
        ch = r.get("rw_changes") or []
        name_changes_90d = sum(1 for c in ch if c.get("field") == "name" and pd.to_datetime(c["changedAt"], utc=True) > NOW - pd.Timedelta(days=90))
        rev = (g.get("revenueEstimate") or {}).get("expected") or {}
        peak = h["playing"].max() if len(h) else np.nan
        peak_t = h.loc[h["playing"].idxmax(), "time"] if len(h) else pd.NaT
        rows.append({
            "universe_id": uid, "name": m.get("name") or g.get("name"), "clean_name": clean_name(m.get("name") or g.get("name")),
            "creator": (m.get("creator") or {}).get("name"), "creator_type": (m.get("creator") or {}).get("type"),
            "created": created, "updated": pd.to_datetime(m.get("updated"), utc=True) if m.get("updated") else pd.NaT,
            "age_days": (NOW - created).days if pd.notna(created) else np.nan,
            "playing_now": m.get("playing"), "visits": m.get("visits"), "max_players": m.get("maxPlayers"),
            "genre": m.get("genre_l1") or m.get("genre"), "subgenre": m.get("genre_l2") or g.get("subgenre"),
            "favorites": r.get("favorites"), "likes": up, "dislikes": down, "like_ratio": up / (up + down) if up + down else np.nan,
            "n_passes": len(prices), "pass_median_price": float(np.median(prices)) if prices else np.nan, "pass_max_price": max(prices) if prices else np.nan,
            "name_changes_90d": name_changes_90d, "event_tag_now": bool(re.search(r"^\s*\[", m.get("name") or "")),
            "rw_rev_daily_usd_est": rev.get("dailyUsd"), "rw_first_seen": g.get("firstSeen"),
            "peak_ccu_since_jun": peak, "peak_time": peak_t,
            "now_over_peak": (m.get("playing") or 0) / peak if peak and peak > 0 else np.nan,
            "on_charts": ",".join(sorted({c["sort"] for c in charts.get(uid, [])})),
        })
    df = pd.DataFrame(rows)
    df["visits_per_day"] = df.visits / df.age_days.clip(lower=1)
    df["fav_per_kvisit"] = df.favorites / (df.visits / 1000).replace(0, np.nan)
    return df, hist


def launch_metrics(df, hist):
    """Games created after RoWatcher tracking began (2026-06-30) => we see their whole launch."""
    out = []
    for _, r in df[df.created >= pd.Timestamp("2026-06-25", tz="UTC")].iterrows():
        h = hist.get(r.universe_id)
        if h is None or len(h) < 5:
            continue
        d = (h.time - r.created).dt.total_seconds() / 86400
        def first(th):
            x = d[h.playing >= th]; return round(float(x.iloc[0]), 1) if len(x) else np.nan
        pk = h.playing.max(); tpk = float(d[h.playing.idxmax()])
        # growth rate between 1k and peak (log-linear on daily maxima)
        dd = h.assign(day=d.round()).groupby("day").playing.max()
        rise = dd[(dd >= 1000) & (dd.index <= tpk + 0.5)]
        r_day = np.polyfit(rise.index.values, np.log(rise.values), 1)[0] if len(rise) >= 3 else np.nan
        out.append({"name": r["name"], "created": r.created.date(), "peak_ccu": int(pk), "days_to_peak": round(tpk, 1),
                    "days_to_1k": first(1e3), "days_to_10k": first(1e4), "days_to_100k": first(1e5), "days_to_1M": first(1e6),
                    "growth_per_day_1k_to_peak": r_day, "doubling_days": np.log(2) / r_day if r_day and r_day > 0 else np.nan,
                    "now": r.playing_now, "now_over_peak": r.playing_now / pk if pk else np.nan})
    o = pd.DataFrame(out)
    return o.sort_values("peak_ccu", ascending=False) if len(o) else o


WAVE_TOKENS = ["steal", "egg", "brainrot", "grow", "garden", "fish", "forest", "99 nights", "obby", "tycoon", "simulator", "tower defense",
               "dress", "rng", "anime", "pet", "dig", "plants", "break", "survive", "escape", "hide", "murder", "rivals", "doors", "rails", "blox"]


def waves(df):
    rows = []
    low = df.clean_name.str.lower()
    for t in WAVE_TOKENS:
        sub = df[low.str.contains(r"\b" + re.escape(t) + r"\b", regex=True)].sort_values("created")
        if len(sub) < 3:
            continue
        leader = sub.loc[sub.playing_now.idxmax()]
        first = sub.iloc[0]
        rows.append({"token": t, "games": len(sub), "first": f"{first['name']} ({first.created.date() if pd.notna(first.created) else '?'})",
                     "leader_now": f"{leader['name']} ({leader.created.date() if pd.notna(leader.created) else '?'})",
                     "leader_is_first": leader.universe_id == first.universe_id, "total_playing": int(sub.playing_now.sum()),
                     "created_last_120d": int((sub.age_days <= 120).sum())})
    o = pd.DataFrame(rows)
    return o.sort_values("total_playing", ascending=False) if len(o) else o


def md(df, cols=None, n=None, fmt=None):
    d = df[cols] if cols else df
    if n: d = d.head(n)
    lines = ["| " + " | ".join(d.columns) + " |", "|" + "---|" * len(d.columns)]
    for _, r in d.iterrows():
        cells = []
        for c in d.columns:
            v = r[c]
            if isinstance(v, float):
                cells.append("" if np.isnan(v) else (f"{v:,.0f}" if abs(v) >= 100 else f"{v:.2f}"))
            elif isinstance(v, (int, np.integer)):
                cells.append(f"{v:,}")
            else:
                cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    df, hist = load()
    df.to_csv(os.path.join(ROOT, "data", "roblox_games.csv"), index=False)
    top = df.sort_values("playing_now", ascending=False)
    L = [f"# Roblox deep dive: tables (n={len(df)} games, snapshot {NOW.date()})", ""]
    t100 = top.head(100)
    L += ["## A. Who is on top", "",
          f"- Top 100 by live players: median age {t100.age_days.median()/365:.1f} years; created in the last 120 days: {(t100.age_days<=120).sum()}; last 365 days: {(t100.age_days<=365).sum()}; older than 3 years: {(t100.age_days>3*365).sum()}.",
          f"- Games at or above ~1M-DAU scale now (>= {CCU_1M_DAU:,} concurrent): {(df.playing_now>=CCU_1M_DAU).sum()}.", "",
          md(top.assign(created=top.created.dt.date), ["name", "playing_now", "created", "genre", "max_players", "like_ratio", "n_passes", "name_changes_90d"], 30), ""]
    g = t100.groupby("genre").agg(games=("name", "size"), playing=("playing_now", "sum")).sort_values("playing", ascending=False)
    L += ["Genre mix of the top 100:", "", md(g.reset_index()), ""]
    lm = launch_metrics(df, hist)
    lm.to_csv(os.path.join(ROOT, "data", "roblox_launches.csv"), index=False)
    L += ["## B. Launch trajectories (games created since late June 2026, full history observed)", "", md(lm, n=40), ""]
    wv = waves(df); wv.to_csv(os.path.join(ROOT, "data", "roblox_waves.csv"), index=False)
    L += ["## C. Format waves (title keyword clusters)", "", md(wv), ""]
    est = df[(df.age_days > 180) & df.peak_ccu_since_jun.notna() & (df.peak_ccu_since_jun >= 5000)]
    L += ["## D. Holding players: games older than 6 months with >= 5k peak since June", "",
          f"- Correlation (Spearman) of 'now / peak since June' with name changes in last 90 days: {est.now_over_peak.corr(est.name_changes_90d, method='spearman'):.2f} (n={len(est)}).",
          f"- Median now/peak: with >= 3 name changes in 90 days {est[est.name_changes_90d>=3].now_over_peak.median():.2f} (n={(est.name_changes_90d>=3).sum()}); with 0-2: {est[est.name_changes_90d<3].now_over_peak.median():.2f} (n={(est.name_changes_90d<3).sum()}).", ""]
    tiers = pd.cut(df.playing_now, [0, 1e3, 1e4, 1e5, 1e7], labels=["<1k", "1k-10k", "10k-100k", "100k+"])
    mon = df.groupby(tiers, observed=True).agg(games=("name", "size"), median_passes=("n_passes", "median"), median_pass_price=("pass_median_price", "median"),
                                              median_max_pass=("pass_max_price", "median"), median_like_ratio=("like_ratio", "median"),
                                              median_max_players=("max_players", "median"), median_rw_rev_per_ccu=("rw_rev_daily_usd_est", lambda s: np.nan))
    df["rw_rev_per_ccu_day"] = df.rw_rev_daily_usd_est / df.playing_now.replace(0, np.nan)
    mon["median_rw_rev_usd_per_ccu_day (RoWatcher est.)"] = df.groupby(tiers, observed=True).rw_rev_per_ccu_day.median()
    L += ["## E. Monetization and social structure by size tier", "", md(mon.drop(columns=["median_rw_rev_per_ccu"]).reset_index().rename(columns={"playing_now": "tier"})), ""]
    uc = df[df.on_charts.str.contains("up-and-coming")]
    L += ["## F. The bar for Up-and-Coming today", "",
          f"- {len(uc)} games; median age {uc.age_days.median():.0f} days (max {uc.age_days.max():.0f}); median live players {uc.playing_now.median():,.0f} (min {uc.playing_now.min():,.0f}); median like ratio {uc.like_ratio.median():.2f}.", "",
          md(uc.sort_values("playing_now", ascending=False).assign(created=uc.created.dt.date), ["name", "created", "age_days", "playing_now", "like_ratio", "genre"], 25), ""]
    open(os.path.join(OUT, "tables.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L)[:6000])
