# DAL @ PHI, MNF Oct 26 2026: SGP report

Snapshot about 6:30 PM ET. The 90-minute inactives list was not out yet; Barkley-active and
Barkley-inactive runs give the same conclusions. Re-run `run.py` after updating prices.

## Verdict

**No 2-4 leg SGP built on my own data edges clears the pass threshold. Default: pass.**
Three correlation-only SGPs clear it **only if the app shows at least the minimum price below**.
Those prices come from a picks article, and I could not verify them.

## 1. Raw data

**Inactives/injuries.** PHI: QB Jalen Hurts IR (blood clots), Tanner McKee's 2nd start. WR DeVonta
Smith OUT, WR Dontayvion Wicks OUT (31.8% + 9.1% of wk-6 targets; 39% season). Barkley Q
(hamstring, full practice Sat, "trending to play"; left 2 of his 4 games early). RBs Shipley and
Bigsby IR; Carson Steele not on the active roster; Elijah Mitchell is RB3. OLB Nolan Smith OUT,
CB Michael Carter II (nickel) OUT, OLB Greenard Q (DNP). Lane Johnson retired; Dickerson activated.
DAL: WR Turpin OUT, LB Winters OUT, OT Shelton OUT; LB Overshown and CB Durant back.

**Team profile (nflverse pbp, weeks 1-6, rank of 32)**

| | DAL off | PHI off | DAL def | PHI def |
|---|---|---|---|---|
| EPA/play | +0.078 (8) | -0.135 (31) | +0.164 (32) | +0.078 (27) |
| Success | 46.8% (9) | 36.5% (30) | 49.3% (32) | 44.7% (22) |
| Pass EPA | +0.125 (9) | -0.127 (28) | +0.331 (32) | +0.116 (25) |
| Rush EPA | -0.020 (13) | -0.147 (28) | -0.007 (25) | +0.030 (27) |
| Neutral PROE | +3.0 (6) | -0.1 | | |
| Neutral sec/play | 30.6 (2nd fastest) | 32.6 (8th) | | |
| Pts/drive | 2.72 (4) | 1.65 (30) | | |
| RZ TD rate | 75% (3) | 68% (8) | | |
| YPA / comp% | 6.4 / 63.7% | 5.3 / 53.2% | allows 7.6 / 65.6% | allows 6.7 / 57.7% |
| Sack / INT rate | 2.6% / 2.0% | 7.0% / 1.9% | forces 3.9% / 0.5% | forces 3.3% / 1.3% |

McKee wk 6: 26/45, 215 yds, 0 INT, 73% neutral pass rate (PROE +10). DAL wk 5-6 pass EPA fell
to -0.118 (from +0.279 wk 1-4).

**Usage.** Lamb 29.2% targets, 35.9% air yards, 31.6% RZ targets, 8 end-zone targets (24.5% share in
wk 5-6 as Pickens rose to 24.5%). Javonte Williams 77% of carries, **15/15 carries inside the 5,
17/18 inside the 10**, 8 TDs in 6 games. PHI role changes: Smith/Wicks' 39% of targets go to Goedert
(18% wk 6 with both playing), Lemon (14%), Cooper (61% snaps, 17.4 YPR), Hollywood Brown and Moore.
Route participation isn't published for 2026, so target and snap share stand in for routes.

**Weather (Open-Meteo, NWS).** 59°F at kickoff, falling to 55°F; wind 5 mph, gusts 11; clear, 0%
precip. No adjustment.

**Referee Alex Kemp (2023-26, 52 games).** Avg total 43.8 vs closing 44.6 (-0.8; league +1.0);
over 44% (league 50.5%); 13.0 accepted penalties/g (league 12.6). Within noise (SE about 7 pts on the over
rate), so I made no adjustment.

**Lines.** Spread DAL -4.5: BetMGM -102/-108, DraftKings -105/-115, FanDuel -108/-112, bet365
-108/-112; Caesars and Fanatics -4 -109/-110. Total 43.5: o -112 to -120 (BetMGM 44 -108/-110).
ML DAL -205 to -235 / PHI +170 to +190. Kalshi: DAL -4.5 0.485, o43.5 0.515, DAL win 0.675, full
spread/total/team-total and prop ladders. Polymarket props via Yardbarker. **Pinnacle and Circa
were not reachable from this environment** (Pinnacle's API needs a key; Circa has no public feed),
so Kalshi is the sharp reference.

## 2. Leg pricing

Fair = power-method devig per book, averaged, blended 50/50 with Kalshi (75/25 for one-sided TD
prices). Only three legs get a probability other than the market's, each with a stated source:

| Leg | Market fair | Mine | Best price | EV straight | Source |
|---|---|---|---|---|---|
| McKee U0.5 INT | 0.440 | 0.490 | +120 bet365 | **+7.8%** | DAL D forces 0.5% INT and 3.9% sacks (bottom of league); McKee 0 INT in ~100 career att; shrunk hard to 2.0%/att over ~34 att |
| Javonte Williams ATD | 0.574 | 0.610 | -160 BetMGM/DK | -0.9% | goal-line monopoly; E[DAL rush TD] ~1.0 x 88% share |
| Dak U278.5 pass yds | 0.532 | 0.545 | -113 Caesars | +2.7% | weak: exchanges (0.55-0.565) and my sim (0.54) sit under books |

The raw sim runs hot on PHI passing (McKee median ~235 vs market ~200; Goedert O48.5 at 0.67).
That comes from my pass-volume assumptions (one McKee start, 45 att) and I could not source it,
so it is **not** counted as an edge.

## 3. Joint model

- Play-by-play Monte Carlo, 30,000 games. Script-driven play calling, plus per-game efficiency,
  pace and play-calling shocks shared across every leg in the game.
- Calibration. The raw sim had median margin DAL +6 and median total 43 (P(DAL -4.5) 0.538 vs
  market 0.49) and under-weights margins of 3. After raking to the Kalshi margin and total
  ladders: **median margin DAL +4, median total 44, P(DAL -4.5) 0.490, P(o43.5) 0.515,
  P(DAL win) 0.678**, matching the market. Effective sample size 24,578 of 30,000.
- Correlation check against 2023-25 game logs. WR receptions vs yards: rank correlation 0.75;
  empirical joint hit rate 0.414 vs the sim's 0.392 at similar marginals. QB attempts vs yards:
  rank correlation 0.62; the sim slightly **understates** it (normalized joint 0.63 vs 0.72).
  The sim's correlations are realistic to conservative.
- 7,568 combos (2, 3 and 4 legs) from 22 legs. The base case assumes the book prices correlation
  the way the sim does, with a 5% SGP margin per leg.

**Result: 0 combos reach EV >= 5% while staying +EV at half the edge.** Best data-driven combo:
Williams ATD + McKee U0.5 INT, hit 28.4%, fair +252. At an estimated book price of +280 it's +8.0%
EV, but -0.7% at half the edge. The two legs are slightly *negatively* correlated (a clean McKee
game means fewer DAL short fields), so a book that ignores correlation pays only about +245, which
is -2%.

## 4. Red team

- **Spread.** Opened PHI -3 (look-ahead); now DAL -4.5, a 7.5-point move. About 3-4 points is
  Hurts to McKee, about 1 is Smith/Wicks, and the rest is PHI's 4-game slide and Barkley's
  uncertainty. In the last 24h, Kalshi DAL -4.5 went 0.51 to 0.48 while DAL ML went 0.66 to 0.68,
  and DraftKings moved PHI +4.5 to -115. Money expects a narrower Dallas win (mass on DAL by 1-4).
  Splits: 84% of ML tickets on DAL; spread 46% tickets / 65% money on DAL. The book may know how
  much of Barkley they'll actually get. No side edge.
- **Total.** The over is juiced at most books. Kalshi o43.5 went 0.53 to 0.515 in 24h, against
  58% tickets / 61% money on the over. Two fast-paced offenses and the league's worst defense
  push it up; PHI's 31st-ranked offense pushes it down. Fair as is.
- **McKee INT under.** Books shade the INT side (-128 to -159) on backup-QB priors, PHI's patched
  OL and a likely trailing script. What they may know that I don't: DAL just added Mike Pettine
  to the defensive staff, and Durant/Overshown return to coverage. Defensive INT rates barely
  persist year to year, which is why I shrank DAL's 0.5% toward 1.55%. The edge holds only at +120;
  at +112 or worse it fails the half-edge test.
- **Williams TD.** Books -160 to -180; Kalshi 0.59 to 0.58. Possible reasons: DAL's last two
  games produced only 29 points, and PHI's run D is better at the point of contact (7th in yards
  before contact) than its EPA rank suggests. My 0.61 doesn't clear -160.
- **Lamb yards + receptions SGP.** The main receptions line is 7.5 at some books, while bet365
  has o6.5 at -200. Books' marginals sit above Kalshi's, so using Kalshi is conservative. PHI's
  nickel corner Carter II is out, which favors Lamb. Risk: Pickens pulled level with him on
  targets in weeks 5-6.
- **McKee yards.** Kalshi 200+ went 0.47 to 0.51 while 34+ attempts went 0.515 to 0.48. The
  market expects better efficiency on fewer throws, which is consistent with Barkley playing.

## 5. Top 3 parlays (ranked by EV at the quoted price)

These quotes come from TheLines (Oct 26, capture time unknown). **Verify each in the app.** Pass
threshold: EV >= +5% at the clickable price AND still > 0 with half the correlation lift, AND
joint probability >= 5%.

| # | Legs | Quoted price / book | Fair odds | Sim hit | EV at quote | EV, half corr. | Min price to bet | Biggest risk |
|---|---|---|---|---|---|---|---|---|
| 1 | Lamb 81+ rec yds + Lamb o6.5 rec | +221 DraftKings | +154 | 39.4% | **+26.5%** | +5.1% | **+205** | the quote is stale or misreported; Lamb's share dipped to 24.5% in wk 5-6 |
| 2 | DAL -4.5 + Under 44.5 + DAL 1H -3.5 | +594 FanDuel | +468 | 17.6% | +22.1% | +0.8% | **+590** | 24h money drifted toward PHI +4.5; FD's 1H line may be -3, not -3.5 |
| 3 | Dak 270+ pass yds + Dak 38+ att | +285 DraftKings | +243 | 29.2% | +12.3% | -3.2% | **+298** (fails at +285) | a DAL lead cuts Dak's volume; 2 INTs in each of his last 2 games |

**Stake:** quarter-Kelly capped at 1% of bankroll. All three hit the cap at their quoted prices
(#1 quarter-Kelly 3.0%, so 1%). Given that the prices are unverified, bet #1 only, at 1% or less,
and only at +205 or better.

**Straight-bet alternative (fewest legs = least vig):** McKee U0.5 INT at bet365 **+120** is +7.8%
EV and +2.3% at half the edge, so it clears the same threshold. Quarter-Kelly is 1.6%, capped at
**1%**. At +112 (DraftKings) or worse, pass.

## Correlation shopping list (fair price; bet only at or above "min")

| Legs | Sim hit | Fair | Min (+5% EV) |
|---|---|---|---|
| DAL -4.5 + J. Williams ATD + J. Williams o16.5 rush att | 29.2% | +242 | +259 |
| DAL -4.5 + J. Williams o16.5 att + McKee U1.5 pass TD | 29.2% | +242 | +259 |
| Over 43.5 + Dak o1.5 pass TD + Lamb ATD | 22.5% | +344 | +366 |
| Under 43.5 + McKee U205.5 pass yds + McKee U1.5 pass TD | 28.6% | +250 | +268 |
| Dak o1.5 pass TD + Lamb o80.5 rec yds + Lamb ATD | 20.3% | +393 | +418 |
