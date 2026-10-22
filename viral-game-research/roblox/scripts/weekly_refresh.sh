#!/bin/bash
# Weekly Roblox data refresh: snapshot the charts, re-collect the ~625-game dataset (with full player histories
# from RoWatcher, which covers each game's climb in ~4-hour steps), rebuild the tables and the playbook page,
# and write a short "what changed this week" note. Takes ~45 minutes.
set -e
cd "$(dirname "$0")/.."
D=$(date -u +%F)
python3 scripts/snapshot_charts.py
rm -rf data/raw/rowatcher
python3 scripts/collect_games.py 500 > data/raw/_collect_log.txt 2>&1
tar czf "data/raw/rowatcher_$D.tar.gz" -C data/raw rowatcher
python3 scripts/analyze.py > /dev/null
python3 scripts/page_data.py > /dev/null
python3 scripts/build_page.py > /dev/null
python3 scripts/weekly_diff.py
