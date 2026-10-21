"""Collect the numbers the web report charts, from the DB and raw files, into report/web/data.json."""
import json, os, sqlite3, sys
import numpy as np, pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "model"))
import dau_math as dm
D = os.path.join(ROOT, "data", "raw", "trends", "daily")
con = sqlite3.connect(os.path.join(ROOT, "data", "viral_games.db"))
out = {}
def daily(name, geo, a=None, b=None):
    s = pd.read_csv(os.path.join(D, f"{name}.{geo}.csv"), parse_dates=["date"]).set_index("date")["value"]
    if a: s = s[a:b]
    return [[d.strftime("%Y-%m-%d"), float(v)] for d, v in s.items()]
out["wordle"] = daily("wordle_pre", "WW", "2021-11-01", "2022-01-02")
out["flappy"] = daily("flappybird", "US", "2013-11-15", "2014-02-08")
out["amongus"] = {g: daily("amongus", g) for g in ["KR", "BR", "US"]}
res = json.load(open(os.path.join(ROOT, "model", "backtest_results.json")))["main"]
out["backtest"] = [{"model": m, "A": res[m]["A_auc"], "Alo": res[m]["A_ci"][0], "Ahi": res[m]["A_ci"][1], "B": res[m]["B_logo_auc"], "Blo": res[m]["B_ci"][0], "Bhi": res[m]["B_ci"][1], "C": res[m]["C_within_cohort"]["accuracy"]}
                   for m in ["conventional", "context_only", "conventional+context", "full(conv+context+novel)"]]
ns = res["novel_signals"]
out["novel"] = [{"k": k, "with": ns[k]["hit_rate_with"], "without": ns[k]["hit_rate_without"], "auc": ns[k]["A_univariate_auc"], "lo": ns[k]["A_ci"][0], "hi": ns[k]["A_ci"][1], "n": ns[k]["n_with"]}
                for k in ["spectator_high", "failure_comedy", "emergent_output", "rules_preknown", "artifact_curiosity"]]
out["watch"] = {k: ns["watch_ratio"][k] for k in ["n", "A_test_n", "A_univariate_auc", "A_ci"]}
dec = pd.read_sql("""SELECT g.name, g.era, g.platform, f.spectator, t.retained_share_52w r FROM games g JOIN features f USING(game_id)
                     JOIN trends_metrics t USING(game_id) WHERE g.outcome_tier>=2 AND t.retained_share_52w IS NOT NULL ORDER BY r DESC""", con)
out["decay"] = dec.to_dict("records")
rows = []
for name, (d1, d7, d30) in dm.PROFILES.items():
    ret = dm.retention_curve(d1, d7, d30)
    k = dm.kappa_needed(ret, seed_total=1000)
    inst, dau = dm.simulate(ret, k, 1000)
    rows.append({"profile": name.replace(" (assumption)", ""), "d1": d1, "d7": d7, "d30": d30, "kappa": k, "installs": float(inst.sum()), "dau": [float(x) for x in dau]})
out["dau"] = rows
out["k"] = pd.read_csv(os.path.join(ROOT, "model", "k_factor_estimates.csv")).replace({np.nan: None}).to_dict("records")
out["base"] = pd.read_sql("SELECT * FROM base_rates", con).to_dict("records")
wc = pd.read_csv(os.path.join(ROOT, "data", "raw", "wordle_census_trends.csv")).drop_duplicates("name")
out["census"] = sorted([[n, float(v)] for n, v in zip(wc.name, wc.peak_vs_nerdle)], key=lambda x: -x[1])
out["concepts"] = pd.read_sql("SELECT name, platform, pitch, model_score, rank, notes FROM concepts ORDER BY rank", con).to_dict("records")
out["acq"] = pd.read_sql("SELECT * FROM acquisitions", con).replace({np.nan: None}).to_dict("records")
g = pd.read_sql("SELECT g.name, g.cohort, g.role, g.outcome_tier, g.platform, g.first_release, b.latent_days, b.ignition_type, b.influencer_timing FROM games g LEFT JOIN breakouts b USING(game_id) WHERE g.cohort!='wordle_census'", con)
out["breakouts"] = g.dropna(subset=["latent_days"]).replace({np.nan: None}).to_dict("records")
out["counts"] = {"games": int(len(g)), "hits": int((g.outcome_tier >= 2).sum()), "sources": con.execute("select count(*) from sources").fetchone()[0],
                 "census": int(len(wc)), "trends_games": con.execute("select count(*) from trends_metrics").fetchone()[0]}
json.dump(out, open(os.path.join(ROOT, "report", "web", "data.json"), "w"), default=float)
print({k: (len(v) if hasattr(v, "__len__") else v) for k, v in out.items()})
