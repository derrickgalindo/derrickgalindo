# Roblox deep dive: tables (n=654 games, snapshot 2026-11-16)

## A. Who is on top

- Top 100 by live players: median age 1.3 years; created in the last 120 days: 41; last 365 days: 47; older than 3 years: 25.
- Games at or above ~1M-DAU scale now (>= 75,000 concurrent): 10.

| name | playing_now | created | genre | max_players | like_ratio | n_passes | name_changes_90d |
|---|---|---|---|---|---|---|---|
| Steal An Egg | 964,469 | 2026-07-25 | Simulation | 7.00 | 0.91 | 2 | 0 |
| Throw Food For Animals | 352,956 | 2026-09-18 | Simulation | 5.00 | 0.94 | 2 | 0 |
| [🎃] Blox Fruits | 331,586 | 2019-01-16 | RPG | 12.00 | 0.92 | 6 | 1 |
| Brookhaven 🏡RP | 326,325 | 2020-04-21 | Roleplay & Avatar Sim | 30.00 | 0.86 | 18 | 0 |
| [🥤] Adopt Me! | 212,218 | 2017-07-14 | Roleplay & Avatar Sim | 35.00 | 0.86 | 5 | 26 |
| 99 Nights in the Forest 🔦 | 159,504 | 2025-03-04 | Survival | 25.00 | 0.91 | 1 | 0 |
| [🎯] RIVALS | 141,060 | 2024-05-26 | Shooter | 40.00 | 0.94 | 8 | 0 |
| Murder Mystery 2 | 111,723 | 2014-01-18 | Survival | 12.00 | 0.91 | 3 | 0 |
| Break and Steal an Egg | 105,790 | 2026-09-05 | Simulation | 7.00 | 0.97 | 0 | 0 |
| [☀️UPD 21🏖️] Anime Adventures | 86,620 | 2021-12-21 | Strategy | 30.00 | 0.92 | 5 | 1 |
| [🎃] Jujutsu Shenanigans | 68,603 | 2022-04-17 | Action | 25.00 | 0.86 | 5 | 0 |
| [🏝️UPD] Fish It! 🐟 | 67,522 | 2024-10-21 | Simulation | 20.00 | 0.83 | 12 | 15 |
| [WEEK 4 🎃 x BUTCHER] Violence District | 63,749 | 2024-10-31 | Survival | 6.00 | 0.93 | 2 | 0 |
| Fisch 🎩 [COMPANION HATS] | 61,965 | 2024-03-13 | Simulation | 20.00 | 0.91 | 9 | 1 |
| 🍁 [TYCOON] Pet Simulator 99! 🍀 | 55,769 | 2022-02-05 | Simulation | 10.00 | 0.95 | 13 | 2 |
| [🎃HLWN🎃] Evade  | 55,367 | 2022-06-10 | Survival | 15.00 | 0.94 | 25 | 1 |
| 🌻 Dandy's World [ALPHA] | 55,033 | 2024-01-26 | Survival | 35.00 | 0.88 | 5 | 0 |
| [UPD🥳] Cameraman Tower Defense | 54,425 | 2026-08-26 | Strategy | 30.00 | 0.98 | 0 | 2 |
| [🗺️MAPS] Survive Your Ideas | 53,643 | 2026-10-06 | Survival | 40.00 | 0.89 | 6 | 0 |
| Forsaken | 52,565 | 2024-07-28 | Survival | 9.00 | 0.84 | 4 | 4 |
| [🐉UPD 11 PART 1🎃] King Legacy | 50,817 | 2019-12-17 | RPG | 12.00 | 0.92 | 0 | 0 |
| Catalog Avatar Creator | 50,354 | 2021-07-03 | Shopping | 24.00 | 0.94 | 0 | 0 |
| [HALLOWEEN] The Strongest Battlegrounds | 46,390 | 2022-08-02 | Action | 15.00 | 0.84 | 7 | 0 |
| [🎃] Dress To Impress | 44,187 | 2023-10-18 | Roleplay & Avatar Sim | 13.00 | 0.91 | 14 | 1 |
| [🏰] Tap Simulator REBORN | 43,872 | 2026-08-04 | Simulation | 10.00 | 0.94 | 10 | 4 |
| Attack on Titan Revolution | 43,826 | 2023-05-07 | RPG | 30.00 | 0.96 | 12 | 1 |
| (TOWING x LIMITED UPDATE 🎃) Drag Drive Simulator | 43,347 | 2025-01-15 | Simulation | 25.00 | 0.96 | 12 | 0 |
| [UPD] Volleyball Legends | 40,427 | 2024-12-17 | Sports & Racing | 12.00 | 0.95 | 4 | 0 |
| Sol's RNG [ Part 2 🎃 ] | 38,274 | 2023-12-03 | Simulation | 20.00 | 0.91 | 7 | 0 |
| Bee Swarm Simulator | 36,951 | 2018-03-21 | Simulation | 6.00 | 0.96 | 0 | 0 |

Genre mix of the top 100:

| genre | games | playing |
|---|---|---|
| Simulation | 36 | 2,315,904 |
| Survival | 16 | 734,693 |
| Roleplay & Avatar Sim | 7 | 661,902 |
| RPG | 6 | 487,139 |
| Action | 11 | 312,790 |
| Strategy | 6 | 236,492 |
| Shooter | 6 | 229,598 |
| Sports & Racing | 4 | 124,123 |
| Shopping | 2 | 65,887 |
| Obby & Platformer | 2 | 63,467 |
| All | 2 | 33,639 |
| Adventure | 2 | 31,829 |

## B. Launch trajectories (games created since late June 2026, full history observed)

| name | created | peak_ccu | days_to_peak | days_to_1k | days_to_10k | days_to_100k | days_to_1M | growth_per_day_1k_to_peak | doubling_days | now | now_over_peak |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Steal An Egg | 2026-07-25 | 7,149,306 | 56.30 | 22.20 | 22.20 | 22.20 | 28.20 | 0.07 | 9.41 | 964,469 | 0.13 |
| Throw Food For Animals | 2026-09-18 | 911,888 | 56.70 | 32.50 | 35.20 | 41.50 |  | 0.20 | 3.49 | 352,956 | 0.39 |
| Break and Steal an Egg | 2026-09-05 | 536,611 | 42.60 | 22.50 | 22.50 | 28.70 |  | 0.14 | 5.08 | 105,790 | 0.20 |
| DONT SPLASH | 2026-10-17 | 163,991 | 15.40 | 3.20 | 4.10 | 8.30 |  | 0.21 | 3.25 | 36,616 | 0.22 |
| [🍲] Karinderya! | 2026-08-07 | 150,093 | 42.90 | 16.60 | 16.80 | 42.90 |  | 0.06 | 11.86 | 4,936 | 0.03 |
| 🍂[♾️] Clean all the Leaves | 2026-07-21 | 136,319 | 39.40 | 26.40 | 26.40 | 31.40 |  | 0.03 | 23.70 | 2,984 | 0.02 |
| [🏆] Huss Valley | 2026-08-31 | 136,041 | 41.00 | 29.60 | 30.90 | 33.90 |  | 0.20 | 3.49 | 21,442 | 0.16 |
| Sell Fries! [Anomaly] 🍟 | 2026-09-21 | 104,668 | 26.10 | 13.90 | 18.00 | 26.10 |  | 0.32 | 2.18 | 15,196 | 0.15 |
| [🎃]+1 Loot To Forge | 2026-08-12 | 95,161 | 46.40 | 35.30 | 35.30 |  |  | 0.16 | 4.30 | 3,222 | 0.03 |
| Climb For Animals Eggs🥚 | 2026-09-06 | 95,070 | 40.50 | 30.30 | 30.30 |  |  | 0.19 | 3.65 | 14,378 | 0.15 |
| [🗺️MAPS] Survive Your Ideas | 2026-10-06 | 94,857 | 38.80 | 27.40 | 29.90 |  |  | 0.29 | 2.42 | 53,643 | 0.57 |
| [EXTINCT] Fake an Egg | 2026-10-04 | 93,481 | 27.70 | 12.40 | 12.40 |  |  | 0.09 | 7.54 | 8,400 | 0.09 |
| Anime Dice | 2026-08-15 | 89,352 | 71.60 | 17.30 | 22.30 |  |  | 0.04 | 15.89 | 25,795 | 0.29 |
| [🌅] +1 Stone Skipping | 2026-09-05 | 88,512 | 34.80 | 21.00 | 22.90 |  |  | 0.17 | 4.18 | 2,875 | 0.03 |
| Sarab | 2026-09-24 | 86,688 | 15.20 | 9.00 | 9.00 |  |  | 0.11 | 6.28 | 2,927 | 0.03 |
| صيد الضبّان | 2026-10-03 | 82,771 | 18.90 | 7.50 | 7.80 |  |  | 0.12 | 5.76 | 20,338 | 0.25 |
| Ragdoll Soccer | 2026-10-13 | 81,376 | 32.80 | 26.50 | 28.00 |  |  | 0.42 | 1.63 | 36,567 | 0.45 |
| Kukirin Life [Testing] | 2026-09-19 | 80,940 | 40.90 | 17.30 | 18.80 |  |  | 0.09 | 7.93 | 11,381 | 0.14 |
| Bike For Egg! | 2026-09-15 | 78,398 | 45.50 | 31.10 | 31.10 |  |  | 0.05 | 15.19 | 16,011 | 0.20 |
| [KENDURI] MALAM SAMA OPAH  | 2026-10-20 | 78,163 | 18.60 | 10.70 | 10.70 |  |  | 0.16 | 4.21 | 32,281 | 0.41 |
| 🗺️[MAPS] Bike Universe | 2026-09-27 | 74,362 | 28.20 | 19.60 | 21.00 |  |  | 0.31 | 2.25 | 11,572 | 0.16 |
| [UPD🥳] Cameraman Tower Defense | 2026-08-26 | 74,258 | 80.90 | 34.90 | 43.90 |  |  | 0.07 | 9.95 | 54,425 | 0.73 |
| [🌍UPD 5] +1 Venom Evolution | 2026-10-05 | 72,509 | 33.10 | 11.70 | 13.20 |  |  | 0.07 | 9.97 | 20,118 | 0.28 |
| [🤖] Ride a Dino | 2026-08-24 | 68,679 | 62.10 | 51.60 | 53.60 |  |  | 0.24 | 2.83 | 2,709 | 0.04 |
| Chop A Forest | 2026-09-21 | 68,451 | 26.00 | 15.90 | 22.10 |  |  | 0.46 | 1.50 | 3,400 | 0.05 |
| [W3🌸] Steal A Pet And Ride It! | 2026-10-04 | 68,359 | 35.10 | 20.50 | 21.00 |  |  | 0.06 | 12.27 | 14,390 | 0.21 |
| Cat Battles 🐾 | 2026-10-05 | 67,065 | 18.80 | 3.10 | 11.20 |  |  | 0.24 | 2.87 | 3,020 | 0.05 |
| Ball VS Ball [Trading Plaza] | 2026-08-12 | 62,176 | 60.40 | 21.10 | 23.30 |  |  | 0.05 | 13.32 | 11,555 | 0.19 |
| [🏰] Tap Simulator REBORN | 2026-08-04 | 59,414 | 81.90 | 67.40 | 70.80 |  |  | 0.17 | 4.08 | 43,872 | 0.74 |
| [UPDATE & EXPANDED MAP] Onthel Purwodadi | 2026-10-17 | 59,331 | 26.10 | 18.60 | 18.70 |  |  | 0.05 | 13.27 | 6,481 | 0.11 |
| Bloody Ragdoll Physics 🩸 | 2026-10-31 | 59,036 | 15.50 | 6.90 | 9.50 |  |  | 0.37 | 1.87 | 33,919 | 0.57 |
| Ragdoll Reality 🩸 | 2026-10-13 | 57,084 | 11.50 | 5.70 | 9.90 |  |  | 0.72 | 0.96 | 6,468 | 0.11 |
| +1 Spider Arm🕷️ | 2026-10-19 | 56,341 | 11.60 | 10.10 | 10.10 |  |  | 0.53 | 1.32 | 8,165 | 0.14 |
| [🎀Accessories] Facecard: Makeup Showdown | 2026-10-05 | 53,662 | 12.90 | 4.20 | 6.80 |  |  | 0.30 | 2.35 | 4,345 | 0.08 |
| Unstable SMP FFA [JAVA PVP!] | 2026-10-21 | 53,613 | 23.80 | 14.60 | 16.40 |  |  | 0.25 | 2.81 | 32,627 | 0.61 |
| Backseat Rally | 2026-10-05 | 52,417 | 18.70 | 12.10 | 12.40 |  |  | 0.18 | 3.95 | 7,918 | 0.15 |
| [🛸] Sweep The Moon 🌕 | 2026-10-23 | 51,886 | 16.20 | 10.20 | 14.30 |  |  | 0.62 | 1.12 | 16,871 | 0.33 |
| Bunker vs Verity | 2026-09-22 | 51,145 | 25.30 | 15.50 | 16.30 |  |  | 0.13 | 5.41 | 2,934 | 0.06 |
| Sandworm Playground | 2026-11-02 | 50,975 | 12.90 | 11.10 | 11.10 |  |  | 0.59 | 1.17 | 26,522 | 0.52 |
| [NOW!] Drive A Kukirin! | 2026-08-05 | 49,689 | 66.40 | 22.90 | 30.40 |  |  | 0.03 | 19.86 | 3,343 | 0.07 |

## C. Format waves (title keyword clusters)

| token | games | first | leader_now | leader_is_first | total_playing | created_last_120d |
|---|---|---|---|---|---|---|
| steal | 15 | [💀] Steal a Brainrot (2025-05-16) | Steal An Egg (2026-07-25) | 0 | 1,196,313 | 11 |
| egg | 6 | [🍂TURKEY] Break a Brainrot Egg! (2026-01-02) | Steal An Egg (2026-07-25) | 0 | 1,104,711 | 5 |
| simulator | 22 | Pilot Training Flight Simulator (2010-01-04) | 🍁 [TYCOON] Pet Simulator 99! 🍀 (2022-02-05) | 0 | 280,096 | 6 |
| anime | 20 | World // Zero ⚔️ Anime RPG  (2019-01-08) | [☀️UPD 21🏖️] Anime Adventures (2021-12-21) | 0 | 232,804 | 8 |
| forest | 3 | 99 Nights in the Forest 🔦 (2025-03-04) | 99 Nights in the Forest 🔦 (2025-03-04) | 1 | 167,433 | 1 |
| rivals | 3 | [🎯] RIVALS (2024-05-26) | [🎯] RIVALS (2024-05-26) | 1 | 164,958 | 0 |
| murder | 3 | Murder Mystery 2 (2014-01-18) | Murder Mystery 2 (2014-01-18) | 1 | 123,532 | 0 |
| tower defense | 11 | Tower Defense Simulator (2019-06-05) | [UPD🥳] Cameraman Tower Defense (2026-08-26) | 0 | 123,380 | 3 |
| fish | 6 | [🏝️UPD] Fish It! 🐟 (2024-10-21) | [🏝️UPD] Fish It! 🐟 (2024-10-21) | 1 | 116,450 | 3 |
| survive | 12 | 🔪Survive the Killer! (2020-01-06) | [🗺️MAPS] Survive Your Ideas (2026-10-06) | 0 | 110,708 | 4 |
| escape | 14 | Escape The Carnival of Terror Obby!  (2020-12-28) | [S8] +1 Speed Keyboard Escape | Candy & Chocolate (2026-01-18) | 0 | 78,640 | 3 |
| pet | 4 | 🍁 [TYCOON] Pet Simulator 99! 🍀 (2022-02-05) | 🍁 [TYCOON] Pet Simulator 99! 🍀 (2022-02-05) | 1 | 76,325 | 1 |
| tycoon | 12 | 🌳 Lumber Tycoon 2 (2009-07-30) | LINE UP! Metro Tycoon (2026-10-04) | 0 | 54,236 | 4 |
| rng | 5 | Sol's RNG [ Part 2 🎃 ] (2023-12-03) | Sol's RNG [ Part 2 🎃 ] (2023-12-03) | 1 | 51,320 | 2 |
| garden | 3 | [🏺] Grow a Garden 🌶️ (2025-03-25) | [🏺] Grow a Garden 🌶️ (2025-03-25) | 1 | 37,412 | 1 |
| obby | 4 | Escape The Carnival of Terror Obby!  (2020-12-28) | obby but you get smaller every stage (2025-05-19) | 0 | 15,477 | 0 |

## D. Holding players: games older than 6 months with >= 5k peak since June

- Correlation (Spearman) of 'now / peak since June' with name changes in last 90 days: -0.19 (n=305).
- Median now/peak: with >= 3 name changes in 90 days 0.23 (n=22); with 0-2: 0.32 (n=283).

## E. Monetization and social structure by size tier

| tier | games | median_passes | median_pass_price | median_max_pass | median_like_ratio | median_max_players | median_rw_rev_usd_per_ccu_day (RoWatcher est.) |
|---|---|---|---|---|---|---|---|
| <1k | 35 | 5.00 | 200 | 599 | 0.85 | 20.00 | 0.15 |
| 1k-10k | 437 | 6.00 | 199 | 599 | 0.90 | 16.00 | 0.48 |
| 10k-100k | 150 | 6.00 | 240 | 599 | 0.92 | 16.00 | 0.47 |
| 100k+ | 9 | 3.00 | 416 | 772 | 0.91 | 12.00 | 0.24 |

## F. The bar for Up-and-Coming today

- 97 games; median age 23 days (max 70); median live players 6,106 (min 549); median like ratio 0.88.

| name | created | age_days | playing_now | like_ratio | genre |
|---|---|---|---|---|---|
| [🗺️MAPS] Survive Your Ideas | 2026-10-06 | 40.00 | 53,643 | 0.89 | Survival |
| Ragdoll Soccer | 2026-10-13 | 33.00 | 36,567 | 0.73 | Sports & Racing |
| Bloody Ragdoll Physics 🩸 | 2026-10-31 | 15.00 | 33,919 | 0.87 | Simulation |
| Unstable SMP FFA [JAVA PVP!] | 2026-10-21 | 25.00 | 32,627 | 0.85 | Action |
| [KENDURI] MALAM SAMA OPAH  | 2026-10-20 | 26.00 | 32,281 | 0.84 | Survival |
| [🐜] Ant Evolution | 2026-10-28 | 18.00 | 28,715 | 0.92 | Survival |
| Realistic Ragdoll MMA 🥊 | 2026-11-05 | 10.00 | 28,137 | 0.79 | Action |
| Sandworm Playground | 2026-11-02 | 13.00 | 26,522 | 0.88 | Simulation |
| Voxel Wars | 2026-10-28 | 18.00 | 24,982 | 0.80 | Shooter |
| BloxNG [CRASH PHYSICS] 💥 | 2026-10-13 | 33.00 | 18,386 | 0.93 | Simulation |
| Volley Bomb | 2026-11-01 | 14.00 | 17,409 | 0.94 | Action |
| [🛸] Sweep The Moon 🌕 | 2026-10-23 | 23.00 | 16,871 | 0.98 | Simulation |
| Do Not Stop. | 2026-10-25 | 21.00 | 16,782 | 0.89 | Survival |
| Stop The Tsunami! | 2026-10-12 | 34.00 | 16,749 | 0.87 | All |
| Can You Pass A Driving Test? | 2026-10-18 | 28.00 | 15,547 | 0.86 | Simulation |
| Low Range: Offroad 4x4 [EARLY ACCESS] | 2026-10-09 | 37.00 | 15,398 | 0.93 | Simulation |
| ⚽ Be a Soccer Legend | 2026-10-12 | 34.00 | 15,203 | 0.96 | Sports & Racing |
| Throw a Seed | 2026-11-07 | 8.00 | 14,824 | 0.96 | Simulation |
| [⚡] Steal a Superpower! | 2026-10-10 | 36.00 | 13,334 | 0.99 | Simulation |
| [🏢] Ragdoll Research | 2026-10-28 | 18.00 | 13,220 | 0.83 | Simulation |
| 💣 Ragdoll Destruction Playground | 2026-11-03 | 12.00 | 13,068 | 0.83 | Simulation |
| [COBRA🐍] FERAL 🐺 Animal Survival | 2026-10-19 | 27.00 | 12,649 | 0.81 | Roleplay & Avatar Sim |
| 🤡 Class Clowns | 2026-10-27 | 19.00 | 12,031 | 0.77 | Survival |
| [PHYSICS] Ragdoll Playground | 2026-09-27 | 49.00 | 11,957 | 0.94 | Simulation |
| +1 Boxing Battle Evolution | 2026-10-17 | 29.00 | 11,876 | 0.89 | Simulation |

