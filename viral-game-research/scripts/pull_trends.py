"""Pull Google Trends (worldwide web search) series for every game in games_master.csv.

For each game we fetch two payloads over the window [launch - 180d, launch + 4y]:
  solo : the game alone (best resolution for curve shape)
  scale: [game, "sudoku"] so the game's peak can be expressed in a common unit
         ("sudoku-equivalents": sudoku is a stable, era-independent anchor search term).
         If the game peaks <= 5 against sudoku, a second rung [game, "nonogram"] is fetched;
         nonogram/sudoku ratios per era come from pull_anchor_ladder().
  (A first attempt anchored on "weather" was discarded: weather dominated and flattened every game to 0-1.)
Topic entities (Knowledge Graph mids) are used when a topic_hint matches a suggestion,
to avoid ambiguous strings like "among us". Resumable: skips files already written.
"""
import csv, json, os, random, sys, time
from datetime import date, timedelta
from pytrends.request import TrendReq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "raw", "trends")
MASTER = os.path.join(ROOT, "data", "games_master.csv")
TODAY = date(2026, 10, 14)

py = TrendReq(hl="en-US", tz=0, timeout=(10, 30), retries=0)


def call(fn, *a, **kw):
    for attempt in range(8):
        try:
            return fn(*a, **kw)
        except Exception as e:  # 429s and transient errors
            wait = 20 * (attempt + 1) + random.random() * 10
            print(f"  retry {attempt} after {e.__class__.__name__}: {str(e)[:80]} (sleep {wait:.0f}s)", flush=True)
            time.sleep(wait)
    raise RuntimeError("giving up")


def resolve_topic(query, hint):
    if not hint:
        return None, None
    sugg = call(py.suggestions, hint)
    for s in sugg:
        if s.get("title", "").lower() == hint.lower() and "game" in s.get("type", "").lower():
            return s["mid"], f'{s["title"]} ({s["type"]})'
    for s in sugg:
        if "game" in s.get("type", "").lower():
            return s["mid"], f'{s["title"]} ({s["type"]})'
    return None, None


def fetch(terms, start, end):
    py.build_payload(terms, timeframe=f"{start} {end}", geo="")
    df = py.interest_over_time()
    time.sleep(6 + random.random() * 6)
    return df


def main(only=None):
    rows = list(csv.DictReader(open(MASTER)))
    meta_path = os.path.join(OUT, "_meta.json")
    meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
    for r in rows:
        gid = r["game_id"]
        if only and gid not in only:
            continue
        launch = date.fromisoformat(r["launch"])
        start = max(date(2004, 1, 1), launch - timedelta(days=180))
        end = min(TODAY, launch + timedelta(days=4 * 365))
        if gid not in meta:
            mid, label = resolve_topic(r["trends_query"], r["topic_hint"])
            meta[gid] = {"term": mid or r["trends_query"], "topic": label, "start": str(start), "end": str(end)}
            json.dump(meta, open(meta_path, "w"), indent=1)
        term = meta[gid]["term"]
        for kind, terms in (("solo", [term]), ("scale", [term, "sudoku"])):
            path = os.path.join(OUT, f"{gid}.{kind}.csv")
            if os.path.exists(path):
                continue
            print(f"{gid} {kind} {terms} {start}..{end}", flush=True)
            df = call(fetch, terms, str(start), str(end))
            if df is None or df.empty:
                open(path, "w").write("date\n")
                continue
            df = df.drop(columns=["isPartial"], errors="ignore")
            df.columns = ["game" if c == term else c for c in df.columns]
            df.to_csv(path)
            if kind == "scale" and df["game"].max() <= 5:
                # game too small to resolve against sudoku: add a smaller anchor rung
                p2 = os.path.join(OUT, f"{gid}.scale2.csv")
                d2 = call(fetch, [term, "nonogram"], str(start), str(end)).drop(columns=["isPartial"], errors="ignore")
                d2.columns = ["game" if c == term else c for c in d2.columns]
                d2.to_csv(p2)


def pull_anchor_ladder():
    """sudoku vs nonogram, weekly, in <=5-year windows 2004-2026, to convert rung-2 values."""
    path = os.path.join(OUT, "_anchor_ladder.csv")
    if os.path.exists(path):
        return
    import pandas as pd
    frames = []
    for y0 in range(2004, 2027, 4):
        end = "2026-10-14" if y0 + 4 >= 2026 else f"{y0 + 4}-01-01"
        df = call(fetch, ["sudoku", "nonogram"], f"{y0}-01-01", end).drop(columns=["isPartial"], errors="ignore")
        df["window"] = f"{y0}"
        frames.append(df)
    pd.concat(frames).to_csv(path)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["ladder"]:
        pull_anchor_ladder()
    else:
        main(set(args) or None)
        pull_anchor_ladder()
