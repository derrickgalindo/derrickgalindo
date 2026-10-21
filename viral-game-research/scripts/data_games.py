"""Hand-coded game records.

GAMES: game_id|developer|dev_type|first_release|breakout_date|era|outcome_tier|peak_dau_m|peak_ccu_m|confidence|outcome_basis
  outcome_tier: 0 flop, 1 modest (real traction, < ~1M DAU), 2 hit (~1M+ DAU or US top-10 overall), 3 mega (~10M+ DAU)
  Tiers for web games without disclosed DAU are provisional here and are re-checked against
  Google Trends peak size in build_db.py (see trends_tier_check).

FEATURES: coded from observable gameplay, not from outcome:
  game_id|session_min|ttff_sec|one_input|rules_preknown|share_artifact|artifact_curiosity|invite_needed|daily_sync|scarcity|
  social_graph|spectator|failure_comedy|emergent_output|free|monetization|ip|creator_audience|paid_ua|platform_newness|novelty

BREAKOUTS: game_id|latent_days|ignition_type|first_community|influencer_timing|narrative|source_ids
"""

CLONE_OF = {
    "absurdle": "wordle", "quordle": "wordle", "dordle": "wordle", "octordle": "wordle", "worldle": "wordle",
    "heardle": "wordle", "nerdle": "wordle", "globle": "wordle", "semantle": "wordle", "contexto": "wordle",
    "lewdle": "wordle", "waffle": "wordle", "redactle": "wordle", "loldle": "wordle", "travle": "wordle",
    "costcodle": "wordle", "bandle": "heardle", "splashyfish": "flappybird", "ironpants": "flappybird",
    "flappydunk": "flappybird", "2048": "threes", "wordfeud": "wordswithfriends", "mafiawars": "mobwars",
    "farmville": "farmtown", "slitherio": "agario", "diepio": "agario", "paperio": "agario", "holeio": "agario",
    "mopeio": "agario", "survivio": "agario", "wingsio": "agario", "stumbleguys": "fallguys",
    "minecraftearth": "pokemongo", "ghostbustersworld": "pokemongo", "jurassicworldalive": "pokemongo",
    "goosegooseduck": "amongus", "cashshow": "hqtrivia", "cookiejam": "candycrush", "hamsterkombat": "notcoin",
    "catizen": "notcoin", "tapswap": "notcoin", "suika": None, "subwaysurfers": "templerun",
}

GAMES = """
wordle|Josh Wardle|solo|2021-10-01|2021-12-20|daily_web|3|2.0||high|90 players 2021-11-01 -> 300k 2022-01-02 -> ~2M mid-Jan; NYT: 'tens of millions of new users'
absurdle|Sam Hughes (qntm)|solo|2022-01-04||daily_web|1|||medium|Press coverage Jan 2022; never daily-habit scale
quordle|Freddie Meyer|solo|2022-01-24|2022-02-01|daily_web|1|0.5||medium|Creator: >500k daily players (Feb 2022); acquired by Merriam-Webster Jan 2023 (terms undisclosed)
dordle|Zaratustra|solo|2022-01-20||daily_web|1|||medium|Spinoff coverage; trends-checked
octordle|Kenneth Crawford|solo|2022-01-25||daily_web|1|||medium|Spinoff coverage; trends-checked
worldle|Antoine Teuf|solo|2022-01-21|2022-02-01|daily_web|1|||medium|Large early-2022 spike; trends-checked
heardle|Omakase|small_indie|2022-02-26|2022-04-01|daily_web|2|1.0||medium|Creator: >1M plays/day (one play per day => ~1M DAU), Mar 2022; acquired by Spotify Jul 2022, shut May 2023. Re-tiered 1->2 after Trends cross-check + creator figure
nerdle|Richard Mann|small_indie|2022-01-20||daily_web|1|||medium|trends-checked
globle|Trainwreck Labs|solo|2022-01-20||daily_web|1|||medium|Creator went full-time on ad revenue; trends-checked
semantle|David Turner|solo|2022-01-30||daily_web|1|||medium|trends-checked
contexto|Nildo Junior|solo|2022-04-01||daily_web|1|||medium|Strong in Brazil; trends-checked
lewdle|Gabe Kaplan/others|small_indie|2022-01-19||daily_web|1|||low|trends-checked
waffle|James Robinson|solo|2022-02-15||daily_web|1|||medium|Vendor case study claims 10M+ MAU; trends-checked
redactle|Jason Hutchens|solo|2022-04-01||daily_web|1|||low|trends-checked
loldle|Pimeko|solo|2022-04-01||daily_web|1|||medium|~5M pageviews/month (vendor case study)
travle|Ali Garbuz|solo|2023-01-15||daily_web|1|||low|trends-checked
costcodle|Kerry Shaw|solo|2024-01-15||daily_web|1|||low|Brief viral spike Jan 2024; trends-checked
connections|New York Times (Wyna Liu)|major_publisher|2023-06-12|2023-07-01|daily_web|3|||medium|NYT's second most-played game; inside NYT funnel
strands|New York Times|major_publisher|2024-03-04|2024-03-15|daily_web|2|||medium|NYT funnel; trends-checked
spellingbee|New York Times|major_publisher|2018-05-09|2020-04-01|daily_web|2|||medium|NYT funnel
immaculategrid|Sports Reference|studio|2023-03-30|2023-04-15|daily_web|1|||low|Viral among sports fans 2023; trends-checked
bandle|Bandle team|small_indie|2022-07-01||daily_web|1|||low|trends-checked
queens|LinkedIn|major_publisher|2024-05-01|2024-06-01|daily_web|2|||low|Inside LinkedIn's 1B-member platform; trends-checked
pips|New York Times|major_publisher|2025-08-18||daily_web|1|||low|Recent; trends-checked
flappybird|Dong Nguyen (.GEARS)|solo|2013-05-24|2014-01-10|app_store_mature|3|||high|US #1 free 2014-01-17; #1 in 100+ countries; 50M+ downloads by Feb 2014
splashyfish|Ruben Ifrah|solo|2014-01-25|2014-02-10|app_store_mature|1|||low|Clone that charted briefly after Flappy Bird removal
ironpants|Ignacio Pecino|solo|2014-01-20|2014-02-10|app_store_mature|1|||low|Clone that charted briefly
swingcopters|Dong Nguyen (.GEARS)|solo|2014-08-21||app_store_mature|1|||medium|Strong launch on notoriety, faded; 'It's no Flappy Bird'
flappydunk|Voodoo|studio|2017-05-01|2017-06-01|app_store_mature|2|||low|Voodoo paid-UA hypercasual
timberman|Digital Melody|small_indie|2014-03-01||app_store_mature|1|||low|Charted 2014
colorswitch|Fortafy Games|small_indie|2015-12-01|2016-01-15|app_store_mature|2|||low|Topped US free charts early 2016
pianotiles|Hu Wen Zeng|solo|2014-03-27|2014-05-01|app_store_mature|2|||medium|Topped charts in many countries 2014
crossyroad|Hipster Whale|small_indie|2014-11-20|2014-11-25|app_store_mature|3|||high|50M downloads in 90 days; $10M
geometrydash|RobTop Games|solo|2013-08-13|2014-01-01|app_store_mature|2|||medium|Premium hit with long tail
stack|Ketchapp|studio|2016-02-01|2016-02-15|app_store_mature|2|||low|Ketchapp cross-promo network
helixjump|Voodoo|studio|2018-03-01|2018-05-01|app_store_mature|3|||medium|Paid-UA hypercasual, among most downloaded 2018
mrjump|1Button|small_indie|2015-03-01||app_store_mature|1|||low|Charted 2015
templerun|Imangi Studios|small_indie|2011-08-04|2011-12-15|app_store_early|3|||medium|Went free Dec 2011; tens of millions of downloads
subwaysurfers|Kiloo/SYBO|studio|2012-05-24|2013-01-01|app_store_mature|3|||medium|Long-tail mega hit
fruitninja|Halfbrick|studio|2010-04-21|2010-05-15|app_store_early|3|||medium|Premium mega hit
doodlejump|Lima Sky|small_indie|2009-04-06|2009-06-01|app_store_early|2|||medium|Top paid 2009-10
2048|Gabriele Cirulli|solo|2014-03-09|2014-03-12|app_store_mature|3|||medium|Weekend web clone of 1024/Threes; viral via Hacker News within days
threes|Sirvo (Vollmer, Wohlwend)|small_indie|2014-02-06|2014-02-07|app_store_mature|1|||high|Premium critical hit eclipsed by free clones
suika|Aladdin X|studio|2021-12-09|2023-09-15|streamer|2|||medium|4M+ Switch downloads after streamer surge Sep 2023
candycrush|King|major_publisher|2012-04-12|2013-01-15|app_store_mature|3|124||high|King total DAU 124M Q4 2013; Candy Crush 78% of bookings
bejeweledblitz|PopCap|studio|2008-12-01|2009-03-01|fb_social|2|||medium|Top Facebook game 2009-10
farmheroes|King|major_publisher|2013-04-01|2014-01-01|app_store_mature|2|||medium|King top-3 game in Q4 2013
petrescue|King|major_publisher|2012-10-01|2013-01-01|app_store_mature|2|||medium|King top-3 game in Q4 2013
bubblewitch|King|major_publisher|2011-09-01|2011-11-01|fb_social|2|||medium|Early King Facebook hit
diamonddash|Wooga|studio|2011-05-01|2011-07-01|fb_social|2|||low|Wooga Facebook hit
jellysplash|Wooga|studio|2013-05-01||app_store_mature|1|||low|Briefly top-grossing
candycrushsoda|King|major_publisher|2014-11-01|2014-11-15|app_store_mature|2|||medium|Cross-promoted sequel
blockblast|Hungry Studio|studio|2023-01-01|2024-03-01|app_store_mature|3|||low|Top downloads 2024; heavy paid UA
angrybirds|Rovio (pub. Chillingo)|studio|2009-12-11|2010-02-11|app_store_early|3|||high|UK #1 Feb 2010 after App Store feature; global mega hit
crushthecastle|Armor Games / Jason Calabrese|solo|2009-03-01||fb_social|1|||medium|Popular Flash game; mechanic predecessor to Angry Birds
cuttherope|ZeptoLab (pub. Chillingo)|small_indie|2010-10-05|2010-10-10|app_store_early|3|||medium|1M paid downloads in ~10 days
amazingalex|Rovio|studio|2012-07-12||app_store_mature|1|||medium|Launched with Angry Birds cross-promotion; faded
badpiggies|Rovio|studio|2012-09-27|2012-09-27|app_store_mature|2|||medium|#1 paid US within hours (Angry Birds IP)
wheresmywater|Disney Mobile|major_publisher|2011-09-22|2011-10-01|app_store_early|2|||medium|#1 paid
wordswithfriends|Newtoy|small_indie|2009-07-21|2009-10-05|app_store_early|2|4.4||medium|4.4M DAU Nov 2011 (Inside Social Games via ABC); Zynga doubled DAU in 120 days post-acquisition
chesswithfriends|Newtoy|small_indie|2009-01-01||app_store_early|1|||medium|'Did fairly well' but was not the hit
hangingwithfriends|Zynga|major_publisher|2011-06-01|2011-06-15|app_store_mature|1|||medium|Briefly the leading word game (Zynga S-1), faded
wordfeud|Bertheussen IT|solo|2010-06-01|2011-01-01|app_store_early|2|||low|Nordic/European hit
ruzzle|MAG Interactive|studio|2012-03-01|2012-12-01|app_store_mature|2|||low|European hit 2012-13
songpop|FreshPlanet|studio|2012-05-01|2012-06-01|fb_social|2|||low|Large Facebook/mobile hit 2012
drawsomething|OMGPOP|studio|2012-02-06|2012-02-25|app_store_mature|3|14.3||high|~14.3-15M DAU Apr 2012 then -33% in 30 days; Zynga paid $183.1M then impaired $95.5M
drawsomething2|Zynga|major_publisher|2013-03-05||app_store_mature|0|||medium|Sequel did not chart meaningfully
triviacrack|Etermax|studio|2013-10-01|2014-11-01|app_store_mature|3|||medium|#1 US free 66 consecutive days; 65M downloads by Nov 2014
quizup|Plain Vanilla|studio|2013-11-07|2013-11-20|app_store_mature|2|||low|Fast early growth, later collapse
hqtrivia|Intermedia Labs|studio|2017-08-01|2017-10-15|app_store_mature|2||2.38|high|2.38M concurrent March 2018; shut down Feb 2020
headsup|Warner Bros / Ellen DeGeneres|major_publisher|2013-05-01|2013-05-15|app_store_mature|2|||medium|#1 paid app driven by Ellen show
bitlife|Candywriter|small_indie|2018-09-01|2019-02-01|streamer|2|||low|#1 US 2019 via YouTube/TikTok
dumbways|Metro Trains Melbourne / McCann|studio|2013-05-15|2013-05-20|app_store_mature|2|||medium|Rode viral PSA video (Nov 2012)
farmville|Zynga|major_publisher|2009-06-19|2009-07-15|fb_social|3|34.5||high|11M DAU at 9 weeks; peak ~34.5M DAU
farmtown|Slashkey|small_indie|2009-02-01|2009-04-01|fb_social|2|||low|Large Facebook farm game before FarmVille
mafiawars|Zynga|major_publisher|2008-06-01|2008-10-01|fb_social|2|||medium|Top FB game 2009; $129.1M 2010 revenue (S-1)
mobwars|Psycho Monkey|solo|2008-01-01|2008-03-01|fb_social|1|||medium|Original; lost to Zynga clone
cityville|Zynga|major_publisher|2010-12-02|2010-12-15|fb_social|3|||medium|Fastest FB game to 100M MAU
petsociety|Playfish|studio|2008-08-01|2008-10-01|fb_social|2|||low|Playfish acquired by EA 2009
farmville2|Zynga|major_publisher|2012-09-18|2012-09-25|fb_social|2|||low|Large launch on Zynga network
agario|Matheus Valadares|solo|2015-04-28|2015-05-15|web_io|3|||medium|Most popular browser game of 2015; mobile #1
slitherio|Steve Howse (Lowtech)|solo|2016-03-25|2016-04-10|web_io|3|||medium|Top-10 apps; ~$100k/day (WSJ est.)
diepio|Matheus Valadares|solo|2016-06-01|2016-11-01|web_io|2|||low|Same creator as Agar.io
paperio|Voodoo|studio|2016-08-01|2018-01-01|web_io|2|||low|Paid-UA mobile
holeio|Voodoo|studio|2018-05-01|2018-06-01|web_io|3|||medium|#1 downloads 2018 via paid UA
krunker|Yendis Entertainment|small_indie|2018-08-01|2019-01-01|web_io|1|||low|Bought by FRVR 2021
skribbl|ticedev|solo|2017-12-01|2020-04-01|streamer|2|||low|Pandemic + streamers
garticphone|Onrizon|small_indie|2020-12-01|2021-01-15|streamer|2|||low|Streamer-driven
amongus|InnerSloth|small_indie|2018-06-15|2020-08-01|streamer|3||1.5|high|1.5M CCU Sep 5 2020; Twitch avg viewers 460 Jun -> 53k Aug 2020
townofsalem|BlankMediaGames|small_indie|2014-12-01|2015-02-01|web_io|1|||low|Browser social deduction
projectwinter|Other Ocean|studio|2019-05-23||streamer|1|||low|Paid PC social deduction, niche
fallguys|Mediatonic / Devolver|studio|2020-08-04|2020-08-04|streamer|3|||medium|Free on PS Plus + streamers; 2M Steam copies week 1
stumbleguys|Kitka Games|small_indie|2020-08-25|2021-07-01|streamer|3|20||medium|20M DAU at Scopely acquisition (Sep 2022)
pokemongo|Niantic / The Pokemon Company|major_publisher|2016-07-06|2016-07-07|app_store_mature|3|||high|50M downloads in 19 days (Sensor Tower)
ingress|Niantic (Google)|studio|2012-11-15||app_store_mature|1|||medium|Same mechanic, no IP; niche
wizardsunite|Niantic / WB|major_publisher|2019-06-21||app_store_mature|1|||high|~$12M first month vs Pokemon GO ~$300M; shut down Jan 2022
minecraftearth|Microsoft/Mojang|major_publisher|2019-10-17||app_store_mature|0|||medium|Shut down June 2021
infinitecraft|Neal Agarwal|solo|2024-01-31|2024-02-01|daily_web|3|||medium|Launch post ~15M views week 1; huge Feb 2024 search spike; trends-checked
littlealchemy|Jakub Koziol (Recloak)|solo|2010-12-01|2011-06-01|fb_social|2|||low|Web/mobile hit; trends-checked
cookieclicker|Julien Thiennot (Orteil)|solo|2013-08-08|2013-08-20|app_store_mature|2|||low|Viral idle web game; trends-checked
geoguessr|Anton Wallen|solo|2013-05-09|2013-05-20|app_store_mature|2|||medium|Viral 2013; later streamer-driven subscription business
passwordgame|Neal Agarwal|solo|2023-06-27|2023-06-28|daily_web|2|||low|Viral via creator audience; trends-checked
universalpaperclips|Frank Lantz|solo|2017-10-09|2017-10-12|web_io|1|||medium|~450k players in first 11 days (creator)
growagarden|BMWLux + Splitting Point|small_indie|2025-03-26|2025-05-10|roblox_algo|3|60|22.3|high|1k CCU Apr 2025 -> 5M CCU May 18 -> 21.3M Jun 21 (day 87); ~60M DAU
stealabrainrot|BRAZILIAN SPYDER (Roblox group)|small_indie|2025-05-15|2025-07-15|roblox_algo|3||25.4|medium|25.4M CCU Oct 2025; -99% CCU by 2026
dresstoimpress|Gigi & Tracy (group)|small_indie|2023-11-01|2024-06-01|roblox_algo|2|||low|1M+ CCU 2024
99nights|Grandma's Favourite Games|small_indie|2025-04-01|2025-07-15|roblox_algo|3|||low|Multi-million CCU July 2025 (Roblox Q2 letter names it viral)
deadrails|RCM Games|small_indie|2025-02-01|2025-03-15|roblox_algo|2|||low|Top-10 by Robux spend June 2025 (Roblox)
fisch|Fisch team|small_indie|2024-10-01|2024-11-01|roblox_algo|2|||low|Top experience late 2024
doors|LSPLASH|small_indie|2022-08-01|2022-08-15|roblox_algo|2|||low|Top experience 2022
adoptme|Uplift Games|small_indie|2017-07-14|2019-06-01|roblox_algo|3||1.6|medium|1.6M CCU 2019
notcoin|Open Builders|studio|2024-01-01|2024-03-01|telegram|3|||low|Tap-to-earn with token airdrop incentive
hamsterkombat|Hamster Kombat team|studio|2024-03-26|2024-05-15|telegram|3|||medium|300M joined (company claim) -> 41M MAU after airdrop
catizen|Catizen team|studio|2024-03-01|2024-06-01|telegram|2|||low|Tap-to-earn
tapswap|TapSwap team|studio|2024-02-01|2024-05-01|telegram|2|||low|Tap-to-earn
cashshow|Uken|studio|2017-12-01||app_store_mature|0|||low|HQ clone, faded
ghostbustersworld|FourThirtyThree|studio|2019-01-01||app_store_mature|0|||medium|IP location game flop
jurassicworldalive|Ludia|studio|2018-05-24|2018-05-30|app_store_mature|1|||low|IP location game, modest
goosegooseduck|Gaggle Studios|small_indie|2021-10-01|2022-12-01|streamer|2|||low|Among Us-like, big with Asian streamers
mopeio|Stan Tatarnykov|solo|2016-07-01|2016-08-01|web_io|1|||low|.io wave
survivio|Justin Kim|small_indie|2017-10-01|2018-01-01|web_io|1|||low|.io battle royale, acquired by Kongregate 2019
wingsio|.io dev|solo|2016-05-01||web_io|0|||low|.io wave, little traction
cookiejam|SGN / Jam City|studio|2014-08-01|2015-01-01|app_store_mature|2|||low|Paid-UA match-3
doodlegod|JoyBits|studio|2010-08-01|2010-12-01|fb_social|1|||low|Element combination predecessor of Infinite Craft
drawmything|OMGPOP|studio|2008-01-01||fb_social|1|||medium|Web predecessor of Draw Something by the same studio
lexulous|RJ Softwares (Agarwalla bros)|small_indie|2008-07-01|2008-07-01|fb_social|1|||medium|Ex-Scrabulous; pushed off Facebook by Hasbro suit
"""

FEATURES = """
wordle|3|10|1|1|2|1|0|1|1|0|0|0|0|1|none|0|0|0|0|1
absurdle|4|10|1|1|2|1|0|0|0|0|0|0|0|1|none|0|1|0|0|0
quordle|6|10|1|1|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|0
dordle|5|10|1|1|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|0
octordle|10|10|1|1|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|0
worldle|2|10|1|0|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|1
heardle|2|10|1|1|2|1|0|1|1|0|0|0|0|1|none|0|0|0|0|1
nerdle|3|10|1|1|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|0
globle|3|10|1|1|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|0
semantle|10|10|1|0|2|0|0|1|1|0|0|0|0|1|none|0|0|0|0|2
contexto|5|10|1|0|2|0|0|1|1|0|0|0|0|1|ads|0|0|0|0|1
lewdle|3|10|1|1|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|0
waffle|4|10|0|0|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|1
redactle|15|30|1|0|2|0|0|1|1|0|0|0|0|1|none|0|0|0|0|2
loldle|3|10|1|0|2|0|0|1|1|0|0|0|0|1|ads|1|0|0|0|0
travle|5|10|1|0|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|1
costcodle|2|10|1|1|2|1|0|1|1|0|0|0|0|1|none|1|0|0|0|0
connections|3|10|1|1|2|1|0|1|1|0|0|0|0|1|sub|0|2|0|0|1
strands|5|10|1|0|2|1|0|1|1|0|0|0|0|1|sub|0|2|0|0|1
spellingbee|15|10|1|0|1|0|0|1|0|0|0|0|0|0|sub|0|2|0|0|1
immaculategrid|5|20|1|0|2|1|0|1|1|0|0|0|0|1|ads|0|1|0|0|1
bandle|2|10|1|1|2|1|0|1|1|0|0|0|0|1|ads|0|0|0|0|0
queens|3|10|1|1|2|1|0|1|1|2|0|0|0|1|none|0|2|0|0|1
pips|4|10|0|1|2|0|0|1|1|0|0|0|0|1|sub|0|2|0|0|1
flappybird|1|3|1|0|1|0|0|0|0|0|2|1|0|1|ads|0|0|0|0|1
splashyfish|1|3|1|0|1|0|0|0|0|0|1|1|0|1|ads|0|0|0|0|0
ironpants|1|3|1|0|1|0|0|0|0|0|1|1|0|1|ads|0|0|0|0|0
swingcopters|1|3|1|0|1|0|0|0|0|0|2|1|0|1|ads|0|2|0|0|0
flappydunk|1|3|1|0|1|0|0|0|0|0|1|1|0|1|ads|0|2|1|0|0
timberman|1|3|1|0|1|0|0|0|0|0|1|1|0|1|ads|0|0|0|0|1
colorswitch|1|3|1|0|1|0|0|0|0|0|1|1|0|1|ads|0|0|0|0|1
pianotiles|1|3|1|0|1|0|0|0|0|0|1|1|0|1|ads|0|0|0|0|1
crossyroad|2|3|1|1|1|0|0|0|0|0|1|1|0|1|ads+iap|0|1|0|0|1
geometrydash|3|10|1|0|1|0|0|0|0|0|2|1|1|0|premium|0|0|0|0|1
stack|1|2|1|0|1|0|0|0|0|0|0|1|0|1|ads|0|2|1|0|1
helixjump|1|2|1|0|1|0|0|0|0|0|1|1|0|1|ads|0|2|1|0|1
mrjump|1|3|1|0|1|0|0|0|0|0|1|1|0|1|ads|0|0|0|0|0
templerun|3|5|1|0|1|0|0|0|0|0|1|1|0|1|iap|0|1|0|1|2
subwaysurfers|3|5|1|0|1|0|0|0|0|0|1|1|0|1|ads+iap|0|1|0|1|0
fruitninja|1.5|3|1|0|1|0|0|0|0|0|1|0|0|0|premium|0|1|0|2|2
doodlejump|3|3|1|0|1|0|0|0|0|0|0|1|0|0|premium|0|0|0|2|1
2048|5|3|1|0|1|0|0|0|0|0|0|0|0|1|none|0|0|0|0|0
threes|5|20|1|0|1|0|0|0|0|0|0|0|0|0|premium|0|1|0|0|2
suika|5|5|1|0|1|0|0|0|0|0|2|1|0|0|premium|0|0|0|0|0
candycrush|3|10|1|1|2|0|0|0|1|2|0|0|0|1|iap|0|2|1|1|1
bejeweledblitz|1|5|1|1|2|0|0|0|0|2|0|0|0|1|iap|0|2|0|2|1
farmheroes|3|10|1|1|2|0|0|0|1|2|0|0|0|1|iap|0|2|1|1|0
petrescue|3|10|1|1|2|0|0|0|1|2|0|0|0|1|iap|0|2|1|1|0
bubblewitch|3|10|1|1|2|0|0|0|1|2|0|0|0|1|iap|0|2|1|2|0
diamonddash|1|5|1|1|2|0|0|0|1|2|0|0|0|1|iap|0|1|0|2|1
jellysplash|3|10|1|1|2|0|0|0|1|2|0|0|0|1|iap|0|1|1|1|0
candycrushsoda|3|10|1|1|2|0|0|0|1|2|0|0|0|1|iap|1|2|1|1|0
blockblast|5|5|1|1|0|0|0|0|0|0|0|0|0|1|ads+iap|0|1|1|0|0
angrybirds|2|10|1|0|1|0|0|0|0|0|1|1|0|0|premium|0|1|0|2|1
crushthecastle|2|10|1|0|0|0|0|0|0|0|0|1|0|1|ads|0|1|0|0|2
cuttherope|2|10|1|0|0|0|0|0|0|0|0|0|0|0|premium|0|1|0|2|2
amazingalex|3|30|1|0|1|0|0|0|0|0|0|0|1|0|premium|0|2|1|1|1
badpiggies|3|20|1|0|1|0|0|0|0|0|1|1|1|0|premium|1|2|1|1|1
wheresmywater|2|10|1|0|0|0|0|0|0|0|0|0|0|0|premium|0|2|0|2|2
wordswithfriends|3|20|1|1|2|0|1|0|1|2|0|0|0|1|ads+premium|0|0|0|2|1
chesswithfriends|5|20|1|1|2|0|1|0|1|2|0|0|0|1|ads+premium|0|0|0|2|1
hangingwithfriends|3|20|1|1|2|0|1|0|1|2|0|0|0|1|ads+iap|0|2|1|1|0
wordfeud|3|20|1|1|2|0|1|0|1|1|0|0|0|1|ads+premium|0|0|0|2|0
ruzzle|2|10|1|1|2|0|1|0|1|2|0|0|0|1|ads+premium|0|0|0|1|1
songpop|2|10|1|1|2|0|1|0|1|2|0|0|0|1|ads+iap|0|0|0|1|1
drawsomething|3|20|1|1|2|0|1|0|1|2|1|1|1|1|ads+premium|0|1|0|1|1
drawsomething2|3|20|1|1|2|0|1|0|1|2|1|1|1|1|ads+iap|0|2|1|0|0
triviacrack|3|10|1|1|2|0|1|0|1|2|0|0|1|1|ads+iap|0|0|0|1|1
quizup|2|20|1|1|2|0|0|0|0|1|0|0|0|1|iap|0|0|0|1|1
hqtrivia|15|60|1|1|1|0|0|1|1|1|1|0|0|1|ads|0|1|0|1|2
headsup|5|10|1|1|1|0|1|0|0|0|2|1|1|0|premium|1|2|0|1|1
bitlife|10|20|1|0|1|0|0|0|0|0|2|1|1|1|ads+iap|0|0|0|1|2
dumbways|2|5|1|0|1|0|0|0|0|0|1|1|0|1|ads|1|2|0|1|1
farmville|5|60|1|0|2|0|0|0|1|2|0|0|0|1|iap|0|2|1|2|1
farmtown|5|60|1|0|2|0|0|0|1|2|0|0|0|1|iap|0|0|0|2|1
mafiawars|3|30|1|0|2|0|0|0|1|2|0|0|0|1|iap|0|2|1|2|0
mobwars|3|30|1|0|2|0|0|0|1|2|0|0|0|1|iap|0|0|0|2|2
cityville|5|60|1|0|2|0|0|0|1|2|0|0|0|1|iap|0|2|1|1|0
petsociety|5|60|1|0|2|0|0|0|1|2|0|0|0|1|iap|0|1|0|2|1
farmville2|5|60|1|0|2|0|0|0|1|2|0|0|0|1|iap|0|2|1|0|0
agario|5|5|1|0|1|0|0|0|0|1|2|1|0|1|ads|0|0|0|2|2
slitherio|5|5|1|0|1|0|0|0|0|1|2|1|0|1|ads|0|0|0|1|0
diepio|8|5|0|0|1|0|0|0|0|1|2|1|0|1|ads|0|1|0|1|0
paperio|3|5|1|0|1|0|0|0|0|1|1|1|0|1|ads|0|2|1|0|0
holeio|2|5|1|0|1|0|0|0|0|1|1|1|0|1|ads|0|2|1|0|1
krunker|10|10|0|0|1|0|0|0|0|1|2|0|0|1|ads+iap|0|0|0|0|1
skribbl|15|20|1|1|1|0|1|0|0|1|2|1|1|1|ads|0|0|0|1|0
garticphone|15|30|1|1|1|0|1|0|0|1|2|1|1|1|ads|0|1|0|1|1
amongus|10|60|0|1|0|0|1|0|0|1|2|1|1|1|ads+iap|0|0|0|1|1
townofsalem|20|60|0|1|0|0|1|0|0|1|1|1|1|1|iap|0|0|0|0|1
projectwinter|30|120|0|1|0|0|1|0|0|1|2|1|1|0|premium|0|1|0|0|1
fallguys|10|30|0|0|1|0|0|0|0|1|2|1|1|0|premium|0|2|0|1|2
stumbleguys|5|20|0|0|1|0|0|0|0|1|2|1|1|1|ads+iap|0|0|0|1|0
pokemongo|15|60|1|1|1|0|0|0|0|0|1|0|0|1|iap|1|2|0|1|2
ingress|20|120|1|0|0|0|0|0|0|0|0|0|0|1|none|0|1|0|1|2
wizardsunite|15|120|1|0|1|0|0|0|0|0|0|0|0|1|iap|1|2|1|0|0
minecraftearth|15|120|0|0|1|0|0|0|0|0|0|0|1|1|iap|1|2|0|0|0
infinitecraft|15|5|1|0|1|0|0|0|0|0|2|1|1|1|ads|0|2|0|0|2
littlealchemy|20|10|1|0|0|0|0|0|0|0|1|0|0|1|ads+premium|0|0|0|1|1
cookieclicker|30|5|1|0|1|0|0|0|0|0|1|0|0|1|ads|0|0|0|0|2
geoguessr|10|20|1|0|1|0|0|0|0|0|2|1|0|1|sub|0|0|0|0|2
passwordgame|15|5|1|0|1|0|0|0|0|0|2|1|1|1|none|0|2|0|0|2
universalpaperclips|60|10|1|0|0|0|0|0|0|0|0|0|0|1|none|0|1|0|0|2
growagarden|15|30|1|0|1|0|0|0|1|2|1|0|0|1|iap|0|1|0|1|0
stealabrainrot|15|20|1|0|1|0|0|0|1|2|2|1|0|1|iap|0|0|0|1|1
dresstoimpress|10|30|0|0|1|0|0|0|0|2|2|1|1|1|iap|0|0|0|1|1
99nights|20|60|0|0|1|0|1|0|0|2|2|1|0|1|iap|0|0|0|1|1
deadrails|15|60|0|0|1|0|1|0|0|2|2|1|0|1|iap|0|0|0|1|1
fisch|15|60|1|0|1|0|0|0|1|2|1|0|0|1|iap|0|0|0|1|0
doors|20|60|0|0|1|0|1|0|0|2|2|1|0|1|iap|0|0|0|1|1
adoptme|20|60|1|0|1|0|0|0|1|2|1|0|0|1|iap|0|0|0|2|1
notcoin|2|5|1|0|2|0|0|0|1|2|0|0|0|1|crypto|0|1|0|2|2
hamsterkombat|3|5|1|0|2|0|0|1|1|2|0|0|0|1|crypto|0|0|0|2|0
catizen|5|10|1|0|2|0|0|0|1|2|0|0|0|1|crypto|0|0|0|2|0
tapswap|2|5|1|0|2|0|0|0|1|2|0|0|0|1|crypto|0|0|0|2|0
cashshow|15|60|1|1|1|0|0|1|1|1|0|0|0|1|ads|0|1|0|0|0
ghostbustersworld|15|120|1|0|1|0|0|0|0|0|0|0|0|1|iap|1|1|0|0|0
jurassicworldalive|15|60|1|0|1|0|0|0|1|0|0|0|0|1|iap|1|1|1|0|0
goosegooseduck|10|60|0|1|0|0|1|0|0|1|2|1|1|1|iap|0|0|0|0|0
mopeio|5|5|1|0|1|0|0|0|0|1|1|1|0|1|ads|0|0|0|1|0
survivio|5|10|0|0|1|0|0|0|0|1|2|1|0|1|ads|0|0|0|1|1
wingsio|5|5|1|0|1|0|0|0|0|1|1|1|0|1|ads|0|0|0|1|0
cookiejam|3|10|1|1|2|0|0|0|1|2|0|0|0|1|iap|0|1|1|0|0
doodlegod|20|10|1|0|0|0|0|0|0|0|0|0|0|0|premium|0|0|0|1|1
drawmything|10|30|1|1|0|0|0|0|0|1|1|1|1|1|ads|0|0|0|1|1
lexulous|10|30|1|1|2|0|1|0|1|2|0|0|0|1|ads|0|0|0|2|0
"""

BREAKOUTS = """
wordle|80|organic_word_of_mouth|Wardle's family group chat -> New Zealand Twitter|after_growth_began|Built 2020 for partner; public Oct 2021. 90 players Nov 1. Family chat, a mention in an NYT newsletter footnote, then big in NZ where a player invented the emoji grid. Share button shipped 2021-12-16. 300k players Jan 2; NYT profile Jan 3 then celebrities; ~2M mid-Jan; sold Jan 31.|wordle_players_90_300k,wardle_gdc2022_ts,wardle_gdc2022_gd,wardle_tweet_share,wordle_nyt_lowseven
flappybird|231|organic_word_of_mouth|US teens on Twitter (rage/complaint posts)|after_growth_began|13 reviews May-Oct 2013; Sept bug-fix update; first tweet Nov 4; US game charts Nov (#1,368); top 250 free Dec 13 as frustrated tweets begin; top 10 Jan 10; #1 Jan 17; PewDiePie video Jan 27; pulled Feb 9. No marketing. Bot accusations never substantiated.|rs_birdman,ibt_flappy_timeline,kotaku_flappy_fiasco,kym_pewdiepie_flappy
angrybirds|62|platform_feature|UK App Store (Game of the Week)|none|Published by Chillingo Dec 2009 with little attention; UK App Store Game of the Week Feb 11 2010 lifted it from ~#600 to #1; US followed.|toucharcade_ab2010
wordswithfriends|76|celebrity|Early iPhone owners|after_growth_began|Launched Jul 2009; founders say growth already inflecting before John Mayer tweeted it was 'the new Twitter' on Oct 5 2009.|techcrunch_wwf_2010
candycrush|275|paid_ua|King Facebook network|none|Facebook Apr 2012 (King had 15M DAU network), mobile Nov 2012; King states it seeds viral channels with paid acquisition; DAU 15M->124M during 2013.|king_f1
farmville|26|platform_feature|Facebook news feed and notifications|none|Launched Jun 19 2009 on Facebook with Zynga cross-promo; 1M new DAU per week; 11M DAU at 9 weeks. Facebook curtailed app notifications in early 2010 and Zynga DAU fell 67M->48M.|zynga_farmville_11m,zynga_s1
drawsomething|19|organic_word_of_mouth|Friends-invite loop|none|Launched Feb 6 2012; 50M downloads in ~50 days; ~14.3M DAU Apr 2; -33% within a month; Zynga bought OMGPOP Mar 21 for $183.1M and impaired $95.5M by Q3.|zynga_10q_2012q1,zynga_10q_2012q3,mcv_drawsomething_decline
2048|3|community_forum|Hacker News|none|Weekend fork of 1024 (itself a Threes clone), posted on Hacker News Mar 9 2014; open-source forks multiplied.|techcrunch_threes_clones
threes|1|press|Apple/press feature|none|Premium $1.99 launch Feb 6 2014 to acclaim; free clones 1024 (Feb 27) and 2048 (Mar 9) eclipsed it within weeks.|techcrunch_threes_clones
amongus|778|influencer|South Korean and Brazilian streamers -> Sodapoppin (Twitch)|before_growth|Released Jun 2018, low double-digit players for most of first year; streamers in Korea/Brazil then Sodapoppin from Jul 15 2020 (Twitch avg viewers 460 -> 53k); 1.5M CCU Sep 5 2020.|ggrecon_amongus,tubefilter_amongus
suika|645|influencer|Japanese VTubers and streamers|before_growth|Switch eShop Japan Dec 2021 (clone of Chinese web game Merge Big Watermelon); exploded Sep 2023 after streamers; sales up 50,000x; 4M+ downloads.|automaton_suika,nintendolife_suika_4m
triviacrack|396|diaspora_family|Argentina -> Latin America -> US Hispanic families|none|Oct 2013 Argentina top-10 in 6 weeks; three LatAm waves; US Nov 2014 via relatives; #1 US 66 days.|mdm_triviacrack,tnw_triviacrack,bbc_triviacrack
crossyroad|5|platform_feature|App Store feature + PewDiePie|unclear|Featured by Apple at launch; 50M downloads in 90 days.|cultofmac_crossy
agario|17|community_forum|4chan /v/|after_growth_began|Developer shared IP on 4chan Apr 27-28 2015 for testing; name suggested by 4chan user; YouTube let's-plays amplified.|wiki_agario
slitherio|16|influencer|YouTube let's plays (incl. PewDiePie)|unclear|Launched Mar 25 2016, no marketing budget; YouTube let's-plays; top-10 apps; ~$100k/day.|loop_slither_100k
hqtrivia|75|press|Tech Twitter / press|none|Live twice-daily show; 2.38M concurrent Mar 2018; novelty faded, shut Feb 2020.|tc_hq_decline,hq_shutdown
growagarden|45|algorithm|Roblox recommendations + Jandel (12M TikTok) after stake at ~1k CCU|before_growth|Built in ~3 days by 16-year-old; Splitting Point bought half at ~500-1,000 CCU in April 2025; weekly updates; 5M CCU May 18; 21.3M CCU Jun 21 (day 87).|gamesbeat_jandel,wiki_grow_a_garden,roblox_q2_2025
stealabrainrot|60|algorithm|Roblox recommendations + Italian-brainrot TikTok meme|unclear|Rode a TikTok meme universe; 25.4M CCU Oct 2025; -99% by 2026.|pgbiz_brainrot_25m,rowatcher_brainrot_decline
infinitecraft|1|creator_audience|neal.fun audience; launch post 15M views week 1|before_growth|Instant spike from creator audience; Twitch/YouTube amplification.|wiki_infinite_craft
pokemongo|1|ip_fandom|Pokemon fandom worldwide|none|IP + Niantic Ingress tech; 50M downloads in 19 days.|sensortower_pogo
wizardsunite|0|ip_fandom|Harry Potter fans|none|Same tech/team pattern and huge IP; ~$12M first month vs ~$300M; shut Jan 2022.|sensortower_hpwu,rs_wizards_shutdown
hamsterkombat|50|incentive|Telegram channels + referral bonuses + token airdrop promise|none|300M joined (company claim); 86% drop after token listing.|forklog_hamster
swingcopters|0|creator_audience|Flappy Bird notoriety|none|Huge launch attention, did not retain.|nbc_swingcopters
stumbleguys|300|unclear|Mobile players without Fall Guys access|unclear|Mobile Fall Guys-like; 20M DAU by Sep 2022; acquired by Scopely.|scopely_stumble
"""
