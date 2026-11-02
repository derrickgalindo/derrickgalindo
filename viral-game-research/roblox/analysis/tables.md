# Roblox deep dive: tables (n=657 games, snapshot 2026-11-02)

## A. Who is on top

- Top 100 by live players: median age 1.5 years; created in the last 120 days: 37; last 365 days: 48; older than 3 years: 28.
- Games at or above ~1M-DAU scale now (>= 75,000 concurrent): 17.

| name | playing_now | created | genre | max_players | like_ratio | n_passes | name_changes_90d |
|---|---|---|---|---|---|---|---|
| Steal An Egg | 1,054,007 | 2026-07-25 | Simulation | 7.00 | 0.91 | 2 | 2 |
| Brookhaven 🏡RP | 448,657 | 2020-04-21 | Roleplay & Avatar Sim | 30.00 | 0.86 | 18 | 0 |
| Murder Mystery 2 | 377,530 | 2014-01-18 | Survival | 12.00 | 0.91 | 3 | 0 |
| [🎃] Blox Fruits | 348,473 | 2019-01-16 | RPG | 12.00 | 0.92 | 6 | 1 |
| [1.2X🎃] Adopt Me! | 251,639 | 2017-07-14 | Roleplay & Avatar Sim | 35.00 | 0.86 | 6 | 37 |
| [🎃] RIVALS | 187,065 | 2024-05-26 | Shooter | 40.00 | 0.94 | 8 | 0 |
| 99 Nights in the Forest 🔦 | 182,997 | 2025-03-04 | Survival | 25.00 | 0.90 | 1 | 0 |
| Break and Steal an Egg | 162,165 | 2026-09-05 | Simulation | 7.00 | 0.97 | 0 | 0 |
| [🎃] Throw Food For Animals | 140,594 | 2026-09-18 | Simulation | 5.00 | 0.94 | 2 | 0 |
| [☀️UPD 21🏖️] Anime Adventures | 103,712 | 2021-12-21 | Strategy | 30.00 | 0.92 | 5 | 1 |
| [HALLOWEEN] The Strongest Battlegrounds | 98,008 | 2022-08-02 | Action | 15.00 | 0.84 | 7 | 0 |
| [🎃] Jujutsu Shenanigans | 97,058 | 2022-04-17 | Action | 25.00 | 0.86 | 5 | 0 |
| [💀] Steal a Brainrot | 91,508 | 2025-05-16 | Simulation | 8.00 | 0.85 | 3 | 2 |
| DONT SPLASH | 91,238 | 2026-10-17 | Obby & Platformer | 10.00 | 0.87 | 12 | 0 |
| Fisch 🎸 [VENUE ENCORE] | 90,322 | 2024-03-13 | Simulation | 20.00 | 0.91 | 9 | 2 |
| 🎃 Dandy's World [ALPHA] | 82,737 | 2024-01-26 | Survival | 35.00 | 0.88 | 7 | 0 |
| [WEEK 2 🎃 x BUTCHER] Violence District | 81,915 | 2024-10-31 | Survival | 6.00 | 0.93 | 2 | 0 |
| 🎃 [MINIGAMES] Pet Simulator 99! 👻 | 73,666 | 2022-02-05 | Simulation | 10.00 | 0.95 | 13 | 3 |
| [🎃THE HOLLOW🎃] Evade  | 68,098 | 2022-06-10 | Survival | 15.00 | 0.94 | 26 | 2 |
| [👻UPD] Fish It! 🐟 | 65,483 | 2024-10-21 | Simulation | 20.00 | 0.83 | 12 | 16 |
| [🎃] Dress To Impress | 60,133 | 2023-10-18 | Roleplay & Avatar Sim | 13.00 | 0.91 | 14 | 1 |
| The Hollow | 57,346 | 2026-10-13 | Entertainment | 20.00 | 0.85 | 0 | 0 |
| Catalog Avatar Creator | 55,686 | 2021-07-03 | Shopping | 24.00 | 0.94 | 0 | 0 |
| [UPD] Volleyball Legends | 55,583 | 2024-12-17 | Sports & Racing | 12.00 | 0.95 | 3 | 0 |
| [⭐UPD 11] Anime Dice | 53,755 | 2026-08-15 | Simulation | 9.00 | 0.99 | 8 | 1 |
| صيد الضبّان | 50,528 | 2026-10-03 | Simulation | 8.00 | 0.95 | 6 | 0 |
| [UPDATE 5] Attack on Titan Revolution | 47,036 | 2023-05-07 | RPG | 30.00 | 0.96 | 12 | 1 |
| [GO-KART!] Illegal Soccer | 45,951 | 2026-05-12 | Sports & Racing | 8.00 | 0.87 | 2 | 1 |
| Fling Things and People | 45,546 | 2021-06-16 | Simulation | 25.00 | 0.80 | 7 | 0 |
| Sol's RNG [ Halloween Event 🎃] | 41,537 | 2023-12-03 | Simulation | 20.00 | 0.91 | 7 | 0 |

Genre mix of the top 100:

| genre | games | playing |
|---|---|---|
| Simulation | 36 | 2,563,663 |
| Survival | 16 | 1,078,740 |
| Roleplay & Avatar Sim | 10 | 908,733 |
| RPG | 2 | 395,509 |
| Action | 8 | 322,415 |
| Shooter | 6 | 291,962 |
| Strategy | 4 | 192,580 |
| Obby & Platformer | 4 | 161,606 |
| Sports & Racing | 4 | 139,885 |
| Shopping | 2 | 73,266 |
| Adventure | 3 | 58,439 |
| Entertainment | 1 | 57,346 |
| All | 2 | 46,597 |
| Party & Casual | 2 | 43,176 |

## B. Launch trajectories (games created since late June 2026, full history observed)

| name | created | peak_ccu | days_to_peak | days_to_1k | days_to_10k | days_to_100k | days_to_1M | growth_per_day_1k_to_peak | doubling_days | now | now_over_peak |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Steal An Egg | 2026-07-25 | 7,149,306 | 56.30 | 11.70 | 12.00 | 19.10 | 28.20 | 0.11 | 6.49 | 1,054,007 | 0.15 |
| Break and Steal an Egg | 2026-09-05 | 536,611 | 42.60 | 22.50 | 22.50 | 28.70 |  | 0.14 | 5.08 | 162,165 | 0.30 |
| DONT SPLASH | 2026-10-17 | 163,991 | 15.40 | 3.20 | 4.10 | 8.30 |  | 0.21 | 3.25 | 91,238 | 0.56 |
| [🎃] Throw Food For Animals | 2026-09-18 | 163,373 | 42.70 | 32.50 | 35.20 | 41.50 |  | 0.44 | 1.58 | 140,594 | 0.86 |
| The Hollow | 2026-10-13 | 160,467 | 17.70 | 8.80 | 8.80 | 8.80 |  | 0.01 | 101 | 57,346 | 0.36 |
| [🍲] Karinderya! | 2026-08-07 | 150,093 | 42.90 | 16.60 | 16.80 | 42.90 |  | 0.06 | 11.86 | 11,313 | 0.08 |
| 🍂🎃 Clean all the Leaves | 2026-07-21 | 136,319 | 39.40 | 23.00 | 23.30 | 26.50 |  | 0.07 | 9.58 | 4,164 | 0.03 |
| [BOSS🎃] Huss Valley | 2026-08-31 | 136,041 | 41.00 | 29.60 | 30.90 | 33.90 |  | 0.20 | 3.49 | 31,257 | 0.23 |
| [CH2] Sell Fries! [Anomaly] 🍟 | 2026-09-21 | 104,668 | 26.10 | 13.90 | 18.00 | 26.10 |  | 0.32 | 2.18 | 38,106 | 0.36 |
| [🎃]+1 Loot To Forge | 2026-08-12 | 95,161 | 46.40 | 35.30 | 35.30 |  |  | 0.16 | 4.30 | 4,936 | 0.05 |
| [🎃]Climb For Animals Eggs🥚 | 2026-09-06 | 95,070 | 40.50 | 30.30 | 30.30 |  |  | 0.19 | 3.65 | 33,387 | 0.35 |
| [🎃] Fake an Egg | 2026-10-04 | 93,481 | 27.70 | 12.40 | 12.40 |  |  | 0.09 | 7.54 | 35,547 | 0.38 |
| [⭐UPD 11] Anime Dice | 2026-08-15 | 89,352 | 71.60 | 17.30 | 22.30 |  |  | 0.04 | 15.89 | 53,755 | 0.60 |
| [🎃] +1 Stone Skipping | 2026-09-05 | 88,512 | 34.80 | 21.00 | 22.90 |  |  | 0.17 | 4.18 | 9,448 | 0.11 |
| Sarab | 2026-09-24 | 86,688 | 15.20 | 9.00 | 9.00 |  |  | 0.11 | 6.28 | 6,697 | 0.08 |
| صيد الضبّان | 2026-10-03 | 82,771 | 18.90 | 7.50 | 7.80 |  |  | 0.12 | 5.76 | 50,528 | 0.61 |
| [CHAPTER 5] Search For The Needle | 2026-08-23 | 82,068 | 21.20 | 9.80 | 11.00 |  |  | 0.15 | 4.53 | 4,202 | 0.05 |
| Kukirin Life [Testing] | 2026-09-19 | 80,940 | 40.90 | 17.30 | 18.80 |  |  | 0.09 | 7.93 | 31,589 | 0.39 |
| [🎃] Bike For Egg! | 2026-09-15 | 78,398 | 45.50 | 31.10 | 31.10 |  |  | 0.05 | 15.19 | 36,336 | 0.46 |
| 🛡️[S1] Bike Universe | 2026-09-27 | 74,362 | 28.20 | 19.60 | 21.00 |  |  | 0.31 | 2.25 | 31,512 | 0.42 |
| [♾️] Ride a Dino | 2026-08-24 | 68,679 | 62.10 | 51.60 | 53.60 |  |  | 0.24 | 2.83 | 16,797 | 0.24 |
| Chop A Forest | 2026-09-21 | 68,451 | 26.00 | 15.90 | 22.10 |  |  | 0.46 | 1.50 | 14,477 | 0.21 |
| [🎃] Steal A Pet And Ride It! | 2026-10-04 | 67,450 | 27.10 | 20.50 | 21.00 |  |  | 0.26 | 2.69 | 38,303 | 0.57 |
| Cat Battles 🐾 | 2026-10-05 | 67,065 | 18.80 | 3.10 | 11.20 |  |  | 0.24 | 2.87 | 13,635 | 0.20 |
| Ball VS Ball [RANKED] | 2026-08-12 | 62,176 | 60.40 | 21.10 | 23.30 |  |  | 0.05 | 13.32 | 22,248 | 0.36 |
| [✨] Tap Simulator REBORN | 2026-08-04 | 59,414 | 81.90 | 67.40 | 70.80 |  |  | 0.17 | 4.08 | 39,630 | 0.67 |
| Ragdoll Reality 🩸 | 2026-10-13 | 57,084 | 11.50 | 5.70 | 9.90 |  |  | 0.72 | 0.96 | 25,334 | 0.44 |
| [UPD 6] Anime Zero | 2026-07-16 | 57,057 | 87.00 | 78.30 | 80.80 |  |  | 0.27 | 2.54 | 3,694 | 0.06 |
| +1 Spider Arm🕷️ | 2026-10-19 | 56,341 | 11.60 | 10.10 | 10.10 |  |  | 0.53 | 1.32 | 36,436 | 0.65 |
| [UPD🎃] +1 Venom Evolution | 2026-10-05 | 55,874 | 27.30 | 11.70 | 13.20 |  |  | 0.11 | 6.17 | 37,711 | 0.67 |
| [☁️WORLD 2] +1 Tongue Escape😛 | 2026-08-11 | 55,358 | 32.90 | 23.30 | 25.70 |  |  | 0.32 | 2.17 | 5,033 | 0.09 |
| [🎃] Facecard: Makeup Showdown | 2026-10-05 | 53,662 | 12.90 | 4.20 | 6.80 |  |  | 0.30 | 2.35 | 7,506 | 0.14 |
| [💰X2] Cameraman Tower Defense | 2026-08-26 | 52,842 | 57.80 | 34.90 | 43.90 |  |  | 0.14 | 4.91 | 38,094 | 0.72 |
| Backseat Rally | 2026-10-05 | 52,417 | 18.70 | 12.10 | 12.40 |  |  | 0.18 | 3.95 | 26,313 | 0.50 |
| Bunker vs Verity | 2026-09-22 | 51,145 | 25.30 | 15.50 | 16.30 |  |  | 0.13 | 5.41 | 5,916 | 0.12 |
| [NOW🗺️] Drive A Kukirin! | 2026-08-05 | 49,689 | 66.40 | 22.90 | 30.40 |  |  | 0.03 | 19.86 | 7,454 | 0.15 |
| TROLL Hug Tower | 2026-07-07 | 48,035 | 40.50 | 26.40 | 26.40 |  |  | 0.09 | 8.06 | 16,818 | 0.35 |
| [🌍UPD] +1 Anime Eyes | 2026-10-14 | 48,032 | 15.70 | 13.00 | 13.00 |  |  | 0.42 | 1.65 | 31,051 | 0.65 |
| Bug Evolution [🕷️] | 2026-10-09 | 44,747 | 23.40 | 17.90 | 19.20 |  |  | 0.34 | 2.01 | 27,503 | 0.61 |
| [UPD] Paint to Get Rich 🎨 | 2026-08-20 | 42,364 | 44.10 | 43.40 | 43.40 |  |  |  |  | 7,686 | 0.18 |

## C. Format waves (title keyword clusters)

| token | games | first | leader_now | leader_is_first | total_playing | created_last_120d |
|---|---|---|---|---|---|---|
| steal | 16 | [💀] Steal a Brainrot (2025-05-16) | Steal An Egg (2026-07-25) | 0 | 1,400,022 | 12 |
| egg | 7 | [🎃BOSS] Break a Brainrot Egg! (2026-01-02) | Steal An Egg (2026-07-25) | 0 | 1,305,295 | 6 |
| murder | 3 | Murder Mystery 2 (2014-01-18) | Murder Mystery 2 (2014-01-18) | 1 | 394,392 | 0 |
| anime | 22 | [🎃] Anime Dimensions Simulator (2021-06-11) | [☀️UPD 21🏖️] Anime Adventures (2021-12-21) | 0 | 303,023 | 11 |
| simulator | 19 | Pilot Training Flight Simulator (2010-01-04) | 🎃 [MINIGAMES] Pet Simulator 99! 👻 (2022-02-05) | 0 | 276,776 | 4 |
| rivals | 4 | [🎃] RIVALS (2024-05-26) | [🎃] RIVALS (2024-05-26) | 1 | 223,221 | 1 |
| forest | 3 | 99 Nights in the Forest 🔦 (2025-03-04) | 99 Nights in the Forest 🔦 (2025-03-04) | 1 | 201,350 | 1 |
| pet | 5 | 🎃 [MINIGAMES] Pet Simulator 99! 👻 (2022-02-05) | 🎃 [MINIGAMES] Pet Simulator 99! 👻 (2022-02-05) | 1 | 142,146 | 2 |
| tower defense | 9 | [🌙 NIGHT 4] Tower Defense Simulator (2019-06-05) | [💰X2] Cameraman Tower Defense (2026-08-26) | 0 | 103,304 | 1 |
| escape | 15 | Escape Running Head (2021-01-07) | +1 Speed Keyboard Escape | Candy & Chocolate (2026-01-18) | 0 | 99,216 | 4 |
| survive | 10 | 🔪Survive the Killer! (2020-01-06) | 🎃 Creatures of Sonaria 🍬 Survive Kaiju Animals (2020-06-25) | 0 | 77,289 | 2 |
| fish | 4 | [👻UPD] Fish It! 🐟 (2024-10-21) | [👻UPD] Fish It! 🐟 (2024-10-21) | 1 | 73,539 | 1 |
| tycoon | 11 | 🌳 Lumber Tycoon 2 (2009-07-30) | [🍬] Restaurant Tycoon 3 (2025-01-16) | 0 | 57,730 | 1 |
| rng | 5 | Sol's RNG [ Halloween Event 🎃] (2023-12-03) | Sol's RNG [ Halloween Event 🎃] (2023-12-03) | 1 | 51,815 | 1 |
| garden | 3 | [🎃] Grow a Garden 🌶️ (2025-03-25) | [UPD] Durian Garden 🍈 (2026-10-21) | 0 | 49,128 | 1 |
| hide | 4 | [🏜] Fly Hide & Seek (2025-11-10) | Hide to Steal Eggs (2026-10-06) | 0 | 20,128 | 3 |

## D. Holding players: games older than 6 months with >= 5k peak since June

- Correlation (Spearman) of 'now / peak since June' with name changes in last 90 days: -0.16 (n=315).
- Median now/peak: with >= 3 name changes in 90 days 0.31 (n=21); with 0-2: 0.39 (n=294).

## E. Monetization and social structure by size tier

| tier | games | median_passes | median_pass_price | median_max_pass | median_like_ratio | median_max_players | median_rw_rev_usd_per_ccu_day (RoWatcher est.) |
|---|---|---|---|---|---|---|---|
| <1k | 33 | 4.00 | 300 | 900 | 0.86 | 20.00 | 0.10 |
| 1k-10k | 442 | 6.00 | 229 | 500 | 0.90 | 18.00 | 0.40 |
| 10k-100k | 156 | 6.00 | 239 | 500 | 0.91 | 16.00 | 0.40 |
| 100k+ | 10 | 4.00 | 388 | 795 | 0.92 | 18.50 | 0.20 |

## F. The bar for Up-and-Coming today

- 97 games; median age 22 days (max 132); median live players 6,636 (min 613); median like ratio 0.87.

| name | created | age_days | playing_now | like_ratio | genre |
|---|---|---|---|---|---|
| DONT SPLASH | 2026-10-17 | 15.00 | 91,238 | 0.87 | Obby & Platformer |
| The Hollow | 2026-10-13 | 19.00 | 57,346 | 0.85 | Entertainment |
| [🎃] Steal A Pet And Ride It! | 2026-10-04 | 28.00 | 38,303 | 0.95 | Simulation |
| [UPD🎃] +1 Venom Evolution | 2026-10-05 | 27.00 | 37,711 | 0.97 | Simulation |
| +1 Spider Arm🕷️ | 2026-10-19 | 13.00 | 36,436 | 0.97 | Simulation |
| [🎃] Fake an Egg | 2026-10-04 | 28.00 | 35,547 | 0.89 | Simulation |
| [🌍UPD] +1 Anime Eyes | 2026-10-14 | 18.00 | 31,051 | 0.96 | Simulation |
| Bug Evolution [🕷️] | 2026-10-09 | 23.00 | 27,503 | 0.78 | Survival |
| Backseat Rally | 2026-10-05 | 27.00 | 26,313 | 0.92 | All |
| Ragdoll Reality 🩸 | 2026-10-13 | 19.00 | 25,334 | 0.83 | Simulation |
| 🧸 My Small Business | 2026-10-17 | 15.00 | 23,009 | 0.96 | Simulation |
| Realistic Ragdoll Engine 🩸 | 2026-10-12 | 20.00 | 20,552 | 0.88 | Simulation |
| [💉INJECTIONS] Ragdoll Playground | 2026-09-27 | 35.00 | 19,738 | 0.96 | Simulation |
| Criminal Simulator 💰 [ALPHA] | 2026-10-08 | 24.00 | 18,771 | 0.90 | Simulation |
| Clone Baby Care (Anomaly) | 2026-10-09 | 23.00 | 15,931 | 0.90 | Survival |
| Raise The Biggest Family | 2026-10-13 | 19.00 | 15,542 | 0.74 | Roleplay & Avatar Sim |
| [UPD4 💀] Depth Incremental | 2026-10-08 | 24.00 | 15,381 | 0.96 | Simulation |
| [🎃] Ragdoll Sandbox | 2026-10-16 | 16.00 | 14,643 | 0.83 | Simulation |
| [👽] What If Disasters | 2026-10-05 | 27.00 | 14,392 | 0.91 | Survival |
| Cat Battles 🐾 | 2026-10-05 | 27.00 | 13,635 | 0.73 | Action |
| [UPD] Realistic Car Destruction | 2026-10-15 | 17.00 | 12,804 | 0.78 | Simulation |
| Cook the Chicken (by slapping it) | 2026-10-06 | 26.00 | 12,655 | 0.79 | Simulation |
| Scare Your Neighbor | 2026-10-02 | 30.00 | 12,316 | 0.99 | Simulation |
| Night Rider 🏍️ [TESTING] | 2026-10-11 | 21.00 | 11,982 | 0.94 | Simulation |
| Hide to Steal Eggs | 2026-10-06 | 26.00 | 11,680 | 0.76 | Simulation |

