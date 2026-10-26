# nfl-sgp: same-game parlay EV finder

Finds the same-game parlay (2-4 legs) with the highest expected value after the book's
margin, or tells you to pass. It works from raw data, not picks articles:

1. **Data** (`sgp/data.py`): nflverse play-by-play, weekly player stats, snap counts,
   injuries, schedules (lines, referee), officials, via `nflreadpy` (the maintained successor
   to `nfl_data_py`, which no longer installs on Python 3.12+). Team EPA/play, success rate,
   neutral pace, pass rate over expected, red-zone TD rate; player target/air-yard/carry
   share, red-zone and inside-10 work; referee crew history.
2. **Simulator** (`sgp/sim.py`): play-by-play Monte Carlo of the whole game. Score and clock
   drive play calling (trailing teams pass and hurry, leading teams run), and each simulated
   game draws one efficiency shock per offense plus a pace shock. Every leg comes from the
   same simulated game, so correlation comes out of the game script; it isn't bolted on.
3. **Calibration** (`sgp/calibrate.py`, `sgp/reweight.py`): fit each offense's efficiency knob
   to the market-implied team means, then rake (iterative proportional fitting) the simulated
   games so the margin and total distributions match the exchange ladders at every line.
   The run prints the median margin/total and the effective sample size after raking.
4. **Pricing** (`sgp/markets.py`, `sgp/price.py`): power-method devig per book, blended with
   Kalshi mids. A leg gets a probability different from the market's only if `legs.py` names
   the edge source (`mine` + `source`). Joint probabilities use the simulation's empirical
   copula with each leg's marginal pinned to that probability. Every 2/3/4-leg combo is
   priced three ways: the book prices correlation like the sim (base case), the book prices half
   of it, and the ceiling (independent product of one book's leg prices).
5. **Output** (`run.py`): leg table, combos ranked by EV, a correlation shopping list (fair and
   minimum acceptable price), quoted SGPs checked against the sim, quarter-Kelly (1% cap).

## Run it

```bash
python -m venv venv && ./venv/bin/pip install nflreadpy pandas numpy pyarrow requests
./venv/bin/python run.py games/2026_07_DAL_PHI --sims 30000
BARKLEY_ACTIVE=0 ./venv/bin/python run.py games/2026_07_DAL_PHI   # inactive scenario
```

About 70 s for 30k games. Writes `results.json` and `combos.csv` into the game folder.

## A new game

Copy `games/2026_07_DAL_PHI/` and edit:

- `teams.py`: one builder per team returning `sim.Team` (pass rate, pace, sack/INT rates, and
  `Receiver`/`Rusher` shares). Pull the numbers with `sgp.data.team_profile` and
  `sgp.data.player_usage`, then move shares for injuries. Expose `HOME, AWAY`.
- `legs.py`: `LEGS` (prices per book, Kalshi fair, optional `mine` + `source`),
  `MARGIN_LADDER` and `TOTAL_LADDER` (Kalshi `KXNFLSPREAD` / `KXNFLTOTAL` mids,
  `sgp.markets.kalshi_ladder` pulls them), `TARGET_MEANS` (`sgp.calibrate.mean_from_ladder`
  on the `KXNFLTEAMTOTAL` ladders), `SGP_QUOTES` (any real SGP prices you see), `FAV, DOG,
  SPREAD, TOTAL, POOL`.

## Limits

- Sportsbook SGP prices are generated per bet slip, and there's no public feed for them, so
  each combo's EV uses an estimated book price. Use `min_price_am`: bet only if the app shows
  at least that.
- The raw (unraked) sim does not reproduce key-number mass at 3 well (~7% vs ~15% in the
  NFL); raking fixes the margin distribution, but per-play logic is still simplified (no
  timeouts, simplified OT, generic penalties).
- Route-level participation data isn't published for the current season, so usage uses
  targets and snap share in place of routes run.
