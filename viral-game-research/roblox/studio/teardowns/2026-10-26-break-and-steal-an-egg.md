# Teardown: Break and Steal an Egg

*Oct 26 2026.*
- *Universe 10765288803, by ILGames x Eggs (Group), launched Sep 5.*
- *Data: `data/roblox_games.csv`, RoWatcher history `data/raw/rowatcher/10765288803.json`, and the Roblox game-passes API.*
- *I haven't played it. The first 60 seconds come from the game description, which says "Game inspired by steal an egg".*

**Core loop:** break eggs with a pickaxe to hatch rare animals, steal other players' animals past the guards, and place them in your base to earn cash for speed and pickaxe upgrades.

## First 60 seconds (from the description)
- A pickaxe and eggs straight away: "Break eggs to hatch rare animals".
- Then the first steal and escape: "Steal them and escape the guards".
- Then you place animals in your base, and cash starts ticking.

## Retention engine
- **Collection:** "Collect them all in the Index!"
- **Idle income:** animals in your base earn cash.
- **Upgrades:** speed and pickaxe.
- **PvP stealing:** players take from each other's bases.
- **Not visible:** trading, offline earnings or ranked play aren't stated.

## Co-play
Servers hold 7 and are always full (RoWatcher shows 100% average fill). The game is player-against-player among strangers, so friends aren't needed.

## Monetization
- **0 game passes.**
- **Revenue: about $43k/day.** That's RoWatcher's model estimate (range $22k–65k, medium confidence), and RoWatcher classifies it as "devproduct-heavy".

## Update cadence
- No title tag.
- One description edit, on Sep 29.
- Last published Oct 25.
- **Event pattern:** single-sample spikes on Sundays:
  - 536,611 on Oct 18 at 09:36 UTC (the sample before was 204k);
  - 255,444 on Oct 25 at 14:24 UTC.
  - This looks like a scheduled weekly event (my inference, not confirmed).

## Launch curve
| Milestone | Value |
|---|---|
| Reached 1k and 10k | before day 22.5 (RoWatcher's first sample was 12k) |
| Reached 100k | day 28.7 |
| Peak | 536,611 on Oct 18, day 43: a spike. Daily highs were 190–220k on Oct 13–17 |
| Now | 140k: 26% of the spike, and same-hour WoW 1.02 |
| Weekday highs | 187k (Mon Oct 19) → 126k (Fri Oct 23) |

**Where it is on the curve:** past its peak, and the weekday highs fell 33% during the week.

## What we'd steal
- **Index completion as the long goal (Hide as a Painting).** "Collect them all in the Index!" works as a frame/paint/pose index for Hide as a Painting v2, with a reward for each completed page.
- **A weekly event at a fixed time (both games).**
  - Its Sunday spikes run at 1.5–2.6× the sample before them.
  - Pick one weekly slot, Saturday or Sunday 09–14 UTC, the same window the steal/egg games spike in, and run a short event in it.
