# Business model from evidence

## Revenue per daily player (net to developer)

| Model | low | mid | high | Revenue/yr at 1M DAU (mid) | minus serving cost | Basis |
|---|---|---|---|---|---|---|
| Web daily game, display + interstitial ads | $0.005 | $0.012 | $0.027 | $4.4M | $4.4M | assumption: 1-2 pageviews x 3 units x $2-6 RPM; cross-checks Flappy Bird ~$0.005 (2014) and Slither.io ~$0.01 (2016) order-of-magnitude estimates |
| Mobile app, ads only (hypercasual-style) | $0.030 | $0.050 | $0.080 | $18.2M | $18.2M | third-party benchmarks $0.03-0.08 blended ad ARPDAU; needs app-store discovery, which is mostly paid now (Rovio UA EUR69.6M in 2017) |
| Mobile app, IAP (casual F2P), net of 30% store fee | $0.025 | $0.038 | $0.066 | $14.1M | $14.0M | King Q4'13 $0.055 and Rovio Q4'17 ~$0.094 gross (filings); Rovio Q2'16 ~$0.035; x0.7 store fee |
| Roblox experience (creator DevEx share) | $0.004 | $0.012 | $0.031 | $4.4M | $4.4M | platform bookings/DAU $0.138-0.141 x 22% DevEx = $0.031 per platform DAU (filings); per-experience lower because players visit several experiences a day; hosting is free |
| Subscription funnel (NYT-style), 1-5% of DAU paying $3.5-6/mo | $0.001 | $0.005 | $0.010 | $1.8M | $1.8M | NYT other single-product ARPU ~$3.5/mo, bundle higher (10-K FY2025); conversion rate is an assumption |

Filing-derived reference points (gross bookings per DAU-day):

| Entity | Period | ARPDAU | Quality |
|---|---|---|---|
| Zynga (all games) | 2010 | $0.041 | filing_derived |
| Zynga (all games) | 9M 2011 | $0.053 | filing_derived |
| King (Candy Crush 78%) | Q4 2013 | $0.055 | filing_derived |
| King | Q1 2013 | $0.068 | filing_derived |
| Rovio Games | Q4 2017 | $0.094 | filing_derived |
| Rovio Games | Q2-Q3 2016 | $0.035 | filing_derived |
| Roblox (all experiences, platform gross) | Q2 2025 | $0.141 | filing_derived |
| Roblox (all experiences, platform gross) | Q3 2025 | $0.138 | filing_derived |
| Roblox creators' share (DevEx) | Q3 2025 | $0.031 | filing_derived |
| Flappy Bird (banner ads) | Jan-Feb 2014 | $0.005 | assumption_range |
| Slither.io | mid-2016 | $0.010 | assumption_range |
| Hypercasual (industry) | 2024-25 | $0.050 | third_party |
| Hybrid-casual (industry) | 2024-25 | $0.250 | third_party |
| Ad-supported daily web puzzle (model) | 2026 | $0.012 | assumption_range |
| NYT other single-product (incl. Games) ARPU | FY2025 | $0.116 | filing_derived |

## Keep vs sell

A hit's attention decays. Using the Trends result that the median hit keeps about 30% of peak interest a year later (a fad),
versus the roughly 35-50% that durable daily rituals keep (Wordle and Connections in this dataset):

| Model | Decay | Year-1 net revenue at 1M avg DAU | 5-yr value kept (15% discount) |
|---|---|---|---|
| Web daily game, display + interstitial ads | fad (30%/yr) | $4.4M | $5.9M |
| Web daily game, display + interstitial ads | ritual (50%/yr) | $4.4M | $7.6M |
| Mobile app, ads only (hypercasual-style) | fad (30%/yr) | $18.2M | $24.6M |
| Mobile app, ads only (hypercasual-style) | ritual (50%/yr) | $18.2M | $31.7M |
| Mobile app, IAP (casual F2P), net of 30% store fee | fad (30%/yr) | $14.0M | $18.9M |
| Mobile app, IAP (casual F2P), net of 30% store fee | ritual (50%/yr) | $14.0M | $24.3M |
| Roblox experience (creator DevEx share) | fad (30%/yr) | $4.4M | $5.9M |
| Roblox experience (creator DevEx share) | ritual (50%/yr) | $4.4M | $7.6M |
| Subscription funnel (NYT-style), 1-5% of DAU paying $3.5-6/mo | fad (30%/yr) | $1.8M | $2.5M |
| Subscription funnel (NYT-style), 1-5% of DAU paying $3.5-6/mo | ritual (50%/yr) | $1.8M | $3.2M |

What buyers actually paid (from the acquisitions table):

| Acquirer | Target | Date | Price | What they bought | What happened |
|---|---|---|---|---|---|
| The New York Times Co. | Wordle (Josh Wardle) | 2022-01-31 | $1.0M | audience + daily habit + subscriber funnel | Q1 2022: 'tens of millions of new users', best quarter ever for Games net subscriber adds; Wordle and Connections kept free as funnel through FY2025 10-K |
| Zynga | Newtoy (Words with Friends) | 2010-11 | $53.3M | audience + mobile social graph + team | Zynga doubled WWF DAU within ~120 days via cross-promotion; became a pillar mobile franchise |
| Zynga | OMGPOP (Draw Something) | 2012-03-21 | $183.1M | audience at peak + mobile growth | Draw Something DAU fell ~33% within a month; $95.5M impairment in Q3 2012 (52% of price) six months later |
| Activision Blizzard | King Digital Entertainment | 2015-11-02 | $5,900.0M | revenue + audience + live-ops machine | Candy Crush still a top-grossing franchise a decade later |
| Take-Two Interactive | Zynga | 2022-01-10 | $12,700.0M | mobile revenue + live-ops portfolio | Closed May 2022 |
| Scopely (Savvy Games) | Niantic games business (Pokemon GO) | 2025-03-12 | $3,500.0M | revenue + IP-licensed live game | nan |
| Scopely | Stumble Guys (Kitka Games) | 2022-09-08 | undisclosed | audience (DAU) for a viral clone | nan |
| Spotify | Heardle | 2022-07 | undisclosed | audience + funnel into music discovery | Spotify shut Heardle down in May 2023 |
| Merriam-Webster (Britannica) | Quordle | 2023-01-23 | undisclosed | daily habit + funnel into dictionary site | nan |
| Splitting Point Studios (Jandel) | ~50% of Grow a Garden | 2025-04 | undisclosed | early daily habit + live-ops capacity + creator audience | Grew to 21-22M CCU within ~10 weeks |

- Audience-only deals (no revenue) priced low: Wordle went for 'low seven figures' with ~2M daily players, roughly **$0.5-1 per daily player**.
- Buying at the peak backfired: Zynga paid $183.1M for OMGPOP at about 14M DAU (~$13 per daily player), then wrote off $95.5M (52%) six months later as DAU fell.
- Revenue businesses sell on revenue: Scopely paid $3.5B for Niantic's games, which had more than $1B in 2024 revenue (~3.5x).
- Early equity, not exits: Splitting Point bought about half of Grow a Garden at ~1,000 concurrent players, before the run to 22M.
- The metrics buyers disclosed, from the filings: DAU, MAU, unique payers, bookings per DAU (Zynga ABPU, King MUP bookings, Roblox ABPDAU),
  concentration (Candy Crush was 78% of King's bookings), retention, and for subscription buyers, conversion to subscribers (NYT 'tens of millions of new users').

