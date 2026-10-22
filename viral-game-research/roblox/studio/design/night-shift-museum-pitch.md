# Pitch: Night-Shift Museum [Anomaly]

*One page, game-designer, Oct 22 2026. Status: **awaiting approval**. This is the learning launch: cheap, fast and meant to be thrown away. Success means learning the Roblox funnel and building museum assets that Hide as a Painting reuses.*

## The format we're joining
The data shows a consistent "[Anomaly]" format: **you work a job, things come to you, and some of them are monsters you have to spot and reject.**

| Game (launched) | Peak concurrent | Days to 1k | Now / peak | Like ratio | Server size |
|---|---|---|---|---|---|
| Animal Hospital (Anomaly) (May 10) | **677k** | — | 3% | 0.93 | 30 |
| Sell Fries! [Anomaly] (Sep 21) | 105k | 13.9 | 23% | 0.83 | 16 |
| Scary Shawarma Kiosk: the ANOMALY (Aug 2025) | 33k | — | 8% | 0.90 | 30 |
| Animal Daycare (Anomaly) (Aug 14) | 23k | 34.8 | 10% | 0.81 | 25 |
| Clone Baby Care (Anomaly) (Oct 9) | 23k | 7.4 | 59% (still young) | 0.88 | 24 |
| Anomaly Cafe (Jul 3) | 14k | 35.1 | 15% | 0.95 | 24 |
| Airport Security (Anomaly) (Sep 30) | 4k | 16.9 | 61% (young) | 0.92 | 30 |

*A dash means the game launched before our player-count histories begin.*

**What the table says:**
- Of the 6 Anomaly games whose whole launch we observed, the median took **15 days to reach 1k** and the median peak is **~20k**.
- Two passed 100k, and like ratios are high (0.81–0.95).
- **Every one fades:** games past their peak are at 3–23% of it.

That's fine for a learning launch, and it's why this game isn't the main bet.

## The game
- **Core loop:** you're a night guard at a museum. Every night, crates of new artwork and late-night visitors arrive at your security desk. Inspect each one and **let it in or lock it out**. Some paintings are alive and some visitors aren't human. Survive 5 nights.
- **Our twist on the format:**
  - What arrives is **artwork**: a painting whose eyes follow you, a frame with no reflection, a statue that's warm.
  - Between waves you **patrol the gallery**, because anything you let in can *move*.
  - Spotting "the painting that changed" is the same skill a seeker uses in Hide as a Painting, so the two games share players' skills as well as assets.

## The first 60 seconds (decides bounce)
| Seconds | What happens |
|---|---|
| 0–10 | The player spawns at the security desk with a flashlight. A radio voice says: "Night 1. Check everything that comes in." No menu. |
| 10–30 | The first crate arrives with an *obvious* anomaly (the painting blinks). One big button: **LOCK OUT** → success sound + coins. |
| 30–45 | A normal visitor arrives. If the player locks them out, a mild penalty and "be careful…". Teaches judgement. |
| 45–60 | The lights flicker, a 3-minute night timer starts, and the first patrol prompt appears: "Something in Gallery A moved." The hook is set. |

## Retention (light on purpose)
- **Score that pulls players back:** "Nights survived" plus a best-run leaderboard.
- **Guard cosmetics** bought with coins: flashlight colours, badges.
- **Weekly content drop:** a new wing with ~6 new anomalies. Anomalies are **data rows** (asset + tell + correct answer), so each weekly drop is small work.

## Co-play
- A shift takes 1–4 guards: one at the desk, others on patrol. Each sees things the others don't, so they have to talk ("did the lady in Gallery B have a shadow?").
- Lobby servers hold ~16, like Sell Fries!.

## Money (minimal)
- 2 game passes, near the Anomaly median of ~150 Robux: a cosmetic flashlight pack, and a "second radio" (one revive per run, PvE only).
- One developer product: a revive.
- Nothing affects other players.

## Risks
**Riskiest assumption:** that the **museum and art theme** pulls as well as the food and animal-care jobs the hits use. Every big Anomaly game so far is a *service job with customers*.

**Cheapest tests:**
1. Load **3 thumbnail concepts** into Roblox's thumbnail test in week 1: desk inspection, a creepy painting close-up, guards with flashlights. Compare play-through rate to the benchmark.
2. Before launch, run a grey-box playtest with 5 friends, watched without telling them. Do they replay night 2 without being asked?

**Other risks:**
- **Copy demotion:** the theme, art-arrival twist and patrol phase keep it from reading as a copy.
- **Fear level:** spooky, not gory. Roblox's audience is young.

## Scope (fits the plan)
- **Week 1 (jam):**
  - one wing, the desk and patrol;
  - 12 anomalies as data;
  - 5 nights;
  - 1–4 player shifts;
  - phone-first big buttons;
  - Creator Store assets.
- **Week 2:** polish the first 60 s, thumbnails, Discord, launch.
- **Week 3:** first weekly update (a new wing).
- **Not in scope:** trading, story mode, custom 3D art.

## Learning goals
These are the numbers we're shipping it to get:
- play-through rate by thumbnail;
- share of players past 60 s and past 180 s;
- D1 return;
- share of sessions with friends;
- what one weekly update does to the numbers.

**Decision rule** (PLAYBOOK.md): give it 4–5 weeks. Kill it if it never passes ~1k concurrent and sits in the bottom half of benchmarks. Scale it if it passes 10k.
