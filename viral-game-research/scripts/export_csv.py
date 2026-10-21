"""Export every table in data/viral_games.db to data/export/<table>.csv (trends_series excluded: large)."""
import os, sqlite3
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
con = sqlite3.connect(os.path.join(ROOT, "data", "viral_games.db"))
os.makedirs(os.path.join(ROOT, "data", "export"), exist_ok=True)
for (t,) in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"):
    if t == "trends_series":
        continue
    pd.read_sql(f"SELECT * FROM {t}", con).to_csv(os.path.join(ROOT, "data", "export", f"{t}.csv"), index=False)
# one convenient wide view
pd.read_sql("""SELECT g.game_id, g.name, g.developer, g.dev_type, g.platform, g.first_release, g.breakout_date, g.era, g.cohort, g.role,
                      g.clone_of, g.outcome_tier, g.peak_dau_m, g.peak_ccu_m, g.confidence, g.outcome_basis, f.*, b.latent_days,
                      b.ignition_type, b.influencer_timing, t.peak_sudoku_units, t.peak_date, t.half_life_weeks, t.retained_share_52w
               FROM games g JOIN features f USING(game_id) LEFT JOIN breakouts b USING(game_id) LEFT JOIN trends_metrics t USING(game_id)""",
            con).loc[:, lambda d: ~d.columns.duplicated()].to_csv(os.path.join(ROOT, "data", "export", "games_wide.csv"), index=False)
print("exported")
