#!/bin/bash
# Take a chart snapshot every 3 hours for as long as this machine is up.
cd "$(dirname "$0")/.."
while true; do python3 scripts/snapshot_charts.py >> data/charts/_log.txt 2>&1; sleep 10800; done
