# 20 concepts scored against the model

Scores come from the models fit on all 122 non-Telegram games: full, conventional+context, and conventional+spectator. They are rank-averaged.
The model has known blind spots (see the backtest), so channel evidence, crowding and build cost are shown next to the score, not folded into it.

| Rank | Concept | Platform | Model score | P(hit) full | P(hit) conv+ctx | P(hit) conv+spectator | Channel evidence | Crowding | Build (weeks) | LLM cost | Revenue/yr at 1M DAU (mid) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Pictionary Obby | roblox | 0.92 | 0.93 | 0.79 | 0.89 | high | some | 8 | no | $4.4M |
| 2 | Hide as a Painting | roblox | 0.92 | 0.93 | 0.79 | 0.89 | high | some | 6 | no | $4.4M |
| 3 | Telephone Pictionary Chains | web | 0.86 | 0.93 | 0.68 | 0.93 | medium-low | some | 4 | no | $4.4M |
| 4 | Imposter Bot | roblox | 0.85 | 0.90 | 0.83 | 0.87 | high | some | 8 | yes | $4.4M |
| 5 | Group-Chat Fibbage | web | 0.82 | 0.93 | 0.60 | 0.92 | medium-low | some | 3 | no | $4.4M |
| 6 | Daily Heist | roblox | 0.80 | 0.90 | 0.78 | 0.85 | high | some | 8 | no | $4.4M |
| 7 | Server Daily Quiz | discord | 0.65 | 0.83 | 0.72 | 0.65 | unproven | some | 4 | no | $1.8M |
| 8 | Two Truths Live | mobile | 0.58 | 0.61 | 0.68 | 0.67 | low | some | 5 | no | $18.2M |
| 9 | Infinite Kitchen | web | 0.55 | 0.75 | 0.27 | 0.79 | medium-low | some | 4 | yes | $4.4M |
| 10 | Talk Your Way Out | web | 0.48 | 0.78 | 0.25 | 0.66 | medium-low | some | 3 | yes | $4.4M |
| 11 | Grow-a-[New Theme] Live-Ops | roblox | 0.48 | 0.40 | 0.57 | 0.78 | high | many | 5 | no | $4.4M |
| 12 | Who's Most Likely (Group Edition) | web | 0.48 | 0.61 | 0.60 | 0.62 | medium-low | some | 3 | no | $4.4M |
| 13 | Rage Hop Replays | mobile | 0.47 | 0.76 | 0.25 | 0.66 | low | many | 3 | no | $18.2M |
| 14 | Couple's Daily | web | 0.44 | 0.47 | 0.60 | 0.62 | medium-low | none | 4 | no | $4.4M |
| 15 | Community Crossword (Reddit) | reddit | 0.42 | 0.73 | 0.56 | 0.26 | unproven | none | 4 | no | $1.8M |
| 16 | Timeline Daily | web | 0.23 | 0.32 | 0.25 | 0.23 | medium-low | many | 2 | no | $4.4M |
| 17 | Dupe Day | web | 0.22 | 0.26 | 0.25 | 0.23 | medium-low | some | 2 | no | $4.4M |
| 18 | Higher-Lower Daily | web | 0.15 | 0.12 | 0.10 | 0.23 | medium-low | many | 1 | no | $4.4M |
| 19 | Guess the Year | web | 0.13 | 0.07 | 0.10 | 0.23 | medium-low | many | 2 | no | $4.4M |
| 20 | Cricket Immaculate Grid | web | 0.05 | 0.06 | 0.06 | 0.16 | medium-low | some | 2 | no | $4.4M |

## Pitches

- **Pictionary Obby** (roblox): Race an obstacle course where the course is drawn live by the previous winner.
- **Hide as a Painting** (roblox): Prop-hunt in a haunted museum: hiders become paintings and statues, seekers hunt them; daily new gallery layout.
- **Telephone Pictionary Chains** (web): Async telephone game in a group chat (draw -> describe -> draw); each chain ends as a 6-second GIF for the group.
- **Imposter Bot** (roblox): Social deduction where one 'player' in every lobby is an AI; find the bot before it convinces you that you are the bot.
- **Group-Chat Fibbage** (web): One prompt a day ('What's the real reason koalas sleep 20 hours?'). Friends in a group link each write a fake answer, then everyone votes for the truth; the reveal is a shareable card of the funniest lies.
- **Daily Heist** (roblox): Everyone on Roblox gets the same co-op escape room each day; servers race; global leaderboard and 'first squad' badges.
- **Server Daily Quiz** (discord): Discord Activity: the whole server plays the same 5 questions daily; leaderboard posted in channel.
- **Two Truths Live** (mobile): Async 'two truths and a lie' with friends using camera-roll photos; reveal reel at the end.
- **Infinite Kitchen** (web): Combine ingredients; an LLM invents (and caches) the dish; a daily target dish to reach in the fewest steps.
- **Talk Your Way Out** (web): Daily AI gatekeeper with a secret password; you get 5 messages to talk your way past. The share card shows your shortest winning line and the AI's best rebuttal.
- **Grow-a-[New Theme] Live-Ops** (roblox): Idle grow-and-steal loop with offline growth, restocks and weekly admin events, in an unclaimed theme.
- **Who's Most Likely (Group Edition)** (web): Friends answer 'who in this group is most likely to...' about each other; results reveal as superlatives cards.
- **Rage Hop Replays** (mobile): One-tap rage platformer that auto-cuts your best fail into a 6-second vertical clip with the level seed.
- **Couple's Daily** (web): Two-player co-op daily puzzle: each partner sees half the clues; share card = joint time.
- **Community Crossword (Reddit)** (reddit): Reddit Devvit game: a subreddit co-builds and solves a daily crossword about its own topic.
- **Timeline Daily** (web): Place 6 events in order (Timeline card-game rules); daily grid.
- **Dupe Day** (web): 5 pairs a day: real photo or AI fake? Emoji grid of your hits and misses, plus a percentile.
- **Higher-Lower Daily** (web): Which has more (Google searches, calories, population)? Daily streak grid.
- **Guess the Year** (web): One photo a day; guess the year on a slider; grid of how close you got.
- **Cricket Immaculate Grid** (web): Immaculate Grid for cricket fans (South Asia, UK, Australia).

## Full-model coefficients used for scoring (standardized)

- `spectator_high`: +0.85
- `friends_graph`: +0.82
- `share_in_product`: -0.63
- `novel`: +0.59
- `one_input`: +0.45
- `new_channel`: +0.42
- `fast_ttff`: +0.34
- `rules_preknown`: +0.30
- `has_audience`: +0.29
- `paid_ua`: +0.24
- `invite_needed`: -0.19
- `failure_comedy`: +0.17
- `short_session`: +0.15
- `free_to_play`: +0.13
- `emergent_output`: +0.09
- `daily_or_scarcity`: +0.04
- `artifact_curiosity`: -0.03
- `ip_licensed`: +0.00
