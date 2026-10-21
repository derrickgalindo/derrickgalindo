-- Viral casual games research database (SQLite)
PRAGMA foreign_keys = ON;

CREATE TABLE sources (
  source_id   TEXT PRIMARY KEY,
  title       TEXT NOT NULL,
  url         TEXT,
  publisher   TEXT,
  source_type TEXT CHECK (source_type IN ('primary_filing','primary_creator','primary_data','primary_company','secondary_press','secondary_reference','secondary_analysis')),
  pub_date    TEXT,
  notes       TEXT
);

CREATE TABLE games (
  game_id        TEXT PRIMARY KEY,
  name           TEXT NOT NULL,
  developer      TEXT,
  dev_type       TEXT CHECK (dev_type IN ('solo','small_indie','studio','major_publisher')),
  platform       TEXT,          -- launch platform: web, mobile, facebook, roblox, telegram, pc
  first_release  TEXT,          -- ISO date (month precision where noted)
  breakout_date  TEXT,          -- when it first reached mass scale (NULL if never)
  era            TEXT,          -- fb_social(2007-11), app_store_early(2008-12), app_store_mature(2013-19), web_io(2015-17), streamer(2018-22), daily_web(2021-), roblox_algo(2023-), telegram(2024)
  cohort         TEXT,          -- groups originals with their clones/contemporaries
  role           TEXT,          -- original_hit, clone, predecessor, contemporary, same_creator
  clone_of       TEXT REFERENCES games(game_id),
  outcome_tier   INTEGER CHECK (outcome_tier BETWEEN 0 AND 3), -- 0 flop, 1 modest, 2 hit (~1M DAU / US top-10), 3 mega (~10M DAU)
  outcome_basis  TEXT,
  peak_dau_m     REAL,          -- peak daily users in millions where a sourced number exists
  peak_ccu_m     REAL,
  confidence     TEXT CHECK (confidence IN ('high','medium','low'))
);

-- Every game coded on the same variables, coded from gameplay (observable) not outcome.
CREATE TABLE features (
  game_id            TEXT PRIMARY KEY REFERENCES games(game_id),
  session_min        REAL,    -- typical session length, minutes
  ttff_sec           REAL,    -- time from first open to first meaningful play
  one_input          INTEGER, -- 1 = single primary gesture (tap / swipe / type a word)
  rules_preknown     INTEGER, -- 1 = core rules borrowed from a culturally known game (Scrabble, Mastermind, Pictionary, charades, Mafia, trivia, Tetris-merge)
  share_artifact     INTEGER, -- 0 none, 1 player-made screenshot/score only, 2 product generates a shareable artifact or invite
  artifact_curiosity INTEGER, -- 1 = shared artifact is intriguing/comparable without revealing content (emoji grid)
  invite_needed      INTEGER, -- 1 = core loop needs a friend (async multiplayer, party)
  daily_sync         INTEGER, -- 1 = everyone gets the same content each day (common-knowledge event)
  scarcity           INTEGER, -- 1 = play is rationed (one per day, energy/lives, offline timers)
  social_graph       INTEGER, -- 0 none, 1 strangers/lobby, 2 real friends graph inside the product
  spectator          INTEGER, -- 0-2 how entertaining it is to watch someone else play
  failure_comedy     INTEGER, -- 1 = frequent funny/rage-inducing failure
  emergent_output    INTEGER, -- 1 = each play yields unique surprising/creative output
  free_to_play       INTEGER,
  monetization       TEXT,    -- none, ads, iap, ads+iap, premium, sub, crypto
  ip_licensed        INTEGER, -- 1 = major licensed IP / brand
  creator_audience   INTEGER, -- 0 none, 1 some, 2 large pre-existing audience/publisher network
  paid_ua            INTEGER, -- 1 = growth materially driven by paid acquisition / cross-promo
  platform_newness   INTEGER, -- 0 saturated, 1 maturing, 2 new or newly opened channel at breakout
  novelty            INTEGER  -- 0 clone/variant of a recent hit, 1 known form on new platform/new twist, 2 new form
);

-- How it actually broke out
CREATE TABLE breakouts (
  game_id            TEXT PRIMARY KEY REFERENCES games(game_id),
  latent_days        INTEGER, -- days from public release to breakout
  ignition_type      TEXT,    -- platform_feature, influencer, press, community_forum, diaspora_family, celebrity, algorithm, creator_audience, ip_fandom, paid_ua, incentive, unknown
  first_community    TEXT,
  influencer_timing  TEXT CHECK (influencer_timing IN ('before_growth','after_growth_began','none','unclear')),
  narrative          TEXT,
  source_ids         TEXT     -- comma-separated source_id list
);

-- Atomic sourced facts
CREATE TABLE facts (
  fact_id     INTEGER PRIMARY KEY AUTOINCREMENT,
  game_id     TEXT REFERENCES games(game_id),
  field       TEXT NOT NULL,
  value       TEXT NOT NULL,
  unit        TEXT,
  as_of       TEXT,
  source_id   TEXT REFERENCES sources(source_id),
  confidence  TEXT CHECK (confidence IN ('high','medium','low')),
  quote       TEXT
);

CREATE TABLE acquisitions (
  deal_id        TEXT PRIMARY KEY,
  acquirer       TEXT, target TEXT, game_id TEXT,
  deal_date      TEXT,
  price_usd_m    REAL,      -- NULL if undisclosed
  price_basis    TEXT,      -- disclosed_filing, disclosed_press, reported_estimate, undisclosed
  what_bought    TEXT,      -- audience, daily_habit, subscriber_funnel, ip, team, revenue, tech
  metrics_cited  TEXT,
  after_outcome  TEXT,
  source_ids     TEXT
);

CREATE TABLE monetization_benchmarks (
  bench_id     TEXT PRIMARY KEY,
  model        TEXT,  -- web_ads, mobile_ads, mobile_iap, subscription, roblox_devex, hybrid
  entity       TEXT,
  period       TEXT,
  arpdau_usd   REAL,  -- revenue (or bookings) per daily active user per day
  basis        TEXT,  -- how computed
  quality      TEXT CHECK (quality IN ('filing_derived','company_stated','third_party','assumption_range')),
  source_ids   TEXT
);

CREATE TABLE base_rates (
  rate_id      TEXT PRIMARY KEY,
  population   TEXT, n INTEGER, threshold TEXT, k INTEGER, rate REAL, method TEXT, source_ids TEXT
);

CREATE TABLE trends_series (
  game_id TEXT, kind TEXT, date TEXT, term TEXT, value REAL,
  PRIMARY KEY (game_id, kind, date, term)
);

CREATE TABLE trends_metrics (
  game_id TEXT PRIMARY KEY REFERENCES games(game_id),
  term TEXT, topic TEXT,
  peak_date TEXT,
  peak_sudoku_units REAL,      -- peak weekly search interest / mean 'sudoku' interest in same window
  weeks_to_peak_from_first_signal INTEGER,
  early_momentum REAL,         -- log ratio of weeks 5-8 vs 1-4 after first non-zero signal
  growth_rate_wk REAL,         -- fitted exponential growth rate in the rise phase (per week)
  doubling_days REAL,
  half_life_weeks REAL,        -- weeks for interest to fall to 50% of peak
  retained_share_52w REAL      -- interest 52 weeks after peak / peak
);

CREATE TABLE k_factor_estimates (
  game_id TEXT, method TEXT, window TEXT, growth_rate_per_day REAL,
  generation_days_low REAL, generation_days_high REAL, k_low REAL, k_high REAL, notes TEXT
);

CREATE TABLE concepts (
  concept_id INTEGER PRIMARY KEY, name TEXT, platform TEXT, pitch TEXT,
  model_score REAL, rank INTEGER, notes TEXT
);
