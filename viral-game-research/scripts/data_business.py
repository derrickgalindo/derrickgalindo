"""Acquisitions, monetization benchmarks and extra sources for the business-model analysis."""

EXTRA_SOURCES = [
    ("rovio_ar2017", "Rovio Entertainment Annual Report 2017 (Games KPIs, user acquisition spend)", "https://www.rovio.com/wp-content/uploads/2024/12/rovio-annual-report-2017.pdf", "Rovio", "primary_company", "2018-03", "Games DAU 13.5M (Q2'16) -> 9.2M (Q4'17); ARPDAU EUR0.03 -> 0.08; UA spend EUR6.3M (2015), 18.2M (2016), 69.6M (2017); UA payback 8-10 months"),
    ("rovio_ipo_announce", "Rovio announces intention to launch IPO (GlobeNewswire)", "https://www.globenewswire.com/news-release/2017/09/05/1107039/0/en/Rovio-announces-its-intention-to-launch-an-initial-public-offering-and-listing-on-the-official-list-of-Nasdaq-Helsinki-Ltd.html", "Rovio", "primary_company", "2017-09-05", "3.7B lifetime downloads; 80M MAU and ~11M DAU Q2 2017"),
    ("tc_activision_king", "Activision Blizzard acquires King for $5.9B (TechCrunch)", "https://techcrunch.com/2015/11/02/activision-blizzard-acquires-candy-crush-maker-king-digital-entertainment-for-5-9-billion", "TechCrunch", "secondary_press", "2015-11-02", "$18/share, EV $5.0B; 474M MAU Q3 2015"),
    ("vgc_taketwo_zynga", "Take-Two announces acquisition of Zynga for $12.7bn (VGC)", "https://videogameschronicle.com/news/take-two-announces-acquisition-of-mobile-games-giant-zynga-for-12-7bn", "VGC", "secondary_press", "2022-01-10", "64% premium; mobile to be >50% of net bookings"),
    ("gematsu_scopely_niantic", "Scopely to acquire Niantic games business (Gematsu)", "https://www.gematsu.com/2025/03/scopely-to-acquire-niantic-games-business", "Gematsu", "secondary_press", "2025-03-12", "$3.5B; >30M MAU; >$1B revenue 2024"),
]

ACQUISITIONS = [
    # deal_id, acquirer, target, game_id, date, price_usd_m, price_basis, what_bought, metrics_cited, after_outcome, source_ids
    ("nyt_wordle", "The New York Times Co.", "Wordle (Josh Wardle)", "wordle", "2022-01-31", 1.0, "disclosed_press: 'low seven figures' (>= $1M; exact figure never disclosed, immaterial in 10-K)",
     "audience + daily habit + subscriber funnel", "Players (~2M daily mid-Jan 2022); free daily ritual; brand fit with Crossword/Spelling Bee",
     "Q1 2022: 'tens of millions of new users', best quarter ever for Games net subscriber adds; Wordle and Connections kept free as funnel through FY2025 10-K",
     "nyt_10k_2021,nyt_q1_2022_pr,nyt_10k_2022,nyt_10k_2025,wordle_nyt_lowseven"),
    ("zynga_newtoy", "Zynga", "Newtoy (Words with Friends)", "wordswithfriends", "2010-11", 53.3, "disclosed_filing (S-1): $44.3M cash + $8.9M stock",
     "audience + mobile social graph + team", "DAU; leading word game on iPhone",
     "Zynga doubled WWF DAU within ~120 days via cross-promotion; became a pillar mobile franchise", "zynga_s1"),
    ("zynga_omgpop", "Zynga", "OMGPOP (Draw Something)", "drawsomething", "2012-03-21", 183.1, "disclosed_filing (10-Q)",
     "audience at peak + mobile growth", "Downloads (50M in ~50 days) and DAU at peak",
     "Draw Something DAU fell ~33% within a month; $95.5M impairment in Q3 2012 (52% of price) six months later", "zynga_10q_2012q1,zynga_10q_2012q3,mcv_drawsomething_decline"),
    ("activision_king", "Activision Blizzard", "King Digital Entertainment", "candycrush", "2015-11-02", 5900.0, "disclosed_press ($18/share equity value; EV $5.0B)",
     "revenue + audience + live-ops machine", "474M MAU (Q3 2015), gross bookings, payer counts",
     "Candy Crush still a top-grossing franchise a decade later", "tc_activision_king,king_f1"),
    ("taketwo_zynga", "Take-Two Interactive", "Zynga", None, "2022-01-10", 12700.0, "disclosed_press",
     "mobile revenue + live-ops portfolio", "Net bookings, mobile share of bookings", "Closed May 2022", "vgc_taketwo_zynga"),
    ("scopely_niantic", "Scopely (Savvy Games)", "Niantic games business (Pokemon GO)", "pokemongo", "2025-03-12", 3500.0, "disclosed_press",
     "revenue + IP-licensed live game", ">30M MAU; >$1B 2024 revenue", None, "gematsu_scopely_niantic"),
    ("scopely_stumble", "Scopely", "Stumble Guys (Kitka Games)", "stumbleguys", "2022-09-08", None, "undisclosed",
     "audience (DAU) for a viral clone", "20M DAU; 160M downloads; $21M lifetime revenue by Jul 2022", None, "scopely_stumble"),
    ("spotify_heardle", "Spotify", "Heardle", "heardle", "2022-07", None, "undisclosed",
     "audience + funnel into music discovery", "Daily players", "Spotify shut Heardle down in May 2023", "spotify_heardle"),
    ("mw_quordle", "Merriam-Webster (Britannica)", "Quordle", "quordle", "2023-01-23", None, "undisclosed",
     "daily habit + funnel into dictionary site", "Daily players", None, "mw_quordle"),
    ("sp_growagarden", "Splitting Point Studios (Jandel)", "~50% of Grow a Garden", "growagarden", "2025-04", None, "undisclosed (equity stake at ~500-1,000 CCU)",
     "early daily habit + live-ops capacity + creator audience", "CCU and retention at tiny scale", "Grew to 21-22M CCU within ~10 weeks", "gamesbeat_jandel,wiki_grow_a_garden"),
]

# Revenue (bookings) per daily active user per day.
BENCHMARKS = [
    # bench_id, model, entity, period, arpdau_usd, basis, quality, source_ids
    ("zynga_2010", "facebook_iap", "Zynga (all games)", "2010", 0.041, "ABPU as reported (avg daily bookings / avg DAU)", "filing_derived", "zynga_s1"),
    ("zynga_9m2011", "facebook_iap", "Zynga (all games)", "9M 2011", 0.053, "ABPU as reported", "filing_derived", "zynga_s1"),
    ("king_q4_2013", "mobile_iap", "King (Candy Crush 78%)", "Q4 2013", 0.0554, "gross bookings $632M / (124M avg DAU x 92 days)", "filing_derived", "king_f1"),
    ("king_q1_2013", "mobile_iap", "King", "Q1 2013", 0.0676, "gross bookings $219M / (36M avg DAU x 90 days)", "filing_derived", "king_f1"),
    ("rovio_q4_2017", "mobile_iap", "Rovio Games", "Q4 2017", 0.094, "ARPDAU EUR0.08 reported, x1.18 USD/EUR", "filing_derived", "rovio_ar2017"),
    ("rovio_2016", "mobile_iap", "Rovio Games", "Q2-Q3 2016", 0.035, "ARPDAU EUR0.03 reported, x1.12 USD/EUR (paid-UA era; pre-optimization)", "filing_derived", "rovio_ar2017"),
    ("roblox_platform_q2_2025", "roblox_platform", "Roblox (all experiences, platform gross)", "Q2 2025", 0.1413, "bookings $1,437.6M / (111.8M DAU x 91 days)", "filing_derived", "roblox_q2_2025"),
    ("roblox_platform_q3_2025", "roblox_platform", "Roblox (all experiences, platform gross)", "Q3 2025", 0.1379, "bookings $1,921.8M / (151.5M DAU x 92 days)", "filing_derived", "roblox_q3_2025"),
    ("roblox_creator_q3_2025", "roblox_devex", "Roblox creators' share (DevEx)", "Q3 2025", 0.0308, "platform ARPDAU x 22.3% DevEx share of bookings; per platform DAU, not per experience DAU", "filing_derived", "roblox_q3_2025"),
    ("flappy_2014", "mobile_ads", "Flappy Bird (banner ads)", "Jan-Feb 2014", 0.005, "~$50k/day (press estimate) / ~10M DAU (assumption, 50M+ downloads); order of magnitude only", "assumption_range", "rs_birdman"),
    ("slither_2016", "web_mobile_ads", "Slither.io", "mid-2016", 0.01, "~$100k/day (WSJ estimate) / ~10M DAU (assumption); order of magnitude only", "assumption_range", "loop_slither_100k"),
    ("hypercasual_ads", "mobile_ads", "Hypercasual (industry)", "2024-25", 0.05, "blended ad ARPDAU range $0.03-0.08 (third-party benchmarks); midpoint", "third_party", "playio_arpdau"),
    ("hybridcasual", "mobile_ads_iap", "Hybrid-casual (industry)", "2024-25", 0.25, "range $0.15-0.50 (third-party); midpoint", "third_party", "playio_arpdau"),
    ("web_daily_puzzle_ads", "web_ads", "Ad-supported daily web puzzle (model)", "2026", 0.012, "assumption: 1.5 pageviews/day x 3 ad units x blended $2.5 RPM (global mix) => ~$0.011; US-heavy audience at $6 RPM => ~$0.027", "assumption_range", None),
    ("nyt_single_product_sub", "subscription", "NYT other single-product (incl. Games) ARPU", "FY2025", 0.116, "~$3.48/month ARPU / 30 days per SUBSCRIBER (not per DAU); multiply by subscriber conversion of DAU", "filing_derived", "nyt_10k_2025"),
]
