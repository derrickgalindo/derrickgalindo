# What to build: evidence from 126 casual games, their clones, SEC filings and search data

*Research for a solo-built game aiming at 1M daily players within 90 days, with no paid marketing. About a 15-minute read.
Everything here traces to `data/viral_games.db`. Run the scripts listed in the [README](../README.md) to regenerate any number.*

---

## The answer in five lines

1. **There is no stable recipe, and simplicity doesn't separate hits from flops.** A model of the textbook viral recipe, trained on 2008–2015 hits, ranks 2016–2025 games *worse than chance* (held-out AUC [[A_CONV]]). The recipe gets copied, the copies flop, and the next hits come from a different channel.
2. **What does hold out of sample: watchability, a channel with spare reach, and retention.** Hand-coded "spectator value" was the only pre-registered new signal to pass the held-out test. [[WATCH_SENTENCE]]
3. **The 1M-in-90-days target is reachable arithmetically, but only one channel produces it regularly now.** It needs a sustained ~8–9-day doubling from a 1,000-player seed. Roblox produced several zero-ad hits that cleared it in 2025: Grow a Garden went from ~1,000 concurrent players in April to 21.3M concurrent by day 87. Roblox takes 44% of its revenue through the Apple and Google stores, so this is a mobile channel.
4. **Business: build on Roblox and keep it. Sell a stake rather than the company, and only after revenue exists.** The buyers' record says audience-only exits pay about $0.5–1 per daily player (Wordle). Buying at the peak gets punished (Zynga wrote off 52% of the $183.1M it paid for OMGPOP within six months). Revenue businesses sell at about 3.5x revenue (Niantic games). 1M Roblox DAU is worth about $4.4M a year to the creator at the mid estimate, with zero hosting cost.
5. **Top three concepts:** *Hide as a Painting* (Roblox prop-hunt), *Pictionary Obby* (Roblox), and *Telephone Pictionary Chains* (web, group chat). Each can be demand-tested in under two weeks for under $100. The kill thresholds come from the DAU math.

---

## 1. What I added to your brief, and what it found

You asked what the best hit-making studios would research that you didn't ask for. I added eight items to the plan; seven produced the findings below (Apple's clone rule and Roblox's kids-privacy obligations went into the limitations).

| Added research | Finding |
|---|---|
| **DAU math and retention** (studios kill games over D1 retention, not virality) | From 1,000 seed players, 1M DAU on day 90 needs a sustained ~8–9-day doubling. Good retention cuts the sharing each active player must do by 3.3x and the total installs needed by 3.3x (§6). |
| **Which channels have spare reach in 2026** | Roblox's recommendation algorithm is the only channel in the data still producing frequent zero-ad breakouts. Daily web puzzles are saturated (NYT, LinkedIn, hundreds of clones). Organic mobile app-store breakouts are rare since paid acquisition took over (§3, §8). |
| **Time-to-clone and defensibility** | Clones arrive within days (300 Flappy Bird clones in 4 days). Followers beat originals often: 2048 over Threes, FarmVille over Farm Town, Mafia Wars over Mob Wars, Suika over Merge Big Watermelon (§3). |
| **Post-peak decay** | [[DECAY_SENTENCE]] Steal a Brainrot fell ~99% from peak. Draw Something lost 33% of its daily players in 30 days (§7). |
| **Cost to serve per player** | Static web and Roblox (which hosts for free) cost close to zero per player. LLM features cost money every time a player triggers one (§8). |
| **Studio kill rates** | Supercell: 30+ games killed, 5 hits. The skeptical base rates are in §7. |
| **2023–2026 data** | Roblox and Telegram breakouts are in the dataset. Without them the model would be fit to a vanished era. |

---

## 2. The dataset

`data/viral_games.db` (SQLite; CSV copies in `data/export/`):

- **126 hand-coded games:** 74 hits and 52 non-hits. They include the originals you named, 20–30 more viral casual games, and deliberately their **clones, predecessors, contemporaries and the same creators' follow-ups**, grouped into 17 cohorts.
- **~140 more Wordle-likes** from a public census (*Wordles of the World*). These are the failures that listicles never name.
- **The same 20 variables for every game:** session length, time to first fun, single input, borrowed rules, share artifact (and whether it intrigues without spoiling), invite loop, daily sync, scarcity, social graph, spectator value, failure comedy, emergent output, monetization, IP, creator audience, paid acquisition, channel newness and novelty.
- **How each documented hit broke out:** latent days, what triggered it, first community, and whether an influencer arrived before or after growth.
- **75 sources, typed.** Primary sources include SEC filings (NYT 10-Ks and 8-Ks, Zynga's S-1 and 10-Qs, King's F-1, Roblox's letters and 10-K), Rovio's 2017 annual report, creator statements (Wardle's GDC talk and tweet, Nguyen in Rolling Stone, Jandel on Grow a Garden), and raw data (Google Trends, the Roblox API, the census). Secondary press fills gaps and is labelled as such.
- **Google Trends series for [[N_TRENDS]] games** (weekly), plus daily windows for the case studies.

**Caveat:** I hand-coded the features and I know the outcomes. To limit the damage, the predictions were pre-registered and committed to git before testing (`model/PREREGISTRATION.md`), and the one signal that passed got an objective, data-pulled proxy (§5).

---

## 3. Your premise, stress-tested

**Hypothesis:** a repeatable recipe exists, with simplicity at its core.

**Simplicity does not discriminate.** 64 of 126 games are simple on all three counts (one input, sessions of 5 minutes or less, first fun within 10 seconds). Their hit rate is 67%, against 56% for the rest, and the simple non-hits are almost all clones (Absurdle, Dordle, Worldle, Splashy Fish, Swing Copters…). Among the non-simple hits are 35 of the biggest: Among Us, FarmVille, Pokémon GO, Draw Something, Grow a Garden. Simplicity is common to the whole category, so it can't be what separates the winners.

**The recipe inverts across eras.** Trained on pre-2016 games, the conventional model scores [[A_CONV]] AUC on 2016+ games, i.e. worse than a coin flip. With the 2021–25 Wordle-clone cohort removed it is still [[A_CONV_NODW]]. The features that marked the old hits (an in-product share artifact, instant first fun, a daily hook) are the features every clone copies. The new hits (Among Us, Fall Guys, Roblox games) have long sessions, lobbies and streamers.

**Timing and platform shifts did much of the work:**
- **Facebook cut app notifications in early 2010, and Zynga's DAU fell from 67M to 48M across 2010** with the same games (Zynga S-1: "These changes limited the level of communication among users… As a result, the number of our players on Facebook declined"). This is a natural experiment showing that the share channel, not the game, carried growth.
- **The same mechanics win or lose depending on the channel.** OMGPOP's *Draw My Thing* (web, 2008) went nowhere. The same idea on iPhone, *Draw Something* (2012), reached ~14M DAU. Niantic's *Ingress* reached a niche; the same mechanic plus Pokémon became *Pokémon GO*. With the IP held constant, *Harry Potter: Wizards Unite* earned ~$12M in its first month against Pokémon GO's ~$300M and shut down in 2022.
- In my coding, games on a channel that was new or newly opened at the time hit 87% of the time, against 41% on saturated channels.
- **Creators repeating their own recipe mostly failed.** No follow-up without paid or cross-promoted distribution became a hit (Swing Copters, Chess with Friends). Follow-ups that did hit had King's or Zynga's cross-promotion behind them.

**Influencers usually amplified growth that had already started.**
- Flappy Bird was US #1 on Jan 17 2014. PewDiePie's video went up **Jan 27**.
- John Mayer's "the new Twitter" tweet came after Words with Friends' founders saw growth inflecting.
- The genuine influencer-caused cases are recent, streamer-native games. Among Us sat in "low double digits" of players for most of its first year, until Korean and Brazilian streamers and then Sodapoppin (Jul 15 2020) took Twitch viewership from 460 to 53,000. Suika Game sat for 21 months until Japanese VTubers found it.

**Luck, in a form you can measure.** Zero-audience hits waited a **median of 78 days** before breaking out (range 3–778). They survived that wait because they cost nothing to run.

### Flappy Bird: what changed after months unnoticed
[[FLAPPY_PARAGRAPH]]

### Did Wordle's share grid cause the spread, or follow it?
[[WORDLE_PARAGRAPH]]

### Did Wordle sell for over $1 million?
**Yes, but the filings never state the price.** The NYT announced the price as "in the low seven figures" (Jan 31 2022, Reuters). The 10-K for FY2021 says only "In January 2022, we acquired Wordle". FY2022 cash flow shows $515.6M of acquisitions net of cash, almost all of it The Athletic (~$550M), so Wordle was immaterial. "Low seven figures" means at least $1.0M, with no exact figure ever disclosed. What the NYT got for it is in the filings: "Wordle brought an unprecedented tens of millions of new users to The Times… our best quarter ever for net subscriber additions to Games" (Q1 2022 8-K). Every 10-K since describes Wordle (and later Connections) as free content used "to generate large audiences… eventually converting them into subscribers".

---

## 4. The model and its held-out test

The pre-registered bar: held-out AUC CI above 0.5 on the temporal split **and** leave-one-cohort-out AUC above 0.6.

| Model | Temporal holdout (train <2016, test 2016+) | Leave-one-cohort-out | Hit outscores its own clones / contemporaries |
|---|---|---|---|
| Conventional recipe | [[T_conventional]] |
| Context only (audience, IP, paid, channel, novelty) | [[T_context_only]] |
| Conventional + context | [[T_conv_ctx]] |
| Full (+ novel candidates) | [[T_full]] |

**Verdict: every variant fails the pre-registered bar.** The model separates hits from flops moderately *within* an era (leave-one-cohort-out ~0.66–0.71) and ranks a hit above its own clones about 75% of the time. It cannot carry a recipe *across* eras.

**Where it fails:**
- **False positives:** almost all of them are 2022–25 Wordle-likes (LoLdle, Costcodle, Heardle, Worldle, Contexto, Travle, Semantle…), which scored 0.65–0.95.
- **False negatives:** Goose Goose Duck, Dead Rails, 99 Nights, Doors, Stumble Guys, Among Us, skribbl.io, Dress to Impress, Fall Guys and Grow a Garden scored 0.01–0.07.
- **Clone paradox:** 107 hit/non-hit pairs in the same cohort have identical recipe features (35 in one-tap, 33 in daily word). The model cannot tell Flappy Bird from Splashy Fish or Wordle from Lewdle, and nothing built from mechanics could.

---

## 5. A new signal: watchability

Pre-registered candidates and their held-out results:

| Candidate | Hit rate with / without | Held-out AUC | Adds to model on both splits? | Holds |
|---|---|---|---|---|
[[NOVEL_ROWS]]

- **Watchability (spectator value) is the one that holds.** Highly watchable games hit [[SPEC_RATES]]. It raises held-out AUC on both splits, and its CI excludes zero. Most "why X went viral" articles treat streamer pickup as luck. The data say it is a design property: streamers pick games that are fun to watch, and the recent pre-growth influencer cases (Among Us, Suika, Grow a Garden) all score high on it. Roblox's own filings list the metrics its recommender rewards: "qualified play-through rate, 7-day play days per user, and 7-day intentional co-play days". That is a design spec.
- **Objective check (pre-registered after the dry run):** [[WATCH_PARAGRAPH]]
- **The famous emoji share grid fails.** Games with an intriguing, spoiler-free share artifact hit [[CURIO_RATES]]: everyone copied the grid, and the copies flopped. The grid is not a growth engine you can rebuild.
- **Early momentum in Trends (the operational signal) is inconclusive:** [[EM_SENTENCE]]

---

## 6. Epidemiology: k-factors and the 90-day math

**Share-on-play growth:** every active player-day produces κ new installs, and the k-factor is R = κ × (expected active days per install). So retention multiplies virality.

| Retention (D1/D7/D30) | κ needed per active player-day | k-factor R | Installs needed by day 90 |
|---|---|---|---|
[[DAU_ROWS]]

To go from 1,000 to 1M daily players in 90 days takes a sustained doubling every **9.0 days** or faster (r ≥ 0.077/day). Observed rates:

| Game | Window | Doubling | k-factor if one share generation is 1–3 days (Wordle) or 1–4 days (Roblox) |
|---|---|---|---|
[[K_ROWS]]

These rates come from player counts and CCU, and the k ranges come from the fixed-generation approximation R = e^{r·Tg}. They include broadcast pushes (press, algorithms), so they are upper bounds on person-to-person spread. The reading: **real hits ran at k ≈ 1.1–1.6 per share generation, with very short generations.** Nobody needs k = 3. What matters is a short loop (play → share → friend plays within a day or two) combined with retention. A median-retention game needs every active player to bring in 0.68 new installs *per day*, which is implausible. A ritual-retention game needs 0.21.

---

## 7. Skeptical investing: the base rates a short seller would use

| Population | Failure rate |
|---|---|
[[BASE_ROWS]]

- **Peaks are worth less than they look.** [[DECAY_SENTENCE]]
  - Draw Something lost 33% of its daily players in 30 days.
  - Hamster Kombat lost 86% after its token airdrop.
  - Steal a Brainrot fell ~99% from its 25.4M concurrent peak.
  - HQ Trivia went from 2.38M concurrent players to shutdown in two years.
- **Buyers who bought the peak lost money.** Zynga paid $183.1M for OMGPOP on Mar 21 2012 and impaired $95.5M by Sep 30.
- **Durable exceptions are rituals.** [[RITUAL_SENTENCE]]

**Short thesis on any viral game:** unless it has a ritual loop or a live-ops machine, value it at about one year of peak-adjusted revenue.

**Behavioral science says why rituals last:**
- **Habits take a median of 66 days to form** (range 18–254; Lally et al. 2010), so the game has to survive about two months of repetition.
- **Habits attach to stable cues** (Wood & Neal 2007). The daily group-chat post is a cue.
- **Scarcity raises value** (Worchel et al. 1975). One puzzle per day is scarcity.
- **Near-misses sustain play** (Clark et al. 2009, *Neuron*). That is Flappy Bird's pipe.
- **Effort rises as a goal gets close** (goal gradient; Kivetz et al. 2006). That is Grow a Garden's growing plants.
- **Competence, autonomy and relatedness predict continued play** (Ryan, Rigby & Przybylski 2006).
- **Shared grids work by social comparison** (Festinger 1954).

Implication: design the loop so people come back (cue + scarcity + progress + a friend), not only so they post once.

---

## 8. Business model, with numbers

**Revenue per daily player per day, net to the developer:**

| Model | Low / mid / high | Per year at 1M DAU (mid) | Evidence |
|---|---|---|---|
| Web daily game, ads | $0.005 / $0.012 / $0.027 | $4.4M | Assumption from ad rates (RPM). Order-of-magnitude checks: Flappy Bird ~$0.005 (2014), Slither.io ~$0.01 (2016) |
| Mobile app, ads | $0.03 / $0.05 / $0.08 | $18.2M | Third-party benchmarks. Needs app-store reach that is now mostly bought: Rovio spent €69.6M on user acquisition in 2017, up from €6.3M in 2015, while its DAU fell from 13.5M to 9.2M |
| Mobile app, in-app purchases (net of 30% store fee) | $0.025 / $0.038 / $0.066 | $14.0M | King Q4'13 $0.055 gross; Rovio Q4'17 ~$0.094 gross (filings) |
| **Roblox (creator's DevEx share)** | $0.004 / $0.012 / $0.031 | $4.4M | Roblox bookings per DAU $0.138–0.141 × 22% DevEx share = $0.031 per *platform* DAU (Q2–Q3 2025 letters). Hosting is free |
| Subscription funnel | $0.001 / $0.005 / $0.010 | $1.8M | NYT single-product ARPU ≈ $3.5/month; 1–5% conversion assumed |

**What buyers paid for, and what they watched:**

| Deal | Price | What was bought | Result |
|---|---|---|---|
| NYT ← Wordle (2022) | Low 7 figures, ~$0.5–1 per daily player | Audience, daily habit, subscriber funnel | "Tens of millions of new users"; record Games subscriber adds |
| Zynga ← Newtoy / Words with Friends (2010) | $53.3M | Audience, mobile social graph, team | DAU doubled within ~120 days through Zynga cross-promotion |
| Zynga ← OMGPOP / Draw Something (2012) | $183.1M at the peak (~$13 per daily player) | Peak audience | 52% written off within six months |
| Activision ← King (2015) | $5.9B | Revenue, 474M MAU, live-ops machine | Still a top franchise |
| Scopely ← Niantic games (2025) | $3.5B (>$1B revenue, ~3.5x) | Revenue, licensed IP | — |
| Scopely ← Stumble Guys; Spotify ← Heardle; Merriam-Webster ← Quordle | Undisclosed | DAU (20M for Stumble Guys) and funnels | Spotify shut Heardle down within a year |
| Splitting Point ← ~50% of Grow a Garden (Apr 2025) | Undisclosed stake at ~1,000 concurrent players | Early habit plus live-ops and reach | 22M concurrent ten weeks later |

The metrics in these filings were DAU, MAU, unique payers, bookings per DAU (Zynga's ABPU, King's payer bookings, Roblox's ABPDAU), revenue concentration (Candy Crush was 78% of King's bookings), user-acquisition payback (Rovio: 8–10 months), and conversion to subscribers (NYT).

**Recommendation: build on Roblox, which is effectively mobile, and keep it.**
- **Odds:** Roblox is the only channel in the data still producing zero-ad 1M+ DAU breakouts several times a year. Its recommender rewards the retention and co-play signals that held up out of sample.
- **Economics:** 1M DAU is worth about $4.4M a year to the creator at the mid estimate (range $1.5–11M), at zero hosting cost.
- **Mobile apps** pay 3–4x more per player, but organic reach is the problem, and that is exactly the constraint you set.
- **Web daily puzzles** have the only proven buyer pool (NYT, Merriam-Webster, Spotify), but they pay audience prices (~$1M) and the category is saturated.
- **Sell or keep:** keep while it earns. Kept, it is worth about $5.9M over five years if it fades like a typical hit (30% a year) and $7.6M if it holds like a ritual. A sale beats keeping only at revenue multiples of 2–3.5x, which buyers pay for proven, decaying-slowly revenue, not for spikes.
- **The Grow a Garden lesson:** if it ignites, sell a minority stake to an established Roblox studio for live-ops capacity and reach. Don't sell the whole thing.
- **Risks:** platform dependence (DevEx rate, algorithm changes; Roblox's own Q2 2026 letter says a recommender change shifted its revenue mix), a young audience (COPPA), and fast decay.

---

## 9. The three concepts

20 concepts were coded on the same variables and scored by the models (full table: `analysis/concepts.md`).

[[CONCEPT_SECTION]]

---

## 10. What would change these conclusions, and the limits

- **Coding bias:** one coder who knows the outcomes. Pre-registration and the objective watch-ratio test limit this but don't remove it.
- **Small sample:** 126 games. AUC confidence intervals are wide, so treat point estimates as directional.
- **Outcome tiers** for games with no disclosed DAU lean on press reports and on Google Trends, which overweights web games people search for every day.
- **The Roblox census** couldn't measure the top of the distribution (rate limits allow about 200 IDs a minute; only about 1% of experiences are real attempts). Roblox base rates come from its 10-K denominator instead.
- **k-factors** come from search interest and press player counts, not install logs, and are upper bounds on person-to-person spread.
- **Still unknown:** Roblox revenue per DAU for a single experience (only platform averages are disclosed), and Wordle's exact price.

## Sources

Every source, with its URL and type, is in the `sources` table (`data/export/sources.csv`). The ones most relied on:
- **Filings:** [NYT 10-K FY2021](https://www.sec.gov/Archives/edgar/data/71691/000007169122000006/nyt-20211226.htm), [NYT Q1 2022 release](https://www.sec.gov/Archives/edgar/data/71691/000007169122000017/pressrelease3272022.htm), [NYT 10-K FY2022](https://www.sec.gov/Archives/edgar/data/71691/000007169123000006/nyt-20221231.htm), [NYT 10-K FY2025](https://www.sec.gov/Archives/edgar/data/71691/000007169126000011/nyt-20251231.htm), [Zynga S-1/A](https://www.sec.gov/Archives/edgar/data/1439404/000119312511328051/d198836ds1a.htm), [Zynga 10-Q Q1 2012](https://www.sec.gov/Archives/edgar/data/1439404/000119312512218465/d310790d10q.htm), [Zynga 10-Q Q3 2012](https://www.sec.gov/Archives/edgar/data/1439404/000119312512437790/d429539d10q.htm), [King F-1/A](https://www.sec.gov/Archives/edgar/data/1580732/000119312514113704/d564433df1a.htm), [Roblox Q2 2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000261/q225shletterex992.htm), [Q3 2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000326/ex991-q32025shareholderl.htm), [Q4 2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000009/ex991-q42025shareholder.htm), [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm), [Rovio Annual Report 2017](https://www.rovio.com/wp-content/uploads/2024/12/rovio-annual-report-2017.pdf).
- **Creators:** [Wardle's share-button tweet](https://x.com/powerlanguish/status/1471493886031773707), [Wardle at GDC (Game Developer)](https://www.gamedeveloper.com/marketing/josh-wardle-reflects-on-the-the-unconventional-road-to-wordle-s-success), [Wardle at GDC (Thumbsticks)](https://www.thumbsticks.com/wardle-on-wordle-simple-word-game-global-phenomenon/), [Nguyen in Rolling Stone](https://davidkushner.com/article/the-flight-of-the-birdman/), [Jandel on Grow a Garden](https://gamesbeat.com/janzen-madsen-interview/).
- **Data:** Google Trends (pulled via pytrends), the [Roblox games API](https://games.roblox.com/v1/games), and the [Wordles of the World census](https://rwmpelstilzchen.gitlab.io/wordles/).
- **Press for gaps:** [Wordle player counts (AP/NYT)](https://www.boston.com/news/national-news/2022/01/04/he-made-wordle-for-his-partner-now-its-an-online-hit/), [Wordle price (Reuters)](https://breakingnews.ie/world/rpt-update-1-new-york-times-acquires-wordle-1251694.html), [Flappy Bird timeline (IBTimes)](https://www.ibtimes.com/flappy-bird-game-deleted-rise-fall-most-addictive-mobile-game-years-1555635), [Among Us (GGRecon)](https://www.ggrecon.com/articles/how-memes-revived-a-two-year-old-indie-game/), [Trivia Crack (Mobile Dev Memo)](https://mdm.co/trivia-crack-case-study-virality), [Draw Something decline (MCV)](https://www.mcvuk.com/development/draw-something-popularity-in-steep-decline), [Flappy Bird clones (Engadget)](https://www.engadget.com/2014-03-06-report-app-store-averaged-a-new-flappy-bird-clone-every-24-minu.html), [Supercell kills (GWO)](https://gameworldobserver.com/2024/03/14/all-games-killed-by-supercell-everdale-hay-day-pop-clash-mini), [Grow a Garden (Wikipedia, with cited timeline)](https://en.wikipedia.org/wiki/Grow_a_Garden), [Steal a Brainrot 25M CCU](https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players), [Hamster Kombat decline](https://forklog.com/en/hamster-kombat-loses-nearly-260-million-players-post-listing/), [Wizards Unite (Sensor Tower)](https://sensortower.com/blog/harry-potter-wizards-first-month).
- **Research:** Lally et al. 2010; Wood & Neal 2007; Clark et al. 2009; Kivetz et al. 2006; Worchel et al. 1975; Ryan et al. 2006; Festinger 1954. DOIs are in `sources`.
