# How the teams behind Roblox hits work

*Oct 22 2026. Sources:*
- *our dataset (`data/top40_owner_portfolios.csv`: every public game owned by the group or user behind each of today's top 40);*
- *developer interviews and press, linked inline.*

*Individual names below come from interviews and press, and some are low-confidence. That's marked where it applies.*

## Correction: "owned by a group" doesn't mean "made by a big studio"
- 94 of the top 100 games are owned by a Roblox group. But a group is often just the legal and team wrapper for **one** game.
- Among the owners of today's top 40:
  - the median owner has **1.5 public games**;
  - 20 of 40 have exactly one;
  - for 18 of 40, the hit is the oldest public game the owner has.
- Launch teams are small:
  - **Grow a Garden:** one 16-year-old built it in days ([GamesBeat](https://gamesbeat.com/janzen-madsen-interview/)).
  - **Dress To Impress:** a teen developer ([RoWatcher](https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits)).
  - **Murder Mystery 2:** still owned by a single user account.
  - **99 Nights in the Forest:** 5 people ([Roblox DevForum](https://devforum.roblox.com/t/creator-spotlight-the-story-behind-99-nights-in-the-forest/4036940)).
- **The large studios mostly arrive after a game has traction:**
  - Splitting Point partnered on Grow a Garden at about 500 concurrent players;
  - Do Big Studios buys games outright, with optional revenue share ([IBTimes](https://www.ibtimes.com/do-big-studios-creative-force-redefining-roblox-gaming-3777585));
  - Voldex bought Brookhaven.

**The pattern:** small team, many prior attempts, then a studio's money and staff once the game works. For a solo engineer, that's good news.

## What they do, from their own accounts
1. **They make many games before the hit, and treat it as an apprenticeship.**
   - Jandel (Grow a Garden) made "30 to 40 games" before it, "five or six" of them good.
   - The 99 Nights team's earlier projects took ~6 months each; 99 Nights took 3.
   - Nosniy Games (RIVALS) has published 19 experiences ([RoWatcher](https://rowatcher.com/news/rivals-how-roblox-s-top-shooter-built-a-nearly-million-player-empire)).
2. **They start as a tiny jam.**
   - 99 Nights began as "a quick game jam, planned for about a week."
   - Its idea was a mix of trends: the "survive N days" trend, Dead Rails, and a cozy forest.
3. **They keep scope small and drop ideas fast.** 99 Nights' advice: keep scope small, iterate fast, "know when to drop an idea," playtest repeatedly, and watch people play when they don't know they're being watched.
4. **They update weekly, from launch.**
   - Splitting Point is "known for doing weekly updates in games across Roblox."
   - 99 Nights ships weekly and holds a 45-minute "Update Party" with players before each update.
   - RIVALS ships a major update about every 5 weeks.
   - Grow a Garden later added two parallel events teams, because one week wasn't enough to make each event well.
5. **They design for phones and for responsiveness.**
   - 99 Nights keeps part and instance counts low for mobile.
   - Actions show up instantly on the player's screen; the server checks them afterwards and can roll back.
6. **They put the retention engine into the core loop.**
   - Grow a Garden: plants grow while you're offline.
   - RIVALS: a ranked ladder; cosmetics are the only paid items; a season pass that returns ~5× its cost.
   - Murder Mystery 2 and Adopt Me: trading economies.
7. **They test packaging on Roblox itself.** Roblox's thumbnail personalization splits traffic across active thumbnails and shifts it toward the ones with a higher qualified play-through rate ([DevForum](https://devforum.roblox.com/t/get-your-thumbnails-ready-for-thumbnail-personalization/3226599)).
8. **They stay close to creators and community.**
   - Discord is the update channel (Steal An Egg posted its outage updates there).
   - Studios founded by creators use their audiences at launch ([Naavik](https://naavik.co/podcast/the-creator-led-studio-playbook/)).
   - Jandel has 12M TikTok followers.
   - Note that outside traffic only *speeds up* the recommender's evaluation; it doesn't count toward the ranking (PLAYBOOK.md).
9. **Heavy monetization after an acquisition causes backlash.** Do Big Studios is criticized for loot boxes, pay-to-win passes and "phantom updates." Grow a Garden's deal drew fears of pay-to-win. Monetizing cosmetics first (the RIVALS model) avoids that.

## Idea → release, step by step
| # | Step | Output | Time | Gate to the next step |
|---|---|---|---|---|
| 0 | **Apprenticeship:** ship small games | the learning game (Night-Shift Museum) | weeks 1–3 | funnel numbers in hand (play-through rate, bounce, D1) |
| 1 | **Idea:** a rising wave plus your own twist | a one-page pitch: core loop, the hook in the first 60 s, the retention engine | 1–2 days | the weekly trend note shows the wave still rising; the twist fits in one sentence |
| 2 | **Jam prototype** | a playable core loop, grey boxes, no art | ~1 week | friends play it again without being asked |
| 3 | **Unobserved playtests** | notes on where people get confused | a few days | most testers get through the first 60 seconds |
| 4 | **Vertical slice** | final first 60 seconds, runs smoothly on a cheap phone, server-authoritative | 1–2 weeks | phone frame rate OK; no exploit in the core loop |
| 5 | **Retention and money systems** | collection/rarity/trading, cosmetics, first game passes | 1–2 weeks | economy sheet balanced (no pay-to-win) |
| 6 | **Packaging** | title, icon, 3–5 thumbnails, group, Discord, 3 short clips | 2–3 days | thumbnails in the personalization test |
| 7 | **Soft launch** | Friends-only, then Public; an "Update Party"; post clips | week 0 | Roblox starts testing it on a group of players |
| 8 | **Weekly updates** | an update every week, an [UPD] tag in the title, events with countdowns | ongoing | — |
| 9 | **Read the numbers, then kill or scale** | weekly analytics review | weeks 4–5 | <1k concurrent and bottom-half benchmarks: kill it. >10k: scale it |
| 10 | **Scale or exit** | hire an events team, or bring in a partner or buyer | after 10k | the shape of the curve (PLAYBOOK.md, step 5) |

## Studios and teams to study
| Team | Game | What to learn | People (public) |
|---|---|---|---|
| **Grandma's Favourite Games** | 99 Nights in the Forest | a lean 5-person team; a 3-month build; weekly updates plus Update Parties | Cracky4 (design and art direction), ForyxeV (programming), Viridial (building and modelling), plus an artist and an animator |
| **Splitting Point** | Grow a Garden | weekly live-ops; spotting and partnering with games early; designer-led | Janzen "Jandel" Madsen (design, owner); original creator BMWLux |
| **Nosniy Games** | RIVALS | competitive depth, anti-cheat, ranked play, cosmetics-only monetization, season pass | SenseiWarrior (co-owner, lead programmer); BSlickMusic (music) |
| **Nikilis** | Murder Mystery 2 | the template for 1 vs All rounds plus a trading economy, alive for 12 years | Nikilis (owner) |
| **Forsaken Dev Team**, **VIOLENCE DISTRICT** | Forsaken, Violence District | recent 1 vs All hits, the closest family to Hide as a Painting | public names not confirmed |
| **Uplift Games** | Adopt Me! | a trading economy at scale; a 40→100-person studio built to avoid overwork and burnout | Josh Ling (co-founder, per press) |
| **BIG Games** | Pet Simulator 99 | collection, rarity and trading across a portfolio of games | not confirmed |
| **Do Big Studios** | Steal a Brainrot; partner on Grow a Garden and Steal An Egg | how a buyer values a game, and what heavy monetization costs in goodwill | SpyderSammy (Steal a Brainrot developer, Do Big executive; sources disagree on the title) |

## Expert roles → agents
The roles that recur on these teams:
- game designer / director
- Luau programmer
- builder / modeller
- artist and animator
- monetization / economy designer
- live-ops / events
- community manager
- growth (thumbnail click-through, experiments)
- analytics

| Agent | The expert it stands in for | What it does | Inputs |
|---|---|---|---|
| **Trend Scout** (already exists: weekly job) | studio scouts (Splitting Point, Do Big) | weekly: rising formats, new climbers, a teardown of each new 10k+ game | charts, RoWatcher |
| **Game Designer** | Cracky4 / Jandel | one-page pitches, a script for the first 60 seconds, reviews each build against the recommender's signals, cuts scope | PLAYBOOK.md, this file, playtest notes |
| **Luau Engineer** | ForyxeV / SenseiWarrior | Claude Code inside a Rojo project; server-authoritative code, anti-exploit checks, mobile performance budgets, tests | the repo |
| **Economy Designer** | Uplift / Murder Mystery 2 / RIVALS economy | item rarities, drop rates, trade values, pass pricing; a simulation that flags inflation and pay-to-win | economy sheet, analytics |
| **Live-ops Producer** | Grow a Garden's events teams | a weekly update calendar, event themes 2–3 weeks ahead, patch notes, [UPD] title tags | the calendar, the trend note |
| **Analyst** | the studio's data lead | weekly read of Creator Analytics exports against benchmarks; applies the kill/scale rule | Creator Analytics CSVs |
| **Packaging & Community** | growth and community manager | thumbnail/icon briefs (3–5 variants to test), title tests, clip scripts, Discord posts | analytics, builds |

**Still human:**
- **3D building, art and animation:** buy from the Creator Store or a freelancer, or use Roblox's AI 3D generation for props.
- **Watching real players:** the 99 Nights team's single most specific piece of advice.
