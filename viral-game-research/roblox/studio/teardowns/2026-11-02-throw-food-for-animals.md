# Teardown: [🎃] Throw Food For Animals

*Nov 2 2026.*
- *Universe 10766972131, by Goofy Chupacabra (Group), launched Sep 18.*
- *Data:*
  - *`data/roblox_games.csv`;*
  - *RoWatcher history `data/raw/rowatcher/10766972131.json`;*
  - *the Roblox game-passes API;*
  - *Roblox metadata for Oct 26 vs today (`roblox_meta.json` in git).*
- *I haven't played it. The first 60 seconds come from the game description.*

**Core loop:** throw food as far as you can to attract animals, collect them, have them earn money, buy better food for rarer animals, and train on pull-up stands to throw farther into new areas.

## First 60 seconds (from the description)
- One verb right away: throw. The distance is the feedback.
- An animal comes to the food, and you've collected it. Money starts coming in from it.
- The two upgrade paths are visible from the start: better food in the shop, and pull-up stands that add Throw Power.

## Retention engine
- **Collection:** rarer animals live in farther areas.
- **Progression:** Throw Power, food tiers and areas you unlock.
- **Not present:** trading, offline progress (it isn't advertised) or ranked play. A French codes guide says it has no codes system yet ([gamewave.fr](https://gamewave.fr/roblox/roblox-codes-throw-food-for-animals/)).

## Co-play
- Not needed. Servers hold only **5 players**, and RoWatcher shows 100% average fill.
- It's effectively a solo game with a few people nearby.

## Monetization
- **2 game passes,** both created Sep 30, with nothing added since: x2 Training Power (149 R$) and x2 Cash (99 R$).
- **Revenue: about $9.7k/day.** That's RoWatcher's model estimate (range $7.3k–12.1k), labelled "gamepass-light".

## Update cadence
- 🎃 title tag (already there on Oct 26).
- No change to the name or description between our Oct 26 and Nov 2 Roblox pulls, and the RoWatcher change log is empty.
- Roblox publish timestamps: Oct 25 20:09 and Nov 1 14:26 UTC. What changed in those publishes is unknown.

## Launch curve
| Milestone | Value |
|---|---|
| Waiting period | daily highs of 31–54 from Oct 9 to Oct 19 (tracked from 15 players, so this is a real measurement) |
| Reached 1k | day 32.5 (Oct 21) |
| Reached 10k | day 35.2 (2.7 days after 1k, about the 2.6-day median) |
| Reached 100k | day 41.5 (1k → 100k in 9 days, doubling about every 1.4 days) |
| Peak | 163,373 on Sat Oct 31 (Halloween), day 42.7 |
| Now | 140k on Monday at 13:00 = **86% of peak**; 6.9× last Monday at the same hour |

## Why it jumped
- **No outside trigger is visible.** There was no rename, no description change and no new pass, and the take-off on Oct 20 came before the only publish we know of (Oct 25).
- **Its engagement is the best of this week's teardown games:**
  - a 0.94 like ratio (Sell Fries 0.85, DONT SPLASH 0.87);
  - about 20 minutes per visit, my estimate from average concurrent players × 1,440 ÷ visits per day (Sell Fries 16, DONT SPLASH 9);
  - full servers.
- **The shape is the recommender's "explore, then expand":** a month near zero, then cohort-by-cohort doubling.
- **The format fits a rising cluster.** "X for animals" (Climb For Animals Eggs peaked at 95k) is a collection loop, and this game puts a new verb on it (throw) with a distance hook. That suits phones and short clips.
- **Halloween weekend added the last leg.** Unlike most games, it held through Monday.
- **My verdict:** a recommender expansion earned by engagement, not an update or an outside push. The cause is not confirmed: there are no patch notes.

## What we'd steal
- **One physical verb with visible distance (Night-Shift Museum).** Make the guard's main action a single satisfying throw, such as tossing a flashlight beacon or a tracker down a dark gallery. How far it lands shows how good you're getting.
- **Collect what your action attracts (Hide as a Painting).** Throwing pulls in animals here. In Hide as a Painting, winning a round could attract a collectable frame or paint whose rarity scales with how far into the museum you hid.
- **Small servers, full servers (both).** Five-player servers that always fill look busy at low player counts. Start Night-Shift Museum at 4–6 per server.
