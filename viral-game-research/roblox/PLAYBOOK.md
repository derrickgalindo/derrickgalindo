# Roblox hit playbook

*Deep dive, Oct 22 2026. Data: 625 Roblox experiences (everything on Roblox's discovery charts today, plus Rolimons' top 500 by live players).*
- *Official Roblox: metadata, votes, favorites and game passes from the Roblox APIs, plus Roblox's own Creator Hub docs on discovery.*
- *RoWatcher: player-count histories since June 30 2026, and revenue figures that are RoWatcher's own model estimates.*
- *Press reports on acquisitions.*
- *Raw data: `data/raw/`. Tables: `analysis/tables.md`. Code: `scripts/`.*

## How a Roblox game is made
- **Tools:** the free Roblox Studio (Windows/Mac). Code is in Luau, Roblox's typed Lua. Engineers usually use Rojo (VS Code + git).
- **What Roblox runs:** servers, matchmaking, payments, chat and voice, and every device (phone, PC, console, tablet). You pay nothing to host.
- **Money:**
  - players buy Robux and spend it on game passes (one-time) and developer products (repeatable);
  - Roblox also pays engagement-based Creator Rewards;
  - Robux convert to dollars through DevEx. Creators received 22% of all bookings in 2025;
  - from June 8 2026, spend by age-checked US adults in R15-avatar games earns a **42% higher DevEx rate** (Roblox newsroom).
- **Ownership:** 94 of today's top 100 games are owned by groups (studios or teams), not individual accounts.

## What Roblox's recommender rewards (official Creator Hub docs)
Home "Recommended For You" ranks games on:
- **play-through rate** (people who play after seeing it);
- **first-play bounce** under 60 s and 61–180 s, which counts against you;
- **play days per user** at D1, D2–7 and D8–28;
- **playtime**, capped at 60 min per user per day;
- **intentional co-play days** with friends;
- **qualified sessions**, spend days and Robux per user.

Rules that matter for strategy:
- **Only players who arrived through recommendations count.** "Roblox doesn't count the engagement, monetization, or retention of users first acquired from ads, curation, friends, search, social media, or any other source." Outside traffic only "accelerate[s] your consideration".
- **Explore, then expand.** The system tests a game on a user cohort and expands to similar cohorts if the cohort engages. New games are evaluated from the first session, and there's no penalty for a weak start.
- **Copies are demoted.** Games whose "metadata and place files closely resemble existing games" are no longer prioritized, but Roblox explicitly says to "add your own spin to existing trends".
- **A custom thumbnail is required** to get any home-page impressions.

## Findings

1. **Play is concentrated, and 1M daily players means the top 10–30.**
   - The top 10 of 7,822 tracked games hold 32% of concurrent players; the top 100 hold 60%.
   - Only 10 games are at or above ~75k concurrent right now. That's my working equivalent of 1M DAU: DAU × minutes per player / 1,440 × a 1.8 peak-to-average ratio, which spans 40k–150k for 30–120 minutes a day.
2. **New games do reach the top, fast.**
   - 37 of the top 100 were created in the last 120 days. Today's #1, Steal An Egg (Misfits Gaming), launched Jul 25 2026, hit 100k concurrent on day 19 and 1M on day 28, and peaked at 7.1M in RoWatcher's samples (~14.3M per other trackers) around day 56.
   - Old games last when they keep updating: 53 of the top 100 are more than a year old, 30 are more than three. Murder Mystery 2, from 2014, is #2.
3. **Launches follow the same shape: a wait, a jump, a peak, a fall.** Across 210 games launched since late June that reached 1k concurrent:
   - **The wait:** a median of **19 days** to reach 1,000 concurrent.
   - **The jump:** from 1k to 10k in a median of **2.6 days** (42% within 2 days). That is the recommender's "expand" step.
   - **The peak:** about **30 days** after launch.
   - **The fall:** daily play is still at 83% of peak a week later and 46% three weeks later. Games that peaked above 50k are now at a median of **15%** of that peak.
   - **Total value:** a fad-shaped hit delivers about **one month of peak-level play** over its whole run.
4. **The odds once a game reaches 1k concurrent** (optimistic, because faded games are undercounted): 65% reached 10k, 12% reached 50k, **6% reached ~1M-DAU scale (75k)**, 3% reached 100k, 1 game reached 1M. Getting to 1k is the hard part: none of 7,356 random new experiences in the earlier sample reached even 1,000 lifetime visits.
5. **Format waves are the main pattern, and the winner of a wave is usually not the first game in it.**
   - "Steal": 14 games, 11 launched in the last 120 days. Steal a Brainrot (May 2025) started it; Steal An Egg (a new object plus hatching and mutations) now leads.
   - "+1 per second" incrementals: 18 games, 12 new.
   - "Anomaly" shift-work horror: 9 games, 6 new. Sell Fries! [Anomaly] went from launch to 105k in 26 days.
   - Close copies fade: Steal Animal Egg peaked at 57k and is at 3k now.
6. **Nothing visible from outside predicts which new games keep their players.** Among 30 recent launches past their peak, like ratio, favorites, server size and game-pass count all correlate weakly with retention (|ρ| ≤ 0.18). Retention lives in the game loop and the update cadence, which only Roblox's recommender sees. That's why testing on Roblox itself beats theorizing.
7. **What the long-lived games share.**
   - A loop players repeat: rounds, collection, or progression.
   - A collection or trading economy: Murder Mystery 2's knives, Adopt Me's pets, Fisch's "400,000+ variations", Fish It's "1,000,000+ variations".
   - Rare-roll mutations, and earnings while offline.
   - Seasonal events: nearly every top game is running a Halloween event right now.
   - Server size matches the loop: tycoon and steal games run about 8 players per server, survival about 24, roleplay about 30.
8. **Money and exits.**
   - **Revenue per player:** RoWatcher's model puts revenue at about $0.3–0.5 a day per concurrent player. At 60 minutes a day that's roughly $0.01–0.02 per daily player, which agrees with the main report's $0.012 mid estimate. These are estimates, not Roblox data.
   - **Exits are active:** Bloomberg (Jul 2025) reported a buying frenzy after Roblox made ownership transfers easier in December 2024. Reports disagree on whether 7 or 15 of June 2025's top earners had been acquired. Buyers include Do Big, Voldex, Splitting Point and Embracer.
   - **Prices** are reportedly **1–12 months of in-game revenue**. Blue Lock: Rivals sold for over $3M while earning ~$5M a month, after about three months of development by a 19-year-old.

## Concepts re-scored on Roblox's terms
The rubric below is built from the evidence above. It isn't a fitted model, because finding 6 shows public metadata doesn't predict retention. Each item is scored 0–2:
- **pull:** how far the closest recent analog got;
- **crowding:** how many same-format games launched in the last 120 days (fewer scores higher);
- **retention engine:** collection, trading or progression;
- **co-play;**
- **watchability;**
- **solo build risk;**
- **moderation/policy risk.**

| Concept | Pull | Crowding | Retention engine | Co-play | Watchable | Build | Moderation | Total /14 |
|---|---|---|---|---|---|---|---|---|
| **Hide as a Painting v2:** round-based hide-by-posing with a Murder Mystery 2-style collect-and-trade economy (frames, paints, poses) and a museum that changes each event | 2 (Paint Or Seek peaked at 60k) | 1 (2 recent analogs) | 2 | 2 | 2 | 1 (~6–8 weeks) | 2 | **12** |
| **Night-Shift Museum [Anomaly]:** spot-the-anomaly shift work as a museum guard, co-op | 2 (Sell Fries! 105k) | 1 (6 new) | 0 | 1 | 2 | 2 (~2–3 weeks) | 2 | **10** |
| Daily Heist: one shared co-op escape room per day | 1 (MONOCHROME 23k) | 2 | 1 | 2 | 2 | 0 (content treadmill) | 2 | 10 |
| Steal-a-[new object] with a real twist | 2 | 0 (14 games, peaking) | 1 | 1 | 1 | 2 | 2 | 9 |
| Grow-a-[theme] live-ops | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 9 |
| Pictionary Obby | 1 (Draw Me! 6.6k) | 2 | 1 | 2 | 2 | 0 (stroke physics) | 0 (freehand drawings on a kids' platform) | 8 |
| Imposter Bot (an AI player in social deduction) | 1 | 2 | 1 | 2 | 2 | 0 | 0 (AI chat moderation) | 8 |
| "+1 per second" incremental | 2 | 0 | 0 | 0 | 1 | 2 | 2 | 7 |

**The fix for Hide as a Painting:**
- Paint Or Seek and Hide In Pixels proved the blend-in-and-hide mechanic draws players: 60k and 23k peaks.
- Both lost almost everyone (now at 5% and 27% of peak) and have weak like ratios (0.78 and 0.60).
- Version 2 copies what keeps Murder Mystery 2 alive after 12 years: short social rounds plus collecting and trading cosmetics.

## Revised plan
1. **Drop the web test.** Roblox's own analytics measure what actually gates growth there: play-through rate, bounce, D1/D7 and co-play. The group-chat share rate the web test measures doesn't drive Roblox discovery.
2. **Weeks 1–3: ship Night-Shift Museum [Anomaly] as a learning launch.** It's cheap, matches a rising wave, and is very watchable. The goal is to learn the funnel (thumbnail, play-through rate, D1) and build the museum assets you'll reuse in #3. Treat it as disposable.
3. **Weeks 3–10: build Hide as a Painting v2,** reusing the museum assets. Start the collection/trading economy from day one.
4. **Kill rules, from the launch data:**
   - The median game waits ~19 days to reach 1k concurrent. Give each launch 4–5 weeks and at least two content updates.
   - Kill it if it never passes ~1k concurrent and its Creator Analytics benchmarks sit in the bottom half of similar games.
   - Scale it up if it clears 10k.
5. **If it breaks out:** sell or take a minority partner near the peak if the curve looks fad-shaped (under ~40% of peak three weeks later). Keep it and invest in live-ops if it holds. Studios like Do Big, Splitting Point and Misfits buy at 1–12 months of revenue.

## Limits
- **Sample:** these are games that are visible today, so the climb odds are optimistic.
- **RoWatcher histories:**
  - they start on June 30 2026, so older games' launch curves aren't covered;
  - samples are roughly 4-hourly, which understates peaks (Steal An Egg: 7.1M here vs ~14.3M on other trackers);
  - its revenue figures are model estimates.
- **The 75k-concurrent ≈ 1M DAU equivalence** depends on session length.
- **The chart snapshots** (every 3 hours) run only while this cloud session is alive.
