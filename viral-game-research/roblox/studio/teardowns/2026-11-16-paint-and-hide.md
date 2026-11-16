# Teardown: Paint and Hide! 🎨

*Nov 16 2026.*
- *Universe 10766044605, by Blocks In Sandals (Group), launched Sep 11 (day 66).*
- *Data:*
  - *`data/roblox_games.csv`;*
  - *the RoWatcher history `data/raw/rowatcher/10766044605.json`;*
  - *the Roblox game-passes API.*
- *I haven't played it. The first 60 seconds come from the description and the pass list.*
- *This is our closest live analog to Hide as a Painting. It was missing from the Nov 2 dataset; see the trend note.*

**Core loop:** hiders paint themselves to match the map and survive until the round timer runs out, while one seeker hunts them and tags them with gadgets.

## First 60 seconds
- You get a role: hider or seeker. A 19 R$ pass doubles your chance of being the seeker, so the seeker is evidently the role people want.
- As a hider, you paint yourself and pick a spot, then hold still until the timer ends.
- As the seeker, you use tag tools. The off-sale passes created at launch were Net Launcher, Slime Blaster, Ice Shooter and Confetti Cannon, and today there's a 999 R$ "All Guns Pass".

## Retention engine
- **Thin.** The description promises no collection, trading, offline progress or ranked play. The only progression that shows from outside is gadgets and faces. Those were passes; most are now off sale.
- **Engagement is middling:**
  - like ratio 0.72;
  - about 13 minutes per visit (7-day average concurrent players × 1,440 ÷ visits per day);
  - Throw Food, for comparison, gets ~20 minutes.
- **Favorites look prompted:** 1.35M favorites on 25.6M visits, or 53 per 1k visits, vs ~1 for Throw Food. Don't read favorites as love.

## Co-play
- Servers hold 12, with 78% average fill.
- The game needs other players (one seeker vs many hiders), but not friends. Matchmaking with strangers works.

## Monetization
- **3 passes on sale:**
  - 2X Seeker Chance, 19 R$ (Sep 21);
  - VIP, 79 R$ (Oct 8);
  - All Guns Pass, 999 R$ (Oct 25).
- **8 more passes are off sale:** tag gadgets and faces created on Sep 21.
- **Revenue:** RoWatcher's model estimates ~$3.2k/day (range $2.4k–4.1k) and labels it "gamepass-heavy". *This is a model estimate.*

## Update cadence
- No title tags.
- The RoWatcher change log is empty.
- Its Roblox `updated` time was 13:34 UTC today, so it's still being published.
- New passes arrived Oct 8 and Oct 25, the second one just before its peak.

## Launch curve (a true measurement: tracked from 89 players on Oct 16)
| Milestone | Value |
|---|---|
| 1k | day 37.6 (Oct 19). The median is 19 days, so it waited twice as long |
| 10k | day 45.9 (Oct 27), 8.3 days after 1k. The median is 2.6, so this was a slow expansion |
| Peak | 19,440 on Sat Oct 31 (Halloween), day 49.6 |
| Weekly highs since | 17.9k (week to Nov 9), then 13.9k (week to Nov 16) |
| Now | 10.0k on Monday at 13:35 = **51% of peak, 16 days after it**. That's about the benchmark of 46% at three weeks. It was 14.4k at the same hour on Nov 2 (0.69×) |

## Read
- The mechanic draws players without any economy behind it, which matches Paint Or Seek (60k in the playbook) and Hide In Pixels (23k).
- All of them hold weakly, and all of them have like ratios between 0.60 and 0.78.
- Nobody in this niche has built a collection or trading layer yet.

## What we'd steal
- **(Hide as a Painting) Sell the seeker chance cheaply.** A 19 R$ "2X Seeker Chance" pass shows that the hunter role is what people want. Offer a cheap "Curator" (seeker) chance pass, and keep everything else cosmetic.
- **(Hide as a Painting) Give hiders something to do besides wait.** The hider's job here is to stand still until a timer runs out, which is probably why likes are weak. Let hiders earn something mid-round, such as a "pose bonus" every 30 s while unspotted, paid in frame or paint drops that feed the trade economy.
- **(Night-Shift Museum) Gadgets as the seeker's toy box.** The seeker's toys (net launcher, slime blaster) are the watchable part. Give the guard 2–3 silly detection tools (a UV torch, a paint-sniffing dog) that later carry over as the Curator's kit in Hide as a Painting.
