# Teardown update: Throw Food For Animals

*Nov 16 2026. This builds on the [Nov 2 teardown](2026-11-02-throw-food-for-animals.md) and covers only what changed. The game went from 141k to 353k at the same hour.*
- *Universe 10766972131.*
- *Data:*
  - *`data/roblox_games.csv`;*
  - *the RoWatcher history `data/raw/rowatcher/10766972131.json`;*
  - *Roblox metadata for Nov 2 (git) and today;*
  - *the game-passes API;*
  - *the guide sites linked below.*

**Core loop (unchanged):** throw food as far as you can, collect the animals it attracts, earn from them, then buy better food and do pull-ups to throw farther into new areas.

## What's sustaining it
1. **A fixed weekly live event.**
   - Guides list an Admin Abuse event every Saturday at 9 AM ET (14:00 UTC), lasting about 30 minutes, with an update expected after it ([beatcopgame, Nov 11](https://beatcopgame.com/throw-food-animals-admin-abuse-event-guide-what-to-prepare/)).
   - That matches our two single-sample Saturday spikes: 676k on Nov 7 at 12:00 UTC and 912k on Nov 14 at 13:12 UTC, roughly 2× the samples on either side.
2. **A rarity layer.**
   - A guide dated Nov 8 lists 5 mutations (Gold → Rainbow) and 9 size tiers (Big → Infinite), "from Update 1" ([ofzenandcomputing](https://www.ofzenandcomputing.com/throw-food-for-animals-mutations-and-sizes/)).
   - Our Nov 2 teardown found no update. So this is new since then, or was invisible from outside (an inference).
3. **Engagement held up as the audience grew 4×.**

| Week ending | Average concurrent players | Visits/day | Minutes per visit (derived) |
|---|---|---|---|
| Nov 2 | 70k | 5.3M | 19.2 |
| Nov 9 | 177k | 13.7M | 18.5 |
| Nov 16 | 282k | 20.7M | 19.6 |

- The like ratio is still 0.94, and the 5-player servers are still 100% full.
- When a broader audience keeps the same session length, the recommender keeps expanding.

**What didn't change:**
- still only 2 game passes (both from Sep 30);
- description unchanged;
- no codes;
- the only title change is that the 🎃 tag was dropped.

## Launch curve now
| Measure | Value |
|---|---|
| Monday 13:00–13:35 UTC, week by week | 19k (Oct 26) → 141k (Nov 2) → 236k (Nov 9) → **353k (Nov 16)**. Growth is slowing (7.3×, 1.7×, 1.5×) but hasn't stopped |
| Peak sample | 911,888 on Sat Nov 14 at 13:12 (the event spike) |
| Next-highest sample | 478k (Sun Nov 15) |
| Now vs peak | 39% of the spike, **74% of the next-highest sample**. Day 59 |

## Monetization
- **2 passes, unchanged:** x2 Training Power 149 R$ and x2 Cash 99 R$.
- **Revenue:** RoWatcher's model now says ~$40.5k/day (range $30.4k–50.7k), up from $9.7k on Nov 2. *This is a model estimate.*

## Copies
- **Throw a Seed** (Nov 7, Fish Time Studios) is at 14.8k, with a 19.1k peak.
  - It uses the same frame: throw down a canyon, do pull-ups to throw farther, 5-player servers.
  - It adds luck zones along the throw, plants that earn money while you're offline, and "1 in a million" secrets.

## What we'd steal
- **(both) One fixed weekly event hour.** A Saturday at 14:00 UTC that players can plan around, like Night-Shift Museum's "Saturday Night Shift" (double anomalies, rare exhibit drops). Later it becomes Hide as a Painting's weekly gallery rotation.
- **(Hide as a Painting) Rarity tiers on top of the collectible, not more collectibles.** Mutations × sizes multiply a small catalog. Frames could come in Gold, Diamond and Rainbow finishes in several sizes, so a 20-frame catalog stretches into a long chase.
