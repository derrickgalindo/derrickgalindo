# Pre-registration: viral-potential model and novel-signal tests

Written 2026-10-21, before any held-out evaluation was run. The git history of this file is the timestamp.

## Outcome
`hit` = `outcome_tier >= 2`. In plain terms: the game reached roughly 1M+ daily players or a US top-10 overall chart position.
Tiers are hand-coded from sourced metrics where those exist and cross-checked against Google Trends peak size.

## Exclusions from the main model
- Telegram tap-to-earn games. Their growth was bought with token-airdrop incentives, which is not a design feature. They are reported separately.
- Census Wordle-likes, which are template-coded. They are used only in a robustness run.

## Feature sets
- **Conventional ("why X went viral" listicle) set:** one_input, short session (<= 5 min), fast first fun (<= 10 s), free,
  in-product share artifact, daily/scarcity hook, real-friends social graph, invite-needed loop.
- **Context set:** creator_audience >= 1, licensed IP, paid UA, platform/channel newness == 2, novelty >= 1.
- **Novel candidates, fixed in advance:**
  - N1 `rules_preknown`: rules borrowed from a culturally known analog game.
  - N2 `spectator == 2`: highly watchable, so streamers carry it.
  - N3 `failure_comedy`: frequent funny or rage-inducing failure.
  - N4 `emergent_output`: every play makes something unique.
  - N5 `artifact_curiosity`: the share artifact is intriguing without spoiling the content.
  - N6 `early_momentum` (Trends, operational): the log ratio of absolute search interest in weeks 5-8 vs weeks 1-4 after the game first
    crosses a fixed absolute threshold (0.02 sudoku-units). The threshold is absolute, so the measure does not depend on the eventual peak.

## Splits
- **A. Temporal holdout:** train on games released before 2016-01-01, test on games released 2016 or later.
- **B. Leave-one-cohort-out:** clones and originals never sit on both sides of a split.
- **C. Within-cohort pairwise ranking:** the share of (hit, non-hit) pairs inside the same cohort where the hit scores higher, out of fold.

## Decision rules
- Report test AUC with a bootstrap 95% CI. The model "works" only if the lower CI bound is above 0.5 on split A **and** pooled AUC on split B is above 0.6.
- A novel signal "holds" only if its held-out univariate AUC CI excludes 0.5 on split A, and adding it to the conventional
  model raises held-out AUC on both A and B.
- Whatever the result, the failures are listed game by game.

## Addendum 1 (2026-10-21, after a dry run on partial data, before any YouTube data was pulled)
The dry run showed that coded `spectator_high` passed. That variable was hand-coded by an analyst who knew the outcomes,
so I am adding an **objective proxy**, fixed before any data is pulled:
- **N2b `watch_ratio`** = (peak YouTube-search interest / mean 'sudoku' YouTube-search interest) ÷
  (peak web-search interest / mean 'sudoku' web-search interest), over the same window.
  Data: Google Trends `gprop=youtube` vs web. The ratio cancels raw popularity and measures how much a game is *watched*
  relative to how much it is *looked up*. Games from before 2008 are excluded, because YouTube search data is unreliable then.
- Test: held-out (2016+) univariate AUC, with a bootstrap CI that must exclude 0.5. Also report the all-games AUC and the
  Spearman correlation with hand-coded `spectator`.
