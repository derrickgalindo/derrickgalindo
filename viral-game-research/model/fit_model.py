"""Viral-potential scoring model with held-out backtests (see PREREGISTRATION.md).

Outputs model/backtest_results.json and model/backtest_report.md.
"""
import json, os, sqlite3, warnings
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from scipy.stats import rankdata

warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "viral_games.db")
OUT = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(7)

CONVENTIONAL = ["one_input", "short_session", "fast_ttff", "free_to_play", "share_in_product", "daily_or_scarcity", "friends_graph", "invite_needed"]
CONTEXT = ["has_audience", "ip_licensed", "paid_ua", "new_channel", "novel"]
NOVEL = ["rules_preknown", "spectator_high", "failure_comedy", "emergent_output", "artifact_curiosity"]


def load(include_census=False):
    con = sqlite3.connect(DB)
    df = pd.read_sql("""SELECT g.*, f.*, t.peak_sudoku_units, t.early_momentum
                        FROM games g JOIN features f USING(game_id) LEFT JOIN trends_metrics t USING(game_id)""", con)
    df = df.loc[:, ~df.columns.duplicated()]
    con.close()
    df["hit"] = (df.outcome_tier >= 2).astype(int)
    df["year"] = pd.to_datetime(df.first_release, errors="coerce").dt.year
    df["short_session"] = (df.session_min <= 5).astype(int)
    df["fast_ttff"] = (df.ttff_sec <= 10).astype(int)
    df["share_in_product"] = (df.share_artifact >= 2).astype(int)
    df["daily_or_scarcity"] = ((df.daily_sync == 1) | (df.scarcity == 1)).astype(int)
    df["friends_graph"] = (df.social_graph >= 2).astype(int)
    df["has_audience"] = (df.creator_audience >= 1).astype(int)
    df["new_channel"] = (df.platform_newness >= 2).astype(int)
    df["novel"] = (df.novelty >= 1).astype(int)
    df["spectator_high"] = (df.spectator >= 2).astype(int)
    df = df[df.platform != "telegram"]
    if not include_census:
        df = df[df.cohort != "wordle_census"]
    return df.reset_index(drop=True)


def fit(train, feats, C=0.5):
    sc = StandardScaler().fit(train[feats].astype(float))
    m = LogisticRegression(C=C, max_iter=2000, class_weight="balanced").fit(sc.transform(train[feats].astype(float)), train.hit)
    return lambda d: m.predict_proba(sc.transform(d[feats].astype(float)))[:, 1], dict(zip(feats, m.coef_[0]))


def checklist(train, feats):
    """Unit-weight score: +1 for each feature whose train-set hit rate is higher when present."""
    signs = {}
    for f in feats:
        on, off = train[train[f] == 1].hit.mean(), train[train[f] == 0].hit.mean()
        signs[f] = 0 if (np.isnan(on) or np.isnan(off)) else np.sign(on - off)
    return lambda d: sum(signs[f] * d[f].astype(float) for f in feats), signs


def fast_auc(y, s):
    """Mann-Whitney AUC (ties count half)."""
    r = rankdata(s)
    n1 = y.sum(); n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def boot_auc(y, s, n=2000):
    y, s = np.asarray(y), np.asarray(s)
    if len(set(y)) < 2:
        return np.nan, (np.nan, np.nan)
    a = roc_auc_score(y, s)
    bs = []
    for _ in range(n):
        i = RNG.integers(0, len(y), len(y))
        if len(set(y[i])) == 2:
            bs.append(fast_auc(y[i], s[i]))
    return a, (float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5)))


def boot_delta(y, s_base, s_new, n=2000):
    y, a, b = np.asarray(y), np.asarray(s_base), np.asarray(s_new)
    d = []
    for _ in range(n):
        i = RNG.integers(0, len(y), len(y))
        if len(set(y[i])) == 2:
            d.append(fast_auc(y[i], b[i]) - fast_auc(y[i], a[i]))
    return float(np.mean(d)), (float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5)))


def logo_scores(df, feats, kind="logit"):
    out = pd.Series(np.nan, index=df.index)
    for c in df.cohort.unique():
        tr, te = df[df.cohort != c], df[df.cohort == c]
        if tr.hit.nunique() < 2:
            continue
        f = fit(tr, feats)[0] if kind == "logit" else checklist(tr, feats)[0]
        out[te.index] = f(te)
    return out


def within_cohort_pairs(df, score):
    wins = ties = n = 0
    for c, g in df.groupby("cohort"):
        hits, non = g[g.hit == 1], g[g.hit == 0]
        for _, h in hits.iterrows():
            for _, o in non.iterrows():
                n += 1
                if score[h.name] > score[o.name]:
                    wins += 1
                elif score[h.name] == score[o.name]:
                    ties += 1
    return {"pairs": n, "hit_ranked_higher": wins, "ties": ties, "accuracy": (wins + 0.5 * ties) / n if n else np.nan}


def identical_feature_pairs(df, feats):
    """Clone paradox: hit/non-hit pairs in the same cohort with IDENTICAL conventional features."""
    rows = []
    for c, g in df.groupby("cohort"):
        for _, h in g[g.hit == 1].iterrows():
            for _, o in g[g.hit == 0].iterrows():
                if all(h[f] == o[f] for f in feats):
                    rows.append((c, h.game_id, o.game_id))
    return rows


def run(include_census=False):
    df = load(include_census)
    res = {"n_games": int(len(df)), "n_hits": int(df.hit.sum()), "include_census": include_census}
    train, test = df[df.year < 2016], df[df.year >= 2016]
    res["split_A"] = {"n_train": int(len(train)), "train_hits": int(train.hit.sum()), "n_test": int(len(test)), "test_hits": int(test.hit.sum())}
    models = {
        "conventional": CONVENTIONAL,
        "conventional+context": CONVENTIONAL + CONTEXT,
        "context_only": CONTEXT,
        "full(conv+context+novel)": CONVENTIONAL + CONTEXT + NOVEL,
    }
    scores_A, scores_B = {}, {}
    for name, feats in models.items():
        f, coefs = fit(train, feats)
        s = f(test)
        auc, ci = boot_auc(test.hit, s)
        cl, signs = checklist(train, feats)
        auc_cl, ci_cl = boot_auc(test.hit, cl(test))
        sB = logo_scores(df, feats)
        ok = sB.notna()
        aucB, ciB = boot_auc(df.hit[ok], sB[ok])
        scores_A[name], scores_B[name] = s, sB
        res[name] = {"A_auc": auc, "A_ci": ci, "A_checklist_auc": auc_cl, "A_checklist_ci": ci_cl, "B_logo_auc": aucB, "B_ci": ciB,
                     "C_within_cohort": within_cohort_pairs(df[ok], sB), "coefs_trained_on_A": {k: round(v, 3) for k, v in coefs.items()},
                     "checklist_signs": {k: int(v) for k, v in signs.items()},
                     "verdict": "works" if (ci[0] > 0.5 and aucB > 0.6) else "fails pre-registered bar"}
    # failure analysis for the conventional+context model on split A
    s = pd.Series(scores_A["conventional+context"], index=test.index)
    t = test.assign(score=s.round(3))[["game_id", "name", "year", "cohort", "outcome_tier", "hit", "score"]]
    thr = s.median()
    res["A_false_positives"] = t[(t.hit == 0) & (t.score >= thr)].sort_values("score", ascending=False).to_dict("records")
    res["A_false_negatives"] = t[(t.hit == 1) & (t.score < thr)].sort_values("score").to_dict("records")
    res["A_ranked_test"] = t.sort_values("score", ascending=False).to_dict("records")
    sB = scores_B["conventional+context"]
    tb = df.assign(score=sB.round(3))[["game_id", "name", "cohort", "hit", "score"]]
    res["B_worst_misses"] = {
        "hits_scored_lowest": tb[tb.hit == 1].nsmallest(8, "score").to_dict("records"),
        "non_hits_scored_highest": tb[tb.hit == 0].nlargest(8, "score").to_dict("records")}
    res["clone_paradox_identical_conventional_features"] = identical_feature_pairs(df, CONVENTIONAL)
    # novel signals
    nov = {}
    base_feats = CONVENTIONAL
    fbase = fit(train, base_feats)[0](test)
    sbaseB = logo_scores(df, base_feats)
    for n in NOVEL:
        a, ci = boot_auc(test.hit, test[n])
        fnew = fit(train, base_feats + [n])[0](test)
        dA = boot_delta(test.hit, fbase, fnew)
        snewB = logo_scores(df, base_feats + [n])
        ok = sbaseB.notna() & snewB.notna()
        dB = roc_auc_score(df.hit[ok], snewB[ok]) - roc_auc_score(df.hit[ok], sbaseB[ok])
        rate_on = df[df[n] == 1].hit.mean(); rate_off = df[df[n] == 0].hit.mean()
        nov[n] = {"A_univariate_auc": a, "A_ci": ci, "A_delta_auc_vs_conventional": dA, "B_delta_auc": dB,
                  "hit_rate_with": rate_on, "hit_rate_without": rate_off, "n_with": int((df[n] == 1).sum()),
                  "holds": bool(ci[0] > 0.5 and dA[0] > 0 and dB > 0)}
    # N6: early momentum (trends, absolute-threshold based) -- only games with trends data
    em = df.dropna(subset=["early_momentum"])
    emA = em[em.year >= 2016]
    a, ci = boot_auc(emA.hit, emA.early_momentum) if emA.hit.nunique() == 2 else (np.nan, (np.nan, np.nan))
    aall, ciall = boot_auc(em.hit, em.early_momentum) if em.hit.nunique() == 2 else (np.nan, (np.nan, np.nan))
    nov["early_momentum"] = {"n_with_trends": int(len(em)), "A_test_n": int(len(emA)), "A_univariate_auc": a, "A_ci": ci,
                             "all_games_auc": aall, "all_ci": ciall, "holds": bool(not np.isnan(a) and ci[0] > 0.5)}
    res["novel_signals"] = nov
    return res, df


def fmt(x):
    return "n/a" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.2f}"


def report(res, res_c):
    L = ["# Backtest report (generated by model/fit_model.py)", "",
         f"Games in main model: {res['n_games']} ({res['n_hits']} hits). Split A: train {res['split_A']['n_train']} "
         f"({res['split_A']['train_hits']} hits, released before 2016), test {res['split_A']['n_test']} ({res['split_A']['test_hits']} hits).", "",
         "| Model | A: held-out AUC [95% CI] | A: unit-weight checklist AUC | B: leave-one-cohort-out AUC | C: hit beats its own clones/contemporaries | Verdict |",
         "|---|---|---|---|---|---|"]
    for name in ["conventional", "context_only", "conventional+context", "full(conv+context+novel)"]:
        r = res[name]
        c = r["C_within_cohort"]
        L.append(f"| {name} | {fmt(r['A_auc'])} [{fmt(r['A_ci'][0])}-{fmt(r['A_ci'][1])}] | {fmt(r['A_checklist_auc'])} | "
                 f"{fmt(r['B_logo_auc'])} [{fmt(r['B_ci'][0])}-{fmt(r['B_ci'][1])}] | {c['hit_ranked_higher']}/{c['pairs']} ({fmt(c['accuracy'])}) | {r['verdict']} |")
    L += ["", "## Coefficients (standardized, trained on pre-2016 games), conventional+context", ""]
    for k, v in sorted(res["conventional+context"]["coefs_trained_on_A"].items(), key=lambda kv: -abs(kv[1])):
        L.append(f"- `{k}`: {v:+.2f}")
    L += ["", "## Where it fails (split A, conventional+context; threshold = median score)", "", "False positives (scored high, were not hits):"]
    for r in res["A_false_positives"]:
        L.append(f"- {r['name']} ({r['year']}, {r['cohort']}): score {r['score']}")
    L.append("\nFalse negatives (hits it scored low):")
    for r in res["A_false_negatives"]:
        L.append(f"- {r['name']} ({r['year']}, {r['cohort']}): score {r['score']}")
    L += ["", "## Clone paradox", "",
          f"Hit vs non-hit pairs in the same cohort with *identical* conventional features: {len(res['clone_paradox_identical_conventional_features'])}", ""]
    for c, h, o in res["clone_paradox_identical_conventional_features"][:40]:
        L.append(f"- {c}: **{h}** (hit) = {o} (not a hit)")
    L += ["", "## Pre-registered novel signals", "", "| Signal | n with | hit rate with / without | A: univariate AUC [CI] | A: ΔAUC vs conventional [CI] | B: ΔAUC | Holds? |", "|---|---|---|---|---|---|---|"]
    for n, r in res["novel_signals"].items():
        if n == "early_momentum":
            continue
        L.append(f"| {n} | {r['n_with']} | {fmt(r['hit_rate_with'])} / {fmt(r['hit_rate_without'])} | {fmt(r['A_univariate_auc'])} [{fmt(r['A_ci'][0])}-{fmt(r['A_ci'][1])}] | "
                 f"{r['A_delta_auc_vs_conventional'][0]:+.3f} [{r['A_delta_auc_vs_conventional'][1][0]:+.3f}, {r['A_delta_auc_vs_conventional'][1][1]:+.3f}] | {r['B_delta_auc']:+.3f} | {'yes' if r['holds'] else 'no'} |")
    em = res["novel_signals"]["early_momentum"]
    L.append(f"\nN6 early momentum (Trends, absolute threshold): {em['n_with_trends']} games with data; held-out (2016+) n={em['A_test_n']}, "
             f"AUC {fmt(em['A_univariate_auc'])} [{fmt(em['A_ci'][0])}-{fmt(em['A_ci'][1])}]; all games AUC {fmt(em['all_games_auc'])} "
             f"[{fmt(em['all_ci'][0])}-{fmt(em['all_ci'][1])}]. Holds: {'yes' if em['holds'] else 'no'}.")
    if res_c:
        r = res_c["conventional+context"]
        L += ["", "## Robustness: adding the census Wordle-likes (template-coded clones)", "",
              f"n={res_c['n_games']} ({res_c['n_hits']} hits). conventional+context: A AUC {fmt(r['A_auc'])} [{fmt(r['A_ci'][0])}-{fmt(r['A_ci'][1])}], "
              f"B AUC {fmt(r['B_logo_auc'])}; within-cohort {r['C_within_cohort']['hit_ranked_higher']}/{r['C_within_cohort']['pairs']}."]
    open(os.path.join(OUT, "backtest_report.md"), "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    res, df = run(False)
    try:
        res_c, _ = run(True)
    except Exception as e:
        res_c = None
        print("census robustness skipped:", e)
    json.dump({"main": res, "with_census": res_c}, open(os.path.join(OUT, "backtest_results.json"), "w"), indent=1, default=float)
    report(res, res_c)
    print(open(os.path.join(OUT, "backtest_report.md")).read())
