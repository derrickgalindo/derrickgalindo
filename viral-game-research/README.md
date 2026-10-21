# Viral game research

Research to decide what to build: a casual game aimed at 1M daily players within 90 days, with no paid marketing.

**Start with [`report/REPORT.md`](report/REPORT.md)** (15-minute read).

| Deliverable | Where |
|---|---|
| Findings report with sources | `report/REPORT.md` |
| Dataset (SQLite) | `data/viral_games.db` (schema: `data/schema.sql`; CSV exports: `data/export/`) |
| Scoring model + held-out backtest | `model/fit_model.py`, `model/backtest_report.md`, `model/backtest_results.json`, `model/PREREGISTRATION.md` |
| DAU arithmetic and k-factors | `model/dau_math.py`, `model/dau_math.csv`, `model/k_factor_estimates.csv` |
| Premise tests, case studies, business model | `analysis/*.md` |
| 20 concepts, scored and ranked | `analysis/concepts.md` (top 3 with demand tests are in the report) |

## What is in the database
| Table | Contents |
|---|---|
| `games` | ~126 hand-coded games (hits, clones, predecessors, contemporaries, same-creator follow-ups), plus ~140 census Wordle-likes |
| `features` | The same variables for every game: session length, time to first fun, share artifact, daily/scarcity hooks, social graph, spectator value, monetization, channel newness and more |
| `breakouts` | How each documented hit actually broke out: latent days, ignition type, first community, influencer timing |
| `facts` | Atomic sourced facts with confidence and quotes |
| `sources` | Every source, typed `primary_filing` / `primary_creator` / `primary_data` / `secondary_*` |
| `acquisitions` | What buyers paid, what they bought, what happened next |
| `monetization_benchmarks` | Revenue per daily player, mostly derived from SEC filings |
| `base_rates` | Census-style failure rates (Wordle-likes, Flappy Bird clones, Roblox, Supercell) |
| `trends_series`, `trends_metrics` | Google Trends weekly/daily series and the curve metrics derived from them |
| `k_factor_estimates`, `concepts` | Epidemiology estimates; the 20 scored concepts |

## Reproduce
```bash
pip install pytrends pandas scikit-learn scipy requests
python3 scripts/pull_trends.py            # Google Trends (slow; resumable)
python3 scripts/pull_case_studies.py      # daily series for case studies
python3 scripts/wordle_census_trends.py   # census of Wordle-likes
python3 scripts/pull_youtube_ratio.py     # YouTube-vs-web watch ratio
python3 scripts/build_db.py               # builds data/viral_games.db
python3 model/fit_model.py && python3 model/dau_math.py
python3 analysis/premise_tests.py && python3 analysis/case_studies.py && python3 analysis/business_model.py && python3 analysis/concepts.py
python3 scripts/export_csv.py
```
Raw inputs live in `data/raw/`: SEC filings (converted to text), the Rovio annual report, Trends CSVs, the Wordle-likes census and the Roblox API sample.
The large `.htm`/`.pdf` originals are git-ignored, and every one has a URL in `sources`.
