#!/bin/bash
cd "$(dirname "$0")/.."
while ps -eo args | grep -q "^/bin/bash scripts/run_trends_queue.sh"; do sleep 30; done
python3 scripts/pull_youtube_ratio.py > data/raw/trends/_log_youtube.txt 2>&1
