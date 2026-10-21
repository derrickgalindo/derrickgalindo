#!/bin/bash
# Run the remaining Google Trends jobs one after another (single IP => sequential to limit 429s).
cd "$(dirname "$0")/.."
while ps -eo args | grep -q "^python3 scripts/pull_trends.py"; do sleep 30; done
python3 scripts/pull_case_studies.py > data/raw/trends/_log_daily.txt 2>&1
python3 scripts/wordle_census_trends.py > data/raw/_log_wordle_census.txt 2>&1
python3 scripts/pull_trends.py > data/raw/trends/_log3.txt 2>&1   # pick up any games that failed earlier
