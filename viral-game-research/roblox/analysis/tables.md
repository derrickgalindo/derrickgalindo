# Roblox deep dive: tables (n=641 games, snapshot 2026-10-26)

## A. Who is on top

- Top 100 by live players: median age 1.6 years; created in the last 120 days: 36; last 365 days: 46; older than 3 years: 32.
- Games at or above ~1M-DAU scale now (>= 75,000 concurrent): 19.

| name | playing_now | created | genre | max_players | like_ratio | n_passes | name_changes_90d |
|---|---|---|---|---|---|---|---|
| Steal An Egg | 1,285,170 | 2026-07-25 | Simulation | 7.00 | 0.92 | 2 | 2 |
| Brookhaven 🏡RP | 405,514 | 2020-04-21 | Roleplay & Avatar Sim | 30.00 | 0.86 | 18 | 0 |
| Murder Mystery 2 | 279,689 | 2014-01-18 | Survival | 12.00 | 0.91 | 3 | 0 |
| 99 Nights in the Forest 🔦 | 231,935 | 2025-03-04 | Survival | 25.00 | 0.90 | 1 | 0 |
| [🎃] Adopt Me! | 229,654 | 2017-07-14 | Roleplay & Avatar Sim | 35.00 | 0.86 | 6 | 42 |
| Blox Fruits | 228,210 | 2019-01-16 | RPG | 12.00 | 0.92 | 6 | 1 |
| [💀] Steal a Brainrot | 218,468 | 2025-05-16 | Simulation | 8.00 | 0.85 | 3 | 2 |
| [🎃] RIVALS | 171,106 | 2024-05-26 | Shooter | 40.00 | 0.94 | 8 | 0 |
| Break and Steal an Egg | 140,261 | 2026-09-05 | Simulation | 7.00 | 0.97 | 0 | 0 |
| [HIRED KILLER] Jujutsu Shenanigans | 137,181 | 2022-04-17 | Action | 25.00 | 0.86 | 5 | 0 |
| [BUTCHER x 🎃] Violence District | 106,186 | 2024-10-31 | Survival | 6.00 | 0.93 | 2 | 0 |
| [🎃 NEW QUEST] Dress To Impress | 92,094 | 2023-10-18 | Roleplay & Avatar Sim | 13.00 | 0.91 | 14 | 0 |
| [NEW STAGES]  DONT SPLASH 🎃 | 90,782 | 2026-10-17 | Obby & Platformer | 10.00 | 0.89 | 12 | 0 |
| 🎃 Dandy's World [ALPHA] | 85,622 | 2024-01-26 | Survival | 35.00 | 0.88 | 7 | 0 |
| [🎃] Anime Dice | 85,207 | 2026-08-15 | Simulation | 9.00 | 0.99 | 8 | 1 |
| [🎃UPD] Fish It! 🐟 | 77,334 | 2024-10-21 | Simulation | 20.00 | 0.83 | 12 | 18 |
| [🎃HLWN] Evade  | 76,203 | 2022-06-10 | Survival | 15.00 | 0.94 | 26 | 1 |
| 🎉 [PSX] Pet Simulator 99! 🐾 | 75,951 | 2022-02-05 | Simulation | 10.00 | 0.95 | 13 | 5 |
| Fisch 👻 [HORSEMAN] | 75,675 | 2024-03-13 | Simulation | 20.00 | 0.91 | 9 | 3 |
| The Strongest Battlegrounds | 71,194 | 2022-08-02 | Action | 15.00 | 0.84 | 7 | 0 |
| DOORS 🍬🍭 | 58,274 | 2021-03-14 | Survival | 50.00 | 0.93 | 3 | 0 |
| Catalog Avatar Creator | 58,114 | 2021-07-03 | Shopping | 24.00 | 0.94 | 0 | 0 |
| [X50] +1 Speed Keyboard Escape | Candy & Chocolate | 57,612 | 2026-01-18 | Simulation | 22.00 | 0.97 | 46 | 28 |
| [🔥TRADES+X2 EXP💎}Cameraman Tower Defense | 53,086 | 2026-08-26 | Strategy | 30.00 | 0.99 | 0 | 1 |
| 🎃 Sell Fries! [Anomaly] 🍟 | 52,558 | 2026-09-21 | Survival | 18.00 | 0.84 | 2 | 0 |
| [🤹APRIL FOOL'S🤡] Anime Adventures | 52,144 | 2021-12-21 | Strategy | 30.00 | 0.92 | 5 | 0 |
| [UPD] Volleyball Legends | 51,934 | 2024-12-17 | Sports & Racing | 12.00 | 0.95 | 3 | 0 |
| [👻] Tap Simulator REBORN | 50,293 | 2026-08-04 | Simulation | 10.00 | 0.95 | 10 | 3 |
| [🎃]Climb For Animals Eggs🥚 | 48,430 | 2026-09-06 | Simulation | 5.00 | 0.99 | 5 | 0 |
| Illegal Soccer | 44,977 | 2026-05-12 | Sports & Racing | 8.00 | 0.87 | 2 | 1 |

Genre mix of the top 100:

| genre | games | playing |
|---|---|---|
| Simulation | 35 | 2,812,711 |
| Survival | 19 | 1,151,042 |
| Roleplay & Avatar Sim | 11 | 920,949 |
| Action | 7 | 341,436 |
| RPG | 3 | 265,868 |
| Shooter | 5 | 261,178 |
| Strategy | 5 | 169,630 |
| Obby & Platformer | 3 | 147,063 |
| Sports & Racing | 3 | 114,633 |
| Shopping | 2 | 76,074 |
| All | 2 | 51,524 |
| Party & Casual | 2 | 46,330 |
| Adventure | 2 | 41,995 |
| Entertainment | 1 | 30,910 |

## B. Launch trajectories (games created since late June 2026, full history observed)

| name | created | peak_ccu | days_to_peak | days_to_1k | days_to_10k | days_to_100k | days_to_1M | growth_per_day_1k_to_peak | doubling_days | now | now_over_peak |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Steal An Egg | 2026-07-25 | 7,149,306 | 56.30 | 11.70 | 12.00 | 19.10 | 28.20 | 0.11 | 6.49 | 1,285,170 | 0.18 |
| Break and Steal an Egg | 2026-09-05 | 536,611 | 42.60 | 22.50 | 22.50 | 28.70 |  | 0.14 | 5.08 | 140,261 | 0.26 |
| [🍲] Karinderya! | 2026-08-07 | 150,093 | 42.90 | 16.60 | 16.80 | 42.90 |  | 0.06 | 11.86 | 13,859 | 0.09 |
| The Hollow | 2026-10-13 | 139,289 | 9.00 | 8.80 | 8.80 | 8.80 |  |  |  | 30,910 | 0.22 |
| 🍂🎃 Clean all the Leaves | 2026-07-21 | 136,319 | 39.40 | 23.00 | 23.30 | 26.50 |  | 0.07 | 9.58 | 5,489 | 0.04 |
| [Pt. 3 🎃] Huss Valley | 2026-08-31 | 136,041 | 41.00 | 29.60 | 30.90 | 33.90 |  | 0.20 | 3.49 | 42,064 | 0.31 |
| [NEW STAGES]  DONT SPLASH 🎃 | 2026-10-17 | 108,742 | 8.50 | 3.20 | 4.10 | 8.30 |  | 0.56 | 1.24 | 90,782 | 0.83 |
| 🎃 Sell Fries! [Anomaly] 🍟 | 2026-09-21 | 104,668 | 26.10 | 13.90 | 18.00 | 26.10 |  | 0.32 | 2.18 | 52,558 | 0.50 |
| [🎃]+1 Loot To Forge | 2026-08-12 | 95,161 | 46.40 | 35.30 | 35.30 |  |  | 0.16 | 4.30 | 10,488 | 0.11 |
| [🎃]Climb For Animals Eggs🥚 | 2026-09-06 | 95,070 | 40.50 | 30.30 | 30.30 |  |  | 0.19 | 3.65 | 48,430 | 0.51 |
| [🎃] Anime Dice | 2026-08-15 | 89,352 | 71.60 | 17.30 | 22.30 |  |  | 0.04 | 15.89 | 85,207 | 0.95 |
| [🎃] +1 Stone Skipping | 2026-09-05 | 88,512 | 34.80 | 21.00 | 22.90 |  |  | 0.17 | 4.18 | 19,845 | 0.22 |
| Sarab | 2026-09-24 | 86,688 | 15.20 | 9.00 | 9.00 |  |  | 0.11 | 6.28 | 12,388 | 0.14 |
| صيد الضبّان | 2026-10-03 | 82,771 | 18.90 | 7.50 | 7.80 |  |  | 0.12 | 5.76 | 33,784 | 0.41 |
| [IMPOSSIBLE 😈] Search For The Needle | 2026-08-23 | 82,068 | 21.20 | 9.80 | 11.00 |  |  | 0.15 | 4.53 | 8,490 | 0.10 |
| Build and Kill Zombies | 2026-08-19 | 80,704 | 37.80 | 21.30 | 23.80 |  |  | 0.18 | 3.81 | 4,180 | 0.05 |
| [🎃] Fake an Egg | 2026-10-04 | 79,934 | 20.70 | 12.40 | 12.40 |  |  | 0.15 | 4.73 | 31,461 | 0.39 |
| [🎃] Bike Universe | 2026-09-27 | 74,362 | 28.20 | 19.60 | 21.00 |  |  | 0.31 | 2.25 | 44,328 | 0.60 |
| [🎃] Bike For Egg! | 2026-09-15 | 70,582 | 38.50 | 31.10 | 31.10 |  |  | 0.07 | 9.65 | 32,455 | 0.46 |
| [🎃] Ride a Dino | 2026-08-24 | 68,679 | 62.10 | 51.60 | 53.60 |  |  | 0.24 | 2.83 | 37,719 | 0.55 |
| [🎃] Chop A Forest | 2026-09-21 | 68,451 | 26.00 | 15.90 | 22.10 |  |  | 0.46 | 1.50 | 28,326 | 0.41 |
| Cat Battles 🐾 | 2026-10-05 | 67,065 | 18.80 | 3.10 | 11.20 |  |  | 0.24 | 2.87 | 31,415 | 0.47 |
| [🎃] Ball VS Ball | 2026-08-12 | 62,176 | 60.40 | 21.10 | 23.30 |  |  | 0.05 | 13.32 | 25,141 | 0.40 |
| [👻] Tap Simulator REBORN | 2026-08-04 | 59,414 | 81.90 | 67.40 | 70.80 |  |  | 0.17 | 4.08 | 50,293 | 0.85 |
| [🎃] +1 Cut Grass Adventure | 2026-06-28 | 57,257 | 54.10 | 38.60 | 40.70 |  |  | 0.11 | 6.03 | 3,034 | 0.05 |
| Ragdoll Reality 🩸 | 2026-10-13 | 57,084 | 11.50 | 5.70 | 9.90 |  |  | 0.72 | 0.96 | 39,892 | 0.70 |
| Anime Zero [SOLAR RADIANCE ☀️] | 2026-07-16 | 57,057 | 87.00 | 78.30 | 80.80 |  |  | 0.27 | 2.54 | 5,736 | 0.10 |
| [☁️WORLD 2] +1 Tongue Escape😛 | 2026-08-11 | 55,358 | 32.90 | 23.30 | 25.70 |  |  | 0.32 | 2.17 | 6,892 | 0.12 |
| [🎃] Kukirin Life [Testing] | 2026-09-19 | 54,790 | 35.80 | 17.30 | 18.80 |  |  | 0.12 | 5.68 | 38,776 | 0.71 |
| [🔥TRADES+X2 EXP💎}Cameraman Tower Defense | 2026-08-26 | 54,383 | 60.80 | 34.90 | 43.90 |  |  | 0.13 | 5.26 | 53,086 | 0.98 |
| [🎃] Facecard: Makeup Showdown | 2026-10-05 | 53,662 | 12.90 | 4.20 | 6.80 |  |  | 0.30 | 2.35 | 13,258 | 0.25 |
| Backseat Rally | 2026-10-05 | 52,417 | 18.70 | 12.10 | 12.40 |  |  | 0.18 | 3.95 | 32,547 | 0.62 |
| Bunker vs Verity | 2026-09-22 | 51,145 | 25.30 | 15.50 | 16.30 |  |  | 0.13 | 5.41 | 13,478 | 0.26 |
| [UPD] Drive A Kukirin! | 2026-08-05 | 49,689 | 66.40 | 22.90 | 30.40 |  |  | 0.03 | 19.86 | 13,827 | 0.28 |
| TROLL Hug Tower | 2026-07-07 | 48,035 | 40.50 | 25.00 | 25.00 |  |  | 0.08 | 8.31 | 14,393 | 0.30 |
| [UPD🎃] Paint to Get Rich 🎨 | 2026-08-20 | 42,364 | 44.10 | 43.40 | 43.40 |  |  |  |  | 12,180 | 0.29 |
| [🎃] +1 Venom Evolution | 2026-10-05 | 39,905 | 20.20 | 11.70 | 13.20 |  |  | 0.21 | 3.29 | 23,266 | 0.58 |
| Steel Fighters | 2026-09-07 | 39,096 | 46.60 | 41.30 | 42.80 |  |  | 0.45 | 1.53 | 21,470 | 0.55 |
| [🎃] Jump To Steal An Egg | 2026-08-18 | 38,808 | 32.80 | 22.60 | 22.80 |  |  | 0.07 | 10.64 | 3,475 | 0.09 |
| 7 Days Cat-Sitting | 2026-09-15 | 38,692 | 33.60 | 13.50 | 14.90 |  |  | 0.04 | 16.44 | 17,775 | 0.46 |

## C. Format waves (title keyword clusters)

| token | games | first | leader_now | leader_is_first | total_playing | created_last_120d |
|---|---|---|---|---|---|---|
| steal | 16 | [💀] Steal a Brainrot (2025-05-16) | Steal An Egg (2026-07-25) | 0 | 1,726,480 | 13 |
| egg | 8 | [🎃BOSS] Break a Brainrot Egg! (2026-01-02) | Steal An Egg (2026-07-25) | 0 | 1,511,235 | 7 |
| murder | 3 | Murder Mystery 2 (2014-01-18) | Murder Mystery 2 (2014-01-18) | 1 | 298,507 | 0 |
| simulator | 22 | Pilot Training Flight Simulator (2010-01-04) | 🎉 [PSX] Pet Simulator 99! 🐾 (2022-02-05) | 0 | 274,851 | 5 |
| forest | 3 | 99 Nights in the Forest 🔦 (2025-03-04) | 99 Nights in the Forest 🔦 (2025-03-04) | 1 | 267,153 | 1 |
| anime | 19 | [🎃] Anime Dimensions Simulator (2021-06-11) | [🎃] Anime Dice (2026-08-15) | 0 | 251,166 | 8 |
| rivals | 4 | [🎃] RIVALS (2024-05-26) | [🎃] RIVALS (2024-05-26) | 1 | 196,507 | 1 |
| break | 3 | [🎃BOSS] Break a Brainrot Egg! (2026-01-02) | Break and Steal an Egg (2026-09-05) | 0 | 151,815 | 1 |
| pet | 4 | 🎉 [PSX] Pet Simulator 99! 🐾 (2022-02-05) | 🎉 [PSX] Pet Simulator 99! 🐾 (2022-02-05) | 1 | 134,673 | 1 |
| escape | 11 | Escape Running Head (2021-01-07) | [X50] +1 Speed Keyboard Escape | Candy & Chocolate (2026-01-18) | 0 | 106,008 | 1 |
| tower defense | 10 | [🌙 NIGHT 3] Tower Defense Simulator (2019-06-05) | [🔥TRADES+X2 EXP💎}Cameraman Tower Defense (2026-08-26) | 0 | 101,576 | 1 |
| survive | 10 | 🔪Survive the Killer! (2020-01-06) | 🎃 Creatures of Sonaria 🍬 Survive Kaiju Animals (2020-06-25) | 0 | 94,828 | 3 |
| fish | 3 | [🎃UPD] Fish It! 🐟 (2024-10-21) | [🎃UPD] Fish It! 🐟 (2024-10-21) | 1 | 83,012 | 0 |
| tycoon | 11 | 🌳 Lumber Tycoon 2 (2009-07-30) | Pet Store Tycoon (2026-06-06) | 0 | 67,800 | 1 |
| rng | 7 | Sol's RNG [ Radiant Forest🌙] (2023-12-03) | Sol's RNG [ Radiant Forest🌙] (2023-12-03) | 1 | 50,771 | 2 |
| grow | 3 | [🎃] Grow a Garden 🌶️ (2025-03-25) | [🎃] Grow a Garden 🌶️ (2025-03-25) | 1 | 32,740 | 1 |
| obby | 5 | Easy Mega Obby (2023-05-13) | [HELL] Spiral Difficulty Chart Obby (2026-01-20) | 0 | 23,631 | 2 |
| hide | 3 | Hide and Seek Extreme (2015-01-18) | [FANTASTIC 4] Hide From The Hulk (2026-09-30) | 0 | 9,464 | 2 |

## D. Holding players: games older than 6 months with >= 5k peak since June

- Correlation (Spearman) of 'now / peak since June' with name changes in last 90 days: -0.20 (n=319).
- Median now/peak: with >= 3 name changes in 90 days 0.37 (n=27); with 0-2: 0.40 (n=292).

## E. Monetization and social structure by size tier

| tier | games | median_passes | median_pass_price | median_max_pass | median_like_ratio | median_max_players | median_rw_rev_usd_per_ccu_day (RoWatcher est.) |
|---|---|---|---|---|---|---|---|
| <1k | 36 | 5.00 | 200 | 799 | 0.83 | 26.50 | 0.15 |
| 1k-10k | 422 | 6.00 | 224 | 499 | 0.90 | 16.00 | 0.38 |
| 10k-100k | 159 | 6.00 | 222 | 599 | 0.92 | 16.00 | 0.37 |
| 100k+ | 11 | 3.00 | 381 | 772 | 0.91 | 12.00 | 0.25 |

## F. The bar for Up-and-Coming today

- 94 games; median age 22 days (max 139); median live players 5,375 (min 774); median like ratio 0.88.

| name | created | age_days | playing_now | like_ratio | genre |
|---|---|---|---|---|---|
| [NEW STAGES]  DONT SPLASH 🎃 | 2026-10-17 | 8.00 | 90,782 | 0.89 | Obby & Platformer |
| [👻] Tap Simulator REBORN | 2026-08-04 | 82.00 | 50,293 | 0.95 | Simulation |
| Ragdoll Reality 🩸 | 2026-10-13 | 12.00 | 39,892 | 0.83 | Simulation |
| [🎃] Kukirin Life [Testing] | 2026-09-19 | 36.00 | 38,776 | 0.84 | Simulation |
| صيد الضبّان | 2026-10-03 | 22.00 | 33,784 | 0.95 | Simulation |
| Backseat Rally | 2026-10-05 | 20.00 | 32,547 | 0.92 | All |
| [🎃] Fake an Egg | 2026-10-04 | 21.00 | 31,461 | 0.89 | Simulation |
| Cat Battles 🐾 | 2026-10-05 | 20.00 | 31,415 | 0.73 | Action |
| The Hollow | 2026-10-13 | 12.00 | 30,910 | 0.84 | Entertainment |
| [🎃] +1 Venom Evolution | 2026-10-05 | 20.00 | 23,266 | 0.97 | Simulation |
| Steel Fighters | 2026-09-07 | 48.00 | 21,470 | 0.91 | Simulation |
| Wash the Car 🧽 | 2026-08-16 | 70.00 | 19,176 | 0.88 | Simulation |
| Save the Krusty Krab 🍔 | 2026-09-29 | 26.00 | 17,215 | 0.94 | Survival |
| Clone Baby Care (Anomaly) | 2026-10-09 | 16.00 | 16,478 | 0.89 | Survival |
| Crazy Diver | 2026-09-24 | 31.00 | 16,379 | 0.58 | Simulation |
| A Long Flight [SANDBOX]  | 2026-09-30 | 25.00 | 16,357 | 0.73 | Survival |
| [UPD] Realistic Ragdoll Engine 🩸 | 2026-10-12 | 13.00 | 15,681 | 0.89 | Simulation |
| What If Disasters | 2026-10-05 | 20.00 | 15,545 | 0.91 | Survival |
| [🎃] +1 Upgrade Per Kill | 2026-09-27 | 28.00 | 13,553 | 0.47 | Action |
| [🎃] Eat Everything In A Grocery Store | 2026-10-03 | 22.00 | 13,085 | 0.90 | Simulation |
| [🎃] +1 Pickaxe Swing for Eggs | 2026-09-27 | 28.00 | 13,040 | 0.92 | Simulation |
| Sarab | 2026-09-24 | 31.00 | 12,388 | 0.89 | Survival |
| [UPD] Something is Wrong With My Dog... | 2026-08-26 | 60.00 | 9,903 | 0.77 | Adventure |
| [🎃] Roll A Stickman! | 2026-09-10 | 45.00 | 9,777 | 0.96 | Simulation |
| [🎃EVENT] Solve The Cube | 2026-10-04 | 21.00 | 9,095 | 0.81 | Puzzle |

