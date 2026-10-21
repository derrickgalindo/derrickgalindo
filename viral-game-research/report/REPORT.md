# What to build: evidence from 126 casual games, their clones, SEC filings and search data

*Research for a solo-built game aiming at 1M daily players within 90 days, with no paid marketing. About a 15-minute read.
Every number traces to `data/viral_games.db`. The scripts that regenerate them are listed in the [README](../README.md).*

---

## The answer in five lines

1. **There is no stable recipe, and simplicity doesn't separate hits from flops.**
   - A model of the textbook viral recipe, trained on 2008–2015 hits, ranks 2016–2025 games *worse than chance* (held-out AUC 0.28).
   - The recipe gets copied, the copies flop, and the next hits come from a different channel.
2. **Three things do hold out of sample: watchability, a channel with spare reach, and retention.**
   - Watchability (spectator value) is the one pre-registered new signal that passed the held-out test in both versions: my hand coding and an objective YouTube-vs-web search measure.
   - It sparks growth but does not sustain it. Watchable hits keep 12% of peak interest after a year; the rest keep 29%.
3. **1M daily players in 90 days is arithmetically reachable, but only one channel produces it regularly today.**
   - It needs a sustained ~8–9-day doubling from a 1,000-player seed.
   - Roblox produced several zero-ad games that cleared it in 2025. Grow a Garden went from ~1,000 concurrent players in April to 21.3M concurrent on day 87.
   - 44% of Roblox's revenue comes through the Apple and Google stores, so this is effectively a mobile channel.
4. **Business: build on Roblox and keep it. Take a partner's minority stake rather than selling outright, unless a buyer pays at least one year of revenue.**
   - Roblox hits fade fast: about 8% of peak search interest a year later. So most of the value comes in year one: about $4.4M at 1M average DAU (range $1.5–11M), with zero hosting cost.
   - Audience-only exits pay about $0.5–1 per daily player (Wordle). Buying at the peak has been punished (Zynga wrote off 52% of OMGPOP within six months).
5. **Top three concepts:** *Hide as a Painting* (Roblox prop-hunt), *Pictionary Obby* (Roblox) and *Telephone Pictionary Chains* (web, group chat). Each can be demand-tested in 1–2 weeks for under $100. The kill thresholds come from the DAU math.

---

## 1. What I added to your brief, and what it found

You asked what top studios would research that you didn't ask for. These are the eight additions; seven produced the findings below (Apple's clone rule and Roblox's kids-privacy obligations are under platform risk in §8 and §10).

| Added research | Finding |
|---|---|
| **DAU math and retention** (studios kill games over D1 retention, not virality) | 1M DAU on day 90 from 1,000 seed players needs ~8-day doubling. Ritual-grade retention cuts the sharing each player must do from 0.68 to 0.21 new installs per active day, and the installs needed from 7.6M to 2.3M (§6). |
| **Which channels have spare reach in 2026** | Roblox's recommender is the one channel in the data still producing frequent zero-ad breakouts. Daily web puzzles are saturated. Organic mobile app-store breakouts are rare since paid acquisition took over (Rovio's user-acquisition spend went from €6.3M in 2015 to €69.6M in 2017). |
| **Time-to-clone and defensibility** | Clones arrive within days: 300 Flappy Bird clones in 4 days, and a third of all new iOS games on Feb 27 2014. Followers often beat originals: 2048 over Threes, FarmVille over Farm Town, Mafia Wars over Mob Wars, Suika over Merge Big Watermelon, and Stumble Guys reached 20M DAU on the platform Fall Guys skipped. |
| **Post-peak decay** | Across 74 hits, interest halves a median 12 weeks after peak, and is at 22% of peak a year later. Roblox hits are at 3–9%. Wordle (34%) and Connections (48%) are the durable exceptions. |
| **Cost to serve per player** | Static web and Roblox (free hosting) cost close to nothing per player. LLM features cost money every time a player triggers one, which ruled out several AI concepts (§9). |
| **Studio kill rates and census-style base rates** | Supercell: 5 hits from about 35 games. Wordle-likes: 51% never registered any search interest. Roblox: none of 7,356 random 2024–25 experiences reached 1,000 visits (§7). |
| **2023–2026 data** | Roblox and Telegram breakouts are in the dataset, so the model isn't fit only to a vanished era. |

---

## 2. The dataset

`data/viral_games.db` (SQLite; CSV copies in `data/export/`):

- **126 hand-coded games (75 hits)** in 17 cohorts. They include the five you named, 20–30 more viral casual games, and deliberately their **clones, predecessors, contemporaries and same-creator follow-ups** (Swing Copters, Draw Something 2, Amazing Alex, Wizards Unite…).
- **133 census Wordle-likes** from *Wordles of the World*: the failures listicles never name, measured in Google Trends.
- **The same 20 variables for every game:** session length, time to first fun, single input, borrowed rules, share artifact (and whether it intrigues without spoiling), invite loop, daily sync, scarcity, social graph, spectator value, failure comedy, emergent output, monetization, IP, creator audience, paid acquisition, channel newness and novelty.
- **How each documented hit broke out:** latent days, what triggered it, first community, and whether an influencer arrived before or after growth.
- **77 sources, typed by kind:**
  - SEC filings: NYT 10-Ks and 8-Ks, Zynga's S-1 and 10-Qs, King's F-1, Roblox's letters and 10-K.
  - Rovio's 2017 annual report.
  - Creator statements: Wardle's tweet and GDC talk, Nguyen in Rolling Stone, Jandel on Grow a Garden.
  - Raw data: Google Trends (weekly for all 126 games; daily for the case studies; YouTube-search for 123), the Roblox API, and the census.
  - Secondary press fills gaps and is labelled as such.

**Caveat:** I hand-coded the features and I know the outcomes. To limit the damage, the predictions were pre-registered and committed to git before testing (`model/PREREGISTRATION.md`), and the signal that passed was re-tested with an objective proxy pulled from data (§5).

---

## 3. Your premise, stress-tested

**Hypothesis:** a repeatable recipe exists, with simplicity at its core.

**Simplicity doesn't discriminate.**
- 64 of 126 games are simple on all three counts (one input, sessions of 5 minutes or less, first fun within 10 seconds). They hit 69% of the time, against 56% for the rest.
- The 20 simple non-hits are nearly all clones (Absurdle, Dordle, Worldle, Splashy Fish, Swing Copters…).
- Many of the biggest hits are not simple: Among Us, FarmVille, Pokémon GO, Draw Something, Grow a Garden.
- Simplicity is the price of entry for the whole category, so it can't be what separates the winners.

**The recipe inverts across eras.**
- Trained on pre-2016 games, the conventional model scores 0.28 AUC on 2016+ games.
- With the 2021–25 Wordle-clone cohort removed from the test set, it still scores 0.46.
- The features that marked the old hits (an in-product share artifact, instant first fun, a daily hook) carry the biggest positive weights, and they are exactly what every clone copies.
- The new hits (Among Us, Fall Guys, Roblox games) have long sessions, lobbies and streamers.

**Timing and platform shifts did much of the work.**
- **A natural experiment:** Facebook cut app notifications in early 2010, and Zynga's average DAU fell from 67M to 48M over 2010 with the same games. Zynga's S-1: "These changes limited the level of communication among users about applications… the number of our players on Facebook declined". The channel, not the game, was carrying growth.
- **The same mechanic wins or loses with the channel.**
  - OMGPOP's *Draw My Thing* (web, 2008) went nowhere; the same idea on iPhone, *Draw Something* (2012), reached ~14M DAU.
  - Niantic's *Ingress* stayed niche; the same mechanic plus Pokémon became *Pokémon GO*.
  - IP isn't enough either: *Harry Potter: Wizards Unite* earned ~$12M in its first month against Pokémon GO's ~$300M (Sensor Tower estimates) and closed in 2022.
- Games launched on a new or newly opened channel hit 87% of the time (in my coding), against 43% on saturated channels.
- **Creators repeating their own recipe:** 7 of 12 follow-ups hit, and every one of those 7 had King, Zynga, Rovio or Niantic distribution behind it. The one follow-up with nothing behind it but its creator's fame, Swing Copters, faded.

**Influencers mostly amplified growth that had already started.**
- Flappy Bird was US #1 on Jan 17 2014; PewDiePie's video went up on Jan 27.
- Words with Friends' founders saw growth inflecting before John Mayer's Oct 2009 tweet.
- The influencer-caused cases are recent and streamer-native:
  - **Among Us** sat in the "low double digits" of players for most of its first year. Search interest crossed 5% of its 2020 peak in South Korea on May 31, Brazil on June 19, and the US only on Aug 15, after Sodapoppin's July 15 stream.
  - **Suika Game** sat for 21 months until Japanese VTubers picked it up.

**Luck shows up as a waiting period you have to survive.** The 12 hits that had no creator audience, no IP and no paid push waited a **median of 78 days** (range 3–778) before breaking out. They survived the wait because they cost nothing to run.

### Flappy Bird: what changed after months unnoticed
Nothing in the game changed. The only update, a bug fix, shipped in September. The documented trail:
- 13 reviews between May 25 and Oct 31 2013.
- First tweet Nov 4.
- US game charts in November at #1,368.

Daily Google Trends puts the turn in **the first half of December 2013**:
- US search first registers on **Dec 5**, then rises ~11x in two weeks (weekly index 5 → 57 by Dec 22).
- This coincides with the game entering the US top 250 free apps on Dec 13, with frustrated "I can't beat this" tweets from US teenagers, and with the school holidays.
- After a holiday plateau, search doubled every **3.1–3.7 days** between Jan 10 (US top 10) and Jan 26. It slowed to **7.9 days** after PewDiePie's video on Jan 27.

The bot accusations were never substantiated. The best-supported story is word of mouth among teenagers that crossed the threshold where App Store chart visibility feeds itself, during a holiday, with no influencer before the climb.

### Did Wordle's share grid cause the spread, or follow it?
**Both, in sequence.**
- **Spread began without the grid.** 90 players on Nov 1 2021 came via a family group chat and an NYT newsletter footnote.
- **The grid came from users.** A New Zealand player typed it by hand, and others copied her before any button existed. Wardle credited her (@irihapeta) in the tweet announcing the button, which its ID dates to **2021-12-16 14:54 UTC**.
- **What changed after the button:**
  - In a Trends window ending Jan 2 (before the NYT profile), worldwide search for "wordle" is flat until Dec 15, then doubles every **2.9 days** for 17 days (US 3.0, Australia 3.6, UK 4.7).
  - Working back from 300,000 players on Jan 2 at that rate puts about 5,000 players on Dec 16. Getting from 90 players on Nov 1 to ~5,000 by Dec 16 means doubling roughly every 8 days without the button.
  - The button therefore coincides with growth running about **2.7x faster**. The holidays are a confound I can't remove.
  - The NYT profile (Jan 3) and celebrity posts broadened reach afterwards. Search doubled every ~7 days through mid-January, from ~300,000 players to ~2M.
- **Lesson:** the grid made existing word of mouth cheaper and more visible. It didn't create it, and copies of it never worked (§5).

### Did Wordle sell for over $1 million?
**Yes, by the NYT's own statement, but the filings never give the exact price.**
- The NYT announced it as "in the low seven figures" (Jan 31 2022, Reuters), i.e. at least $1.0M.
- The FY2021 10-K says only "In January 2022, we acquired Wordle". FY2022 cash flow shows $515.6M of acquisitions net of cash, almost all The Athletic (~$550M), so Wordle was immaterial.
- What the NYT bought shows up in its filings: "Wordle brought an unprecedented tens of millions of new users to The Times… our best quarter ever for net subscriber additions to Games" (Q1 2022 8-K). Every 10-K since lists Wordle (and later Connections) as free content used "to generate large audiences… eventually converting them into subscribers".

---

## 4. The model and its held-out test

The pre-registered bar: the held-out AUC CI sits above 0.5 on the temporal split **and** leave-one-cohort-out AUC is above 0.6. "Own clones" is the share of same-cohort hit/non-hit pairs in which the hit scores higher.

| Model | Temporal holdout: train <2016, test 2016+ (95% CI) | Leave-one-cohort-out | Hit outscores its own clones |
|---|---|---|---|
| Conventional recipe | **0.28** (0.17–0.42) | 0.67 | 63% |
| Context only (audience, IP, paid, channel, novelty) | 0.56 (0.41–0.69) | 0.60 | 72% |
| Conventional + context | 0.31 (0.18–0.45) | 0.65 | 78% |
| Full (+ novel candidates) | 0.32 (0.18–0.45) | **0.71** | 78% |

**Verdict: every variant fails the pre-registered bar.**
- It separates hits from flops moderately *within* an era (leave-one-cohort-out 0.60–0.71).
- It ranks a hit above its own clones about 3 times in 4.
- It cannot carry a recipe *across* eras.

**Where it fails:**
- **False positives:** almost all are 2022–25 Wordle-likes, scored 0.64–0.95 (Costcodle, LoLdle, Worldle, Travle, Contexto, Semantle, Nerdle, Globle…).
- **False negatives:** the streamer and Roblox era, scored 0.01–0.08 (Goose Goose Duck, Dead Rails, 99 Nights, Doors, Stumble Guys, Among Us, skribbl.io, Dress to Impress, Fall Guys, Grow a Garden).
- **The clone paradox:** 114 hit/non-hit pairs in the same cohort have identical recipe features (40 daily-word pairs, 35 one-tap pairs). No model built on mechanics can tell Flappy Bird from Splashy Fish or Wordle from Lewdle.

---

## 5. A new signal: watchability

Pre-registered candidates, tested on the temporal holdout:

| Candidate | Hit rate with / without | Held-out AUC (95% CI) | Improves model on both splits | Holds |
|---|---|---|---|---|
| **Spectator value (hand-coded)** | **85% / 55%** | **0.70 (0.60–0.80)** | **+0.043 / +0.050** | **Yes** |
| **Watch ratio (objective: YouTube vs web search, 92 games)** | — | **0.69 (0.51–0.86)** | — | **Yes, narrowly** |
| Emergent output (every play makes something unique) | 71% / 59% | 0.61 (0.52–0.70) | +0.002 / +0.009 | Marginal |
| Failure comedy | 74% / 53% | 0.75 (0.65–0.85) | −0.017 / +0.007 | No: overlaps with simplicity |
| Borrowed rules (Scrabble, Pictionary, Mafia…) | 60% / 63% | 0.45 | ~0 | No |
| Intriguing share artifact (the emoji grid) | **28% / 67%** | **0.35** | 0 | **No: the sign is reversed** |
| Early search momentum (weeks 5–8 vs 1–4) | — | 0.60 (0.44–0.75) on 55 games | — | No |

**What this says:**
- **Watchability holds.** Most articles treat a streamer finding a game as luck. The data say it's a property of the game, and it can be measured before launch: post clips and see whether people watch and share them (§9).
- **Roblox publishes what its recommender rewards:** "qualified play-through rate, 7-day play days per user, and 7-day intentional co-play days" (Q4 2025 letter). Watchable, co-play games produce exactly those signals.
- **The objective check is weak but real.** The watch ratio has only a 0.21 correlation with my hand coding, and web games are searched for by name every day just to open them, which distorts it. So treat the finding as moderate evidence, not proof.
- **The famous emoji grid has a reversed sign.** Games with an intriguing share artifact hit 28% of the time against 67% for the rest, because hundreds of clones copied the grid.
- **Watchability's trade-off:** watchable hits keep 12% of peak interest a year later, against 29% for the rest. Design for retention as well.

---

## 6. Epidemiology: k-factors and the 90-day math

**The model:** every active player-day produces κ new installs. The k-factor is then R = κ × (expected active days per install), so for games spread by sharing, retention multiplies virality. Seed = 1,000 players. Retention rows: median and top-quartile mobile come from GameAnalytics benchmarks; the ritual row is an assumption.

| Retention (D1 / D7 / D30) | κ needed per active player-day | k-factor R | Installs needed by day 90 |
|---|---|---|---|
| Median mobile (22% / 4% / 0.8%) | 0.68 | 1.8 | 7.6M |
| Top-quartile casual (32% / 12% / 4%) | 0.47 | 4.3 | 5.1M |
| Strong casual hit (45% / 20% / 10%) | 0.33 | 7.5 | 3.7M |
| Daily ritual (55% / 40% / 28%) | 0.21 | 16.6 | 2.3M |

**Requirement:** going from 1,000 to 1M daily players in 90 days takes a doubling every **9.0 days** or faster, sustained.

**Observed growth** (k assumes one share "generation" takes 1–3 days for Wordle, 1–4 for Roblox, 2–7 for Among Us):

| Game | Window | Doubling | k per generation |
|---|---|---|---|
| Wordle | 90 → 300,000 players (Nov 1–Jan 2) | 5.3 days | 1.14–1.48 |
| Wordle | 300k → ~2M (Jan 2–14, includes NYT profile) | 4.4 days | 1.17–1.61 |
| Grow a Garden | ~1,000 → 5M concurrent (mid-Apr–May 18 2025) | 2.7 days | 1.29–2.81 |
| Among Us | Twitch viewers 460 → 53,000 (Jun–Aug 2020) | 8.9 days | 1.17–1.72 |
| FarmVille | ~1M new DAU per week, linear | — | Platform-fed, not an epidemic curve |
| Draw Something | 14.3M → 10.4M DAU (Apr–May 2012) | Shrinking | 0.93–0.97 (< 1) |

**What this says:**
- These rates are upper bounds on person-to-person spread, because they include press and algorithm pushes.
- Real hits ran at **k ≈ 1.1–1.6 per generation, with very short generations.** Nobody needs k = 3. What matters is a loop that turns over within a day or two, plus retention.
- With median retention, every active player would have to bring in 0.68 new installs *every day*, which is implausible. With ritual retention, 0.21.

---

## 7. Skeptical investing: the base rates a short seller would use

| Population | Outcome |
|---|---|
| 133 English Wordle-likes (census) | 51% never registered measurable search interest. 9.8% reached a quarter of Nerdle's peak, which is under 1% of Wordle's. 3.8% matched Nerdle. None came near Wordle. These are upper bounds, because generic names like "START" pick up unrelated searches. |
| ~300 Flappy Bird clones in 4 days (Pocket Gamer); 95 of 293 new iOS games on Feb 27 2014 | None sustained a US top-10 position. Splashy Fish and Ironpants charted briefly. |
| Roblox: >14M active experiences in 2025 (10-K) | 2 set 20M+ concurrent records. About 1,000 creators averaged $1.3M. A random sample of 7,356 experiences created in 2024–25 (104 real attempts) had **zero** with even 1,000 lifetime visits; the best had 254. |
| Supercell (CEO, 2023) | 5 hits out of about 35 games; 30+ killed. |
| Same-creator follow-ups | 7/12 hit, all with a publisher's distribution behind them. |

**Peaks are worth less than they look:**
- Across 74 hits, search interest halves a median **12 weeks** after peak, and is at **22%** of peak a year later.
- Draw Something lost 33% of its daily players in 30 days.
- Hamster Kombat lost 86% after its token airdrop.
- Steal a Brainrot fell ~99% from 25.4M concurrent players.
- HQ Trivia went from 2.38M concurrent to shutdown in two years.
- Zynga paid $183.1M for OMGPOP on Mar 21 2012 and wrote off $95.5M by Sep 30.

The durable exceptions are rituals and live-ops machines: Connections (48% of peak after a year), Wordle (34%) and Candy Crush (48%).

**Short thesis on any viral game:** unless it has a ritual loop or a live-ops machine, value it at about one year of revenue.

**Behavioral science, applied to the loop:**
- **Habits take a median of 66 days to form** (range 18–254; Lally et al. 2010). A game must survive about two months of repetition, which matches the observed 78-day median wait before breakout.
- **Habits attach to stable cues** (Wood & Neal 2007). The group chat is the cue.
- **Rationing raises value** (Worchel et al. 1975, scarcity).
- **Near-misses sustain play** (Clark et al. 2009, *Neuron*): Flappy Bird's pipes.
- **Effort rises as a goal gets close** (goal gradient; Kivetz et al. 2006): Grow a Garden's growing plants.
- **Competence, autonomy and relatedness predict continued play** (Ryan, Rigby & Przybylski 2006).
- **Shared results work through social comparison** (Festinger 1954).

The data add one warning: having a daily-sync hook didn't make hits last longer (23% vs 22% of peak after a year). The rituals that lasted had both a cue and a real social payoff.

---

## 8. Business model, with numbers

**Revenue per daily player per day, net to the developer:**

| Model | Low / mid / high | Per year at 1M DAU (mid) | Evidence |
|---|---|---|---|
| Web daily game, ads | $0.005 / $0.012 / $0.027 | $4.4M | Assumption from ad rates. Order-of-magnitude checks: Flappy Bird ~$0.005 (2014), Slither.io ~$0.01 (2016) |
| Mobile app, ads | $0.03 / $0.05 / $0.08 | $18.2M | Third-party benchmarks. Needs app-store reach that is now bought: Rovio spent €69.6M on acquisition in 2017 while its DAU fell from 13.5M to 9.2M |
| Mobile app, in-app purchases, net of 30% store fee | $0.025 / $0.038 / $0.066 | $14.0M | King Q4'13 $0.055 gross; Rovio Q4'17 ~$0.094 gross; Zynga 2011 $0.053 (filings) |
| **Roblox (creator's DevEx share)** | $0.004 / $0.012 / $0.031 | **$4.4M** | Roblox bookings per DAU $0.138–0.141 × 22% DevEx share = $0.031 per *platform* DAU (2025 letters). Free hosting |
| Subscription funnel | $0.001 / $0.005 / $0.010 | $1.8M | NYT single-product ARPU ≈ $3.5/month; 1–5% conversion assumed |

**Five-year value if kept** (1M average DAU in year one, 15% discount rate). Decay rates are measured from Trends:
- **Roblox-typical, 8% of peak kept per year:** web or Roblox $4.7M; mobile in-app $15.0M.
- **Median hit, 22%:** web or Roblox $5.4M; mobile in-app $17.3M.
- **Ritual, 45%:** web or Roblox $7.1M; mobile in-app $22.8M.

**What buyers paid for, and what they watched:**

| Deal | Price | What was bought | Result |
|---|---|---|---|
| NYT ← Wordle (2022) | Low 7 figures (~$0.5–1 per daily player) | Audience, daily habit, subscriber funnel | "Tens of millions of new users"; record Games subscriber adds |
| Zynga ← Newtoy / Words with Friends (2010) | $53.3M | Audience, mobile social graph, team | DAU doubled within ~120 days through cross-promotion |
| Zynga ← OMGPOP / Draw Something (2012) | $183.1M at the peak (~$13 per daily player) | Peak audience | 52% written off within six months |
| Activision ← King (2015) | $5.9B | Revenue, 474M MAU, live-ops | Still a top franchise |
| Take-Two ← Zynga (2022) | $12.7B | Mobile revenue portfolio | — |
| Scopely ← Niantic games (2025) | $3.5B (>$1B revenue; ~3.5x) | Revenue, licensed IP | — |
| Scopely ← Stumble Guys; Spotify ← Heardle; Merriam-Webster ← Quordle | Undisclosed | Daily players (20M for Stumble Guys) and funnels | Spotify shut Heardle down within a year |
| Splitting Point ← ~50% of Grow a Garden (Apr 2025) | Undisclosed stake at ~1,000 concurrent players | Early habit plus live-ops and reach | 22M concurrent ten weeks later |

The metrics these buyers report and price on: DAU, MAU, unique payers, bookings per DAU (Zynga's ABPU, King's payer bookings, Roblox's ABPDAU), revenue concentration (Candy Crush was 78% of King's bookings), user-acquisition payback (Rovio: 8–10 months) and conversion to subscribers (NYT).

**Recommendation: build on Roblox, which is effectively mobile, and keep it.**
- **Why Roblox:**
  - It's the only channel in the data still producing zero-ad 1M+ DAU breakouts several times a year.
  - Its recommender rewards the co-play and retention signals that held up out of sample.
  - It hosts for free and handles payments.
  - 1M DAU is worth about $4.4M a year at the mid estimate.
- **Why not the alternatives:**
  - **Mobile apps** pay 3–4x more per player, but organic reach is the binding constraint, and that is exactly the one you set.
  - **Web daily puzzles** have the only proven exit buyers (NYT, Merriam-Webster, Spotify), but they pay audience prices (around $1M), the category is saturated, and their clones are the model's worst false positives.
- **Sell or keep:**
  - Because Roblox hits keep only ~8% of peak a year later, a kept hit is worth only ~1.07x its first year. A full sale at 1x revenue or more during the run therefore beats holding.
  - Buyers know this (OMGPOP), so the realistic deal is a **minority stake to an established Roblox studio** for live-ops capacity and reach, as Grow a Garden did at ~1,000 concurrent players, or IP licensing (Grow a Garden has a film in development, per Deadline).
  - Extend the run with sequels: "Grow a Garden 2" climbed quickly to the top, per Roblox's Q2 2026 letter.
- **Risks:** platform dependence (DevEx rate and recommender changes; Roblox says one shifted its own revenue mix in Q2 2026), a young audience (COPPA, moderation) and fast decay.

---

## 9. Concepts: 20 scored, three ranked

All 20 were coded on the same variables and scored by the models (rank-averaged). The full table is in `analysis/concepts.md`. In brief:
- Roblox and group-chat concepts with high watchability and co-play top the list.
- Daily-grid web puzzles (Timeline Daily, Higher-Lower, Guess the Year, a cricket Immaculate Grid) sit at the bottom, scoring 0.05–0.23, which matches the clone cohort that failed.
- The LLM concepts (Talk Your Way Out, Infinite Kitchen) score mid-pack and carry a per-play cost.

| Rank | Concept | Platform | Model score | Channel evidence |
|---|---|---|---|---|
| 1 | Hide as a Painting | Roblox | 0.92 | High |
| 2 | Pictionary Obby | Roblox | 0.92 | High |
| 3 | Telephone Pictionary Chains | Web | 0.86 | Medium-low |
| 4 | Imposter Bot | Roblox | 0.85 | High |
| 5 | Group-Chat Fibbage | Web | 0.82 | Medium-low |

The top two tie on model score. Hide as a Painting ranks first because it avoids the moderation and stroke-physics risks of Pictionary Obby.

### Kill thresholds that apply to all three tests

These come from `model/dau_math.csv`. Reaching 1M DAU by day 90 from about 1,000 seed players takes a sustained 8–9-day doubling, which is **about +70–80% more new players week over week**. At small scale, that rate requires one of these pairs:
- D7 retention of at least 20% with at least **0.33 new players per active player per day**; or
- D7 retention of at least 40% (ritual-grade) with at least **0.21**.

Below that, the game can still be a fine business. It won't reach 1M DAU in 90 days without paid marketing.

### #1 Hide as a Painting (Roblox)
**What it is:** prop hunt in a haunted museum.
- Hiders pick a frame or pedestal and pose as a painting or statue. Guards with flashlights get three minutes and a limited number of accusations.
- A new gallery layout each day, the same for every server, with a "best hiding spot of the day" board.

**Why the model ranks it at the top:**
- Spectator value is high: hide-and-seek reveals make good clips.
- Failure comedy (a "painting" caught mid-twitch) and emergent output (absurd avatar portraits worth screenshotting).
- Borrowed rules: hide-and-seek and Statues.
- Real friends graph and a channel whose recommender rewards co-play.

**Risk:** prop hunts already exist on Roblox. The museum, the posing and the daily shared layout are the difference, and that difference has to show in the first 10 seconds of a clip.

**Cheapest demand test (about 10 days, $0–50):**
1. **Days 1–3: watchability test before building.** Record three 15-second greybox clips in Roblox Studio (catch moment, pose reveal, near miss) and post them to TikTok and YouTube Shorts. Compare share and completion rates with your own median post. **Kill if** none beats your median.
2. **Days 4–10: one map, one round loop, published.** Recruit 30–50 players from 2–3 Roblox Discord communities. **Pass** if Creator Dashboard shows D1 at least 35%, average session at least 10 minutes, and a third or more of sessions in parties.
3. **Optional measurement buy:** spend $50 on Roblox sponsored ads to get an unbiased retention cohort. This is a measurement, not growth marketing.
4. **Weeks 3–6:** count organic visits week over week once the recommender starts testing it. **Keep going** only at +70% a week or better for two consecutive weeks.

### #2 Pictionary Obby (Roblox)
**What it is:** the artist gets a secret word and draws it. The strokes become the platforms of an obstacle course that teammates run while guessing the word. Points go to fast guesses and finishes.

**Why it scores high:**
- Spectator value is high, and it produces emergent, funny output: every course is a bad drawing you have to run across.
- Borrowed rules (Pictionary) and co-play.

**Risks:**
1. **Moderation.** Freehand drawing on a kids' platform needs stroke limits, filtering and report/kick tools. Existing Roblox drawing games show it's possible, but budget time for it.
2. **Physics.** Turning arbitrary strokes into fair platforms is the technical risk, and it should be prototyped first.

**Cheapest demand test (about 2 weeks, $0–50):**
1. **Days 1–4:** build a stroke-to-platform prototype and run the same three-clip watchability test as #1.
2. **Days 5–14:** a private server with 4–8-player lobbies, recruited from Discord. **Pass** on the same retention and party thresholds as #1, plus at least 3 rounds per session.

### #3 Telephone Pictionary Chains (web)
**What it is:** an asynchronous telephone game built for group chats.
- One person gets a prompt and draws it in 60 seconds. A link passes to the next person, who captions the drawing. The next person draws the caption, and so on.
- After six steps the whole chain plays back to the group as a 6-second GIF.
- No accounts. Static front end plus a tiny key-value backend, so it costs almost nothing per player.

**Why it scores high:**
- Invite-needed loop, borrowed rules (the Telephone/Gartic Phone family), high spectator value, failure comedy and emergent output.
- Gartic Phone needs everyone online at once. Doing it asynchronously in group chats removes that coordination cost.

**Risk:** the web channel has weak evidence for zero-ad 1M-DAU breakouts, and Gartic Phone owns the synchronous version.

**Why test it first anyway:** it is the cheapest way to **measure the k-factor directly**. Every chain link carries the sender's ID, so new players per active player per day is counted, not estimated.

**Cheapest demand test (about 1 week, ~$10 hosting):**
1. Build the 6-step chain and GIF playback.
2. Seed it in 10 of your own group chats and 3 relevant subreddits.
3. Measure the share rate and D7 from the link graph. **Pass** if new players per active player per day is at least 0.33 with D7 of at least 20%. **Kill** below 0.2.

### Recommended order
1. Run #3's one-week test first. It gives you a real, measured share rate on day 7.
2. Run #1's clip test in parallel.
3. Build whichever Roblox concept passes the clip and retention tests.
4. If one breaks out, follow the Grow a Garden pattern: bring in a live-ops partner for a minority stake, and plan the sequel before the decay sets in.

---

## 10. Limits, and what would change these conclusions

- **Coding bias:** one coder who knows the outcomes. Pre-registration and the objective watch-ratio test reduce this; they don't remove it.
- **Small sample:** 126 hand-coded games, so CIs are wide. The watch-ratio pass is narrow (lower bound 0.51).
- **Outcome tiers:** where DAU was never disclosed, tiers rest on press reports and creator claims. Heardle was moved up a tier after the Trends cross-check and its creator's figure of over 1M plays a day.
- **Google Trends:** it overweights web games people search for daily, it floors small values to zero, and it may understate play inside the Roblox app.
- **The Roblox random sample** can't see the top of the distribution: rate limits allow about 200 IDs a minute, and only about 1% of experiences are real attempts.
- **k-factors** come from search interest and press player counts, not install logs.
- **Still unknown:** Roblox revenue per DAU for a single experience (only platform averages are disclosed), and Wordle's exact price.
- **Channels not studied:** PC/Steam co-op hits (Lethal Company, R.E.P.O., Schedule I) are a streamer-driven channel too. They fall outside your web/mobile brief and outside the dataset.

## Sources

Every source, with its URL and type, is in the `sources` table (`data/export/sources.csv`). The ones relied on most:
- **Filings:** [NYT 10-K FY2021](https://www.sec.gov/Archives/edgar/data/71691/000007169122000006/nyt-20211226.htm) · [NYT Q1 2022 release](https://www.sec.gov/Archives/edgar/data/71691/000007169122000017/pressrelease3272022.htm) · [NYT 10-K FY2022](https://www.sec.gov/Archives/edgar/data/71691/000007169123000006/nyt-20221231.htm) · [NYT 10-K FY2025](https://www.sec.gov/Archives/edgar/data/71691/000007169126000011/nyt-20251231.htm) · [Zynga S-1/A](https://www.sec.gov/Archives/edgar/data/1439404/000119312511328051/d198836ds1a.htm) · [Zynga 10-Q Q1 2012](https://www.sec.gov/Archives/edgar/data/1439404/000119312512218465/d310790d10q.htm) · [Zynga 10-Q Q3 2012](https://www.sec.gov/Archives/edgar/data/1439404/000119312512437790/d429539d10q.htm) · [King F-1/A](https://www.sec.gov/Archives/edgar/data/1580732/000119312514113704/d564433df1a.htm) · [Roblox Q2 2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000261/q225shletterex992.htm) · [Q3 2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000326/ex991-q32025shareholderl.htm) · [Q4 2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000009/ex991-q42025shareholder.htm) · [Q2 2026](https://www.sec.gov/Archives/edgar/data/1315098/000162828026051059/ex991-robloxq22026earnin.htm) · [Roblox 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm) · [Rovio Annual Report 2017](https://www.rovio.com/wp-content/uploads/2024/12/rovio-annual-report-2017.pdf)
- **Creators:** [Wardle's share-button tweet](https://x.com/powerlanguish/status/1471493886031773707) · [Wardle at GDC (Game Developer)](https://www.gamedeveloper.com/marketing/josh-wardle-reflects-on-the-the-unconventional-road-to-wordle-s-success) · [Wardle at GDC (Thumbsticks)](https://www.thumbsticks.com/wardle-on-wordle-simple-word-game-global-phenomenon/) · [Nguyen in Rolling Stone](https://davidkushner.com/article/the-flight-of-the-birdman/) · [Jandel on Grow a Garden](https://gamesbeat.com/janzen-madsen-interview/)
- **Data:** Google Trends (pytrends; raw CSVs in `data/raw/trends`) · [Roblox games API](https://games.roblox.com/v1/games) · [Wordles of the World census](https://rwmpelstilzchen.gitlab.io/wordles/)
- **Press for gaps:** [Wordle player counts (AP/NYT)](https://www.boston.com/news/national-news/2022/01/04/he-made-wordle-for-his-partner-now-its-an-online-hit/) · [Wordle price (Reuters)](https://breakingnews.ie/world/rpt-update-1-new-york-times-acquires-wordle-1251694.html) · [Flappy Bird timeline (IBTimes)](https://www.ibtimes.com/flappy-bird-game-deleted-rise-fall-most-addictive-mobile-game-years-1555635) · [Flappy Bird clones (Engadget)](https://www.engadget.com/2014-03-06-report-app-store-averaged-a-new-flappy-bird-clone-every-24-minu.html) · [Among Us (GGRecon)](https://www.ggrecon.com/articles/how-memes-revived-a-two-year-old-indie-game/) · [Trivia Crack (Mobile Dev Memo)](https://mdm.co/trivia-crack-case-study-virality) · [Draw Something decline (MCV)](https://www.mcvuk.com/development/draw-something-popularity-in-steep-decline) · [Supercell kills (GWO)](https://gameworldobserver.com/2024/03/14/all-games-killed-by-supercell-everdale-hay-day-pop-clash-mini) · [Grow a Garden timeline (Wikipedia)](https://en.wikipedia.org/wiki/Grow_a_Garden) · [Steal a Brainrot 25M](https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players) · [Hamster Kombat decline](https://forklog.com/en/hamster-kombat-loses-nearly-260-million-players-post-listing/) · [Wizards Unite (Sensor Tower)](https://sensortower.com/blog/harry-potter-wizards-first-month) · [Heardle creator figure](https://liveforlivemusic.com/news/heardle-like-wordle-for-music) · [Quordle creator figure](https://money.yahoo.com/quordle-game-four-times-harder-203958412.html)
- **Research:** Lally et al. 2010 · Wood & Neal 2007 · Clark et al. 2009 · Kivetz et al. 2006 · Worchel et al. 1975 · Ryan et al. 2006 · Festinger 1954 (DOIs in `sources`)
