"""Build data/viral_games.db from the coded data modules, raw filings-derived facts, and raw time series."""
import csv, json, math, os, sqlite3, sys
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_sources import SOURCES
from data_games import GAMES, FEATURES, BREAKOUTS, CLONE_OF
from data_business import EXTRA_SOURCES, ACQUISITIONS, BENCHMARKS
import trends_metrics as tm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "viral_games.db")

FACTS = [
    # game_id, field, value, unit, as_of, source_id, confidence, quote
    ("wordle", "daily_players", "90", "players", "2021-11-01", "wordle_players_90_300k", "high", "On Nov. 1, 90 people played"),
    ("wordle", "daily_players", "300000", "players", "2022-01-02", "wordle_players_90_300k", "high", "more than 300,000 people played"),
    ("wordle", "daily_players", "2000000", "players", "2022-01-mid", "wordle_2m_jan", "medium", "nearly two million users"),
    ("wordle", "share_button_shipped", "2021-12-16T14:54Z", "timestamp", "2021-12-16", "wardle_tweet_share", "high", "Added a share button to Wordle that generates a spoiler-free emoji grid... Shoutout to @irihapeta for inventing"),
    ("wordle", "acquisition_price", "low seven figures", "USD", "2022-01-31", "wordle_nyt_lowseven", "high", "price in the low seven figures"),
    ("wordle", "new_users_to_nyt", "tens of millions", "users", "2022-Q1", "nyt_q1_2022_pr", "high", "Wordle brought an unprecedented tens of millions of new users to The Times"),
    ("flappybird", "reviews_may25_oct31", "13", "reviews", "2013-10-31", "ibt_flappy_timeline", "medium", None),
    ("flappybird", "us_game_chart_entry", "1368", "rank", "2013-11", "ibt_flappy_timeline", "medium", None),
    ("flappybird", "first_tweet", "2013-11-04", "date", "2013-11-04", "rs_birdman", "high", "the first Twitter mention came on November 4th"),
    ("flappybird", "us_top10", "2014-01-10", "date", "2014-01-10", "ibt_flappy_timeline", "medium", None),
    ("flappybird", "us_number_one", "2014-01-17", "date", "2014-01-17", "rs_birdman", "high", None),
    ("flappybird", "pewdiepie_video", "2014-01-27", "date", "2014-01-27", "kym_pewdiepie_flappy", "medium", None),
    ("flappybird", "ad_revenue_per_day", "50000", "USD/day", "2014-02", "rs_birdman", "low", "estimated"),
    ("flappybird", "downloads", "50000000", "downloads", "2014-02", "rs_birdman", "medium", None),
    ("farmville", "dau", "11000000", "DAU", "2009-08 (week 9)", "zynga_farmville_11m", "medium", None),
    ("farmville", "dau_peak", "34500000", "DAU", "2010-03", "zynga_farmville_11m", "low", "Wikipedia-reported peak"),
    ("drawsomething", "dau", "14300000", "DAU (FB-connected)", "2012-04-02", "mcv_drawsomething_decline", "medium", None),
    ("drawsomething", "dau", "10400000", "DAU (FB-connected)", "2012-05-02", "mcv_drawsomething_decline", "medium", None),
    ("drawsomething", "acquisition_price", "183.1", "USD M", "2012-03-21", "zynga_10q_2012q1", "high", None),
    ("drawsomething", "impairment", "95.5", "USD M", "2012-09-30", "zynga_10q_2012q3", "high", None),
    ("wordswithfriends", "acquisition_price", "53.3", "USD M", "2010-11", "zynga_s1", "high", None),
    ("wordswithfriends", "dau_after_acq", "doubled within ~120 days", None, "2011", "zynga_s1", "high", None),
    ("candycrush", "king_avg_dau", "7,11,12,15,36,76,109,124", "M DAU by quarter Q1'12-Q4'13", "2013-Q4", "king_f1", "high", None),
    ("candycrush", "king_gross_bookings", "29,38,43,71,219,481,648,632", "USD M by quarter Q1'12-Q4'13", "2013-Q4", "king_f1", "high", None),
    ("candycrush", "share_of_bookings", "78", "%", "2013-Q4", "king_f1", "high", None),
    ("amongus", "ccu", "1500000", "concurrent", "2020-09-05", "ggrecon_amongus", "medium", None),
    ("amongus", "twitch_avg_viewers", "460 (Jun 2020) -> 53000 (Aug 2020)", "viewers", "2020-08", "ggrecon_amongus", "medium", None),
    ("hqtrivia", "ccu", "2380000", "concurrent", "2018-03", "tc_hq_decline", "high", None),
    ("growagarden", "ccu", "1000", "concurrent", "2025-04", "wiki_grow_a_garden", "medium", "Splitting Point bought a share at ~1,000 CCU (Madsen: ~500)"),
    ("growagarden", "ccu", "5000000", "concurrent", "2025-05-18", "wiki_grow_a_garden", "medium", None),
    ("growagarden", "ccu", "21300000", "concurrent", "2025-06-21", "wiki_grow_a_garden", "medium", None),
    ("growagarden", "ccu", "22300000", "concurrent", "2025-08-23", "gamesbeat_jandel", "high", None),
    ("growagarden", "dau_peak", "60000000", "DAU", "2025", "gamesbeat_jandel", "medium", "around 60 million peak, I think"),
    ("stealabrainrot", "ccu", "25400000", "concurrent", "2025-10", "pgbiz_brainrot_25m", "medium", None),
    ("stealabrainrot", "ccu_decline", "-99.2%", "vs peak", "2026", "rowatcher_brainrot_decline", "low", None),
    ("triviacrack", "us_number_one_days", "66", "days", "2014-11..2015-01", "bbc_triviacrack", "medium", None),
    ("crossyroad", "downloads_90d", "50000000", "downloads", "2015-02", "cultofmac_crossy", "medium", None),
    ("hamsterkombat", "users_joined", "300000000", "users (company claim)", "2024-09", "forklog_hamster", "low", None),
    ("hamsterkombat", "mau_after_airdrop", "41000000", "MAU", "2024-10", "forklog_hamster", "medium", None),
    ("wizardsunite", "first_month_spend", "12000000", "USD (est.)", "2019-07", "sensortower_hpwu", "medium", None),
]

BASE_RATES_STATIC = [
    ("supercell_launch", "Supercell games that entered development/beta (as of Feb 2023)", 35, "launched globally and kept", 5, 5 / 35,
     "Paananen: '30+ killed, 5 hits' => k/n with n=35 (lower bound on n)", "gwo_supercell_killed"),
]


def parse(block, n):
    rows = []
    for line in block.strip().splitlines():
        parts = line.split("|")
        assert len(parts) == n, (len(parts), n, line[:60])
        rows.append([None if p == "" else p for p in parts])
    return rows


def num(x):
    if x is None:
        return None
    try:
        return float(x)
    except ValueError:
        return x


def census_rows():
    """Wordle-likes from the census, template-coded with Wordle's mechanics (they are reimplementations)."""
    path = os.path.join(ROOT, "data", "raw", "wordle_census_trends.csv")
    anchor = os.path.join(ROOT, "data", "raw", "wordle_census_trends.csv.anchor.csv")
    if not os.path.exists(path):
        return [], [], {}
    df = pd.read_csv(path).drop_duplicates("name")
    nerdle_vs_wordle = pd.read_csv(anchor)["peak"].iloc[0] if os.path.exists(anchor) else float("nan")
    census = json.load(open(os.path.join(ROOT, "data", "raw", "wordles_of_the_world_parsed.json")))
    by_name = {g["name"].strip(): g for g in census}
    games, feats = [], []
    stats = {"n": 0, "ge_quarter_nerdle": 0, "ge_nerdle": 0, "nonzero": 0, "nerdle_vs_wordle": nerdle_vs_wordle}
    known = {"Lewdle", "Dordle", "Quordle", "Octordle", "Absurdle", "Heardle", "Nerdle", "Semantle"}
    for _, r in df.iterrows():
        nm = str(r["name"])
        g = by_name.get(nm, {})
        stats["n"] += 1
        stats["nonzero"] += int(r["weeks_nonzero"] > 0)
        stats["ge_quarter_nerdle"] += int(r["peak_vs_nerdle"] >= 0.25)
        stats["ge_nerdle"] += int(r["peak_vs_nerdle"] >= 1.0)
        if nm in known:
            continue  # already hand-coded
        gid = "wc_" + "".join(ch for ch in nm.lower() if ch.isalnum())[:30]
        tier = 1 if r["peak_vs_nerdle"] >= 0.25 else 0
        games.append((gid, nm, None, "solo", "web", g.get("date"), None, "daily_web", "wordle_census", "clone", "wordle", tier,
                       f"census; Trends peak = {r['peak_vs_nerdle']:.2f} x Nerdle's peak (tier1 if >= 0.25)", None, None, "low"))
        feats.append((gid, 3, 10, 1, 1, 2, 1, 0, 1, 1, 0, 0, 0, 0, 1, "ads", 0, 0, 0, 0, 0))
    return games, feats, stats


def roblox_base_rates():
    path = os.path.join(ROOT, "data", "raw", "roblox_census.csv")
    if not os.path.exists(path):
        return []
    df = pd.read_csv(path).drop_duplicates("universe_id")
    real = df[(df.is_default == 0) & (df.created != df.updated)]
    out = []
    for label, sub in (("all universes", df), ("non-default, updated after creation ('real attempts')", real)):
        for thr in (1_000, 100_000, 1_000_000, 100_000_000):
            k = int((sub.visits >= thr).sum())
            out.append((f"roblox_{'all' if label.startswith('all') else 'real'}_{thr}", f"Roblox experiences created Dec 2023-Apr 2025: {label}",
                        len(sub), f"lifetime visits >= {thr:,}", k, k / len(sub) if len(sub) else None,
                        "uniform random sample of universe IDs 5.4e9-7.6e9 via games.roblox.com", "roblox_games_api"))
    return out


def main():
    if os.path.exists(DB):
        os.remove(DB)
    con = sqlite3.connect(DB)
    con.executescript(open(os.path.join(ROOT, "data", "schema.sql")).read())
    con.execute("PRAGMA foreign_keys = OFF")  # load in any order; integrity checked at the end
    con.executemany("INSERT INTO sources VALUES (?,?,?,?,?,?,?)", SOURCES + EXTRA_SOURCES)

    master = {r["game_id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data", "games_master.csv")))}
    for r in parse(GAMES, 11):
        gid = r[0]
        m = master[gid]
        con.execute("INSERT INTO games VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (gid, m["name"], r[1], r[2], m["platform"], r[3], r[4], r[5], m["cohort"], m["role"], CLONE_OF.get(gid),
                     int(r[6]), r[10], num(r[7]), num(r[8]), r[9]))
    for r in parse(FEATURES, 21):
        con.execute("INSERT INTO features VALUES (" + ",".join("?" * 21) + ")", [num(x) if i not in (0, 15) else x for i, x in enumerate(r)])
    for r in parse(BREAKOUTS, 7):
        con.execute("INSERT INTO breakouts VALUES (?,?,?,?,?,?,?)", (r[0], int(r[1]), r[2], r[3], r[4], r[5], r[6]))
    con.executemany("INSERT INTO facts (game_id, field, value, unit, as_of, source_id, confidence, quote) VALUES (?,?,?,?,?,?,?,?)", FACTS)
    con.executemany("INSERT INTO acquisitions VALUES (?,?,?,?,?,?,?,?,?,?,?)", ACQUISITIONS)
    con.executemany("INSERT INTO monetization_benchmarks VALUES (?,?,?,?,?,?,?,?)", BENCHMARKS)

    g, f, stats = census_rows()
    if g:
        con.executemany("INSERT INTO games VALUES (" + ",".join("?" * 16) + ")", g)
        con.executemany("INSERT INTO features VALUES (" + ",".join("?" * 21) + ")", f)
        con.execute("INSERT INTO base_rates VALUES (?,?,?,?,?,?,?,?)",
                    ("wordle_census_quarter_nerdle", "English Wordle-likes in 'Wordles of the World' (domain/twist/non-linguistic)", stats["n"],
                     "Trends peak >= 25% of Nerdle's peak", stats["ge_quarter_nerdle"], stats["ge_quarter_nerdle"] / stats["n"],
                     f"Google Trends 2022-2024 vs anchor 'nerdle' (Nerdle peak = {stats['nerdle_vs_wordle']:.3f} x Wordle peak)", "wordles_census,google_trends"))
        con.execute("INSERT INTO base_rates VALUES (?,?,?,?,?,?,?,?)",
                    ("wordle_census_ge_nerdle", "English Wordle-likes in census", stats["n"], "Trends peak >= Nerdle's peak", stats["ge_nerdle"],
                     stats["ge_nerdle"] / stats["n"], "as above", "wordles_census,google_trends"))
        con.execute("INSERT INTO base_rates VALUES (?,?,?,?,?,?,?,?)",
                    ("wordle_census_any_signal", "English Wordle-likes in census", stats["n"], "any measurable weekly search interest", stats["nonzero"],
                     stats["nonzero"] / stats["n"], "as above", "wordles_census,google_trends"))
    con.executemany("INSERT INTO base_rates VALUES (?,?,?,?,?,?,?,?)", BASE_RATES_STATIC + roblox_base_rates())

    # Trends
    try:
        met = tm.all_metrics()
        known = {row[0] for row in con.execute("SELECT game_id FROM games")}
        for _, r in met.iterrows():
            if r.game_id not in known:
                continue
            con.execute("INSERT INTO trends_metrics VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (r.game_id, r.term, r.topic, r.peak_date, None if pd.isna(r.peak_sudoku_units) else float(r.peak_sudoku_units),
                         None if pd.isna(r.weeks_to_peak) else int(r.weeks_to_peak),
                         *[None if pd.isna(r[c]) else float(r[c]) for c in ["early_momentum", "growth_rate_wk", "doubling_days", "half_life_weeks", "retained_share_52w"]]))
        con.executemany("INSERT OR REPLACE INTO trends_series VALUES (?,?,?,?,?)", tm.series_rows())
    except FileNotFoundError as e:
        print("trends not ready:", e)
    con.commit()
    bad = con.execute("PRAGMA foreign_key_check").fetchall()
    assert not bad, bad[:5]
    for t in ["sources", "games", "features", "breakouts", "facts", "acquisitions", "monetization_benchmarks", "base_rates", "trends_metrics", "trends_series"]:
        print(t, con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0])
    con.close()


if __name__ == "__main__":
    main()
