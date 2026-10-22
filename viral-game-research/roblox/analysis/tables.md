# Roblox deep dive: tables (n=625 games, snapshot 2026-10-22)

## A. Who is on top

- Top 100 by live players: median age 1.5 years; created in the last 120 days: 37; last 365 days: 47; older than 3 years: 30.
- Games at or above ~1M-DAU scale now (>= 75,000 concurrent): 10.

| name | playing_now | created | genre | max_players | like_ratio | n_passes | name_changes_90d |
|---|---|---|---|---|---|---|---|
| Steal An Egg | 761,288 | 2026-07-25 | Simulation | 7.00 | 0.92 | 2 | 2 |
| Murder Mystery 2 | 625,476 | 2014-01-18 | Survival | 12.00 | 0.91 | 3 | 0 |
| Brookhaven 🏡RP | 264,940 | 2020-04-21 | Roleplay & Avatar Sim | 30.00 | 0.86 | 18 | 0 |
| [🎃] Adopt Me! | 121,086 | 2017-07-14 | Roleplay & Avatar Sim | 35.00 | 0.86 | 6 | 49 |
| [🎃] RIVALS | 116,272 | 2024-05-26 | Shooter | 40.00 | 0.94 | 8 | 0 |
| [SKY ASSASSIN] Jujutsu Shenanigans | 109,689 | 2022-04-17 | Action | 20.00 | 0.86 | 5 | 0 |
| Blox Fruits | 109,091 | 2019-01-16 | RPG | 12.00 | 0.92 | 6 | 1 |
| [💀] Steal a Brainrot | 107,095 | 2025-05-16 | Simulation | 8.00 | 0.85 | 3 | 2 |
| 99 Nights in the Forest 🔦 | 103,512 | 2025-03-04 | Survival | 25.00 | 0.90 | 1 | 1 |
| Break and Steal an Egg | 78,413 | 2026-09-05 | Simulation | 7.00 | 0.98 | 0 | 0 |
| 🎃 Dandy's World [ALPHA] | 71,842 | 2024-01-26 | Survival | 35.00 | 0.88 | 7 | 0 |
| [🎃DUELS] Murderers VS Sheriffs | 70,974 | 2025-02-09 | Action | 30.00 | 0.87 | 5 | 1 |
| [🎃UPD] Fish It! 🐟 | 70,681 | 2024-10-21 | Simulation | 20.00 | 0.83 | 12 | 21 |
| [🎃] Anime Dice | 67,068 | 2026-08-15 | Simulation | 9.00 | 0.99 | 8 | 1 |
| [🎃] Dress To Impress | 62,359 | 2023-10-18 | Roleplay & Avatar Sim | 13.00 | 0.91 | 14 | 0 |
| Catalog Avatar Creator | 58,911 | 2021-07-03 | Shopping | 24.00 | 0.94 | 0 | 0 |
| Fisch 🎃 [FISCHFRIGHT] | 56,841 | 2024-03-13 | Simulation | 20.00 | 0.91 | 9 | 4 |
| [🎃HLWN] Evade  | 45,659 | 2022-06-10 | Survival | 15.00 | 0.94 | 26 | 1 |
| [🎃] Huss Valley | 44,929 | 2026-08-31 | Action | 30.00 | 0.88 | 4 | 0 |
| [UPD] Volleyball Legends | 44,793 | 2024-12-17 | Sports & Racing | 12.00 | 0.95 | 3 | 0 |
| [UPD 🤖] Forsaken | 44,195 | 2024-07-28 | Survival | 9.00 | 0.84 | 4 | 5 |
| Cat Battles 🐾 | 42,207 | 2026-10-05 | Action | 10.00 | 0.73 | 2 | 0 |
| [UPDATE!] Illegal Soccer | 41,771 | 2026-05-12 | Sports & Racing | 8.00 | 0.86 | 2 | 1 |
| The Strongest Battlegrounds | 40,458 | 2022-08-02 | Action | 15.00 | 0.84 | 7 | 0 |
| Vanguards: 2nd Anniversary | 34,847 | 2024-01-28 | Strategy | 24.00 | 0.97 | 5 | 0 |
| 💎 [DIAMOND] Pet Simulator 99! 💎 | 34,204 | 2022-02-05 | Simulation | 10.00 | 0.95 | 13 | 6 |
| [CURE] Violence District | 32,432 | 2024-10-31 | Survival | 6.00 | 0.93 | 2 | 0 |
| [🎃] Tap Simulator REBORN | 31,977 | 2026-08-04 | Simulation | 10.00 | 0.95 | 10 | 3 |
| Sol's RNG [ Radiant Forest🌙] | 30,899 | 2023-12-03 | Simulation | 20.00 | 0.91 | 7 | 1 |
| Berry Avenue 🏠 RP | 29,572 | 2022-01-07 | Roleplay & Avatar Sim | 31.00 | 0.86 | 9 | 0 |

Genre mix of the top 100:

| genre | games | playing |
|---|---|---|
| Simulation | 32 | 1,632,484 |
| Survival | 18 | 1,124,916 |
| Roleplay & Avatar Sim | 10 | 568,568 |
| Action | 12 | 401,912 |
| Shooter | 5 | 173,877 |
| Sports & Racing | 6 | 161,227 |
| RPG | 4 | 151,393 |
| Strategy | 4 | 78,644 |
| Shopping | 2 | 77,357 |
| Party & Casual | 3 | 47,168 |
| All | 2 | 33,812 |
| Obby & Platformer | 1 | 22,554 |
| Adventure | 1 | 15,520 |

## B. Launch trajectories (games created since late June 2026, full history observed)

| name | created | peak_ccu | days_to_peak | days_to_1k | days_to_10k | days_to_100k | days_to_1M | growth_per_day_1k_to_peak | doubling_days | now | now_over_peak |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Steal An Egg | 2026-07-25 | 7,149,306 | 56.30 | 11.70 | 12.00 | 19.10 | 28.20 | 0.11 | 6.49 | 761,288 | 0.11 |
| Break and Steal an Egg | 2026-09-05 | 536,611 | 42.60 | 22.50 | 22.50 | 28.70 |  | 0.14 | 5.08 | 78,413 | 0.15 |
| [🍲] Karinderya! | 2026-08-07 | 150,093 | 42.90 | 16.60 | 16.80 | 42.90 |  | 0.06 | 11.86 | 4,235 | 0.03 |
| 🍂🎃 Clean all the Leaves | 2026-07-21 | 136,319 | 39.40 | 23.00 | 23.30 | 26.50 |  | 0.07 | 9.58 | 2,788 | 0.02 |
| [🎃] Huss Valley | 2026-08-31 | 136,041 | 41.00 | 29.60 | 30.90 | 33.90 |  | 0.20 | 3.49 | 44,929 | 0.33 |
| 🎃 Sell Fries! [Anomaly] 🍟 | 2026-09-21 | 104,668 | 26.10 | 13.90 | 18.00 | 26.10 |  | 0.32 | 2.18 | 24,168 | 0.23 |
| [🎃]+1 Loot To Forge | 2026-08-12 | 95,161 | 46.40 | 35.30 | 35.30 |  |  | 0.16 | 4.30 | 11,120 | 0.12 |
| Climb For Animals Eggs🥚 | 2026-09-06 | 95,070 | 40.50 | 30.30 | 30.30 |  |  | 0.19 | 3.65 | 27,925 | 0.29 |
| [🎃] +1 Stone Skipping | 2026-09-05 | 88,512 | 34.80 | 21.00 | 22.90 |  |  | 0.17 | 4.18 | 11,929 | 0.13 |
| Sarab | 2026-09-24 | 86,688 | 15.20 | 9.00 | 9.00 |  |  | 0.11 | 6.28 | 3,336 | 0.04 |
| [⚗️🌻] Search For The Needle | 2026-08-23 | 82,068 | 21.20 | 9.80 | 11.00 |  |  | 0.15 | 4.53 | 4,527 | 0.06 |
| Build and Kill Zombies | 2026-08-19 | 80,704 | 37.80 | 21.30 | 23.80 |  |  | 0.18 | 3.81 | 4,513 | 0.06 |
| [🎃] Anime Dice | 2026-08-15 | 79,742 | 65.50 | 17.30 | 22.30 |  |  | 0.05 | 13.51 | 67,068 | 0.84 |
| [CH2] 🪵 Chop A Forest | 2026-09-21 | 68,451 | 26.00 | 15.90 | 22.10 |  |  | 0.46 | 1.50 | 17,643 | 0.26 |
| [🎃] Ball VS Ball | 2026-08-12 | 62,176 | 60.40 | 21.10 | 23.30 |  |  | 0.05 | 13.32 | 21,109 | 0.34 |
| صيد الضبّان | 2026-10-03 | 61,799 | 17.90 | 7.50 | 7.80 |  |  | 0.12 | 5.75 | 13,757 | 0.22 |
| Steal Animal Egg | 2026-09-11 | 57,427 | 28.50 | 21.00 | 21.00 |  |  | 0.08 | 8.86 | 3,296 | 0.06 |
| [🎃] +1 Cut Grass Adventure | 2026-06-28 | 57,257 | 54.10 | 38.60 | 40.70 |  |  | 0.11 | 6.03 | 2,180 | 0.04 |
| Anime Zero [SOLAR RADIANCE ☀️] | 2026-07-16 | 57,057 | 87.00 | 78.30 | 80.80 |  |  | 0.27 | 2.54 | 9,080 | 0.16 |
| Cat Battles 🐾 | 2026-10-05 | 56,775 | 12.80 | 3.10 | 11.20 |  |  | 0.34 | 2.03 | 42,207 | 0.74 |
| Scream And Run [VERITY] | 2026-08-25 | 55,427 | 18.80 | 5.70 | 9.90 |  |  | 0.21 | 3.32 | 2,368 | 0.04 |
| [☁️WORLD 2] +1 Tongue Escape😛 | 2026-08-11 | 55,358 | 32.90 | 23.30 | 25.70 |  |  | 0.32 | 2.17 | 4,242 | 0.08 |
| [🎃] Kukirin Life [Testing] | 2026-09-19 | 54,098 | 28.90 | 17.30 | 18.80 |  |  | 0.20 | 3.49 | 10,920 | 0.20 |
| Facecard: Makeup Showdown [⭐UPD] | 2026-10-05 | 53,662 | 12.90 | 4.20 | 6.80 |  |  | 0.30 | 2.35 | 10,896 | 0.20 |
| Bunker vs Verity | 2026-09-22 | 51,145 | 25.30 | 15.50 | 16.30 |  |  | 0.13 | 5.41 | 10,733 | 0.21 |
| TROLL Hug Tower | 2026-07-07 | 48,035 | 40.50 | 25.00 | 25.00 |  |  | 0.08 | 8.31 | 10,167 | 0.21 |
| [NOW] Paint to Get Rich 🎨 | 2026-08-20 | 42,364 | 44.10 | 43.40 | 43.40 |  |  |  |  | 6,705 | 0.16 |
| 🦸 +1 Superhero Evolution | 2026-07-27 | 42,220 | 41.40 | 15.30 | 26.20 |  |  | 0.13 | 5.18 | 2,168 | 0.05 |
| [🎃] Tap Simulator REBORN | 2026-08-04 | 41,748 | 75.00 | 67.40 | 70.80 |  |  | 0.29 | 2.37 | 31,977 | 0.77 |
| [🎃UPD] Cameraman Tower Defense | 2026-08-26 | 39,268 | 54.80 | 34.90 | 43.90 |  |  | 0.14 | 4.79 | 20,359 | 0.52 |
| 7 Days Cat-Sitting | 2026-09-15 | 38,692 | 33.60 | 13.50 | 14.90 |  |  | 0.04 | 16.44 | 18,076 | 0.47 |
| Guess the character color | 2026-06-26 | 36,739 | 31.00 | 25.80 | 26.80 |  |  | 0.23 | 3.07 | 2,534 | 0.07 |
| [☄️] Ride a Dino | 2026-08-24 | 36,515 | 58.10 | 51.60 | 53.60 |  |  | 0.34 | 2.02 | 26,435 | 0.72 |
| Backseat Rally | 2026-10-05 | 35,612 | 15.70 | 12.10 | 12.40 |  |  | 0.24 | 2.85 | 19,420 | 0.55 |
| [MAFUBA] Anime Astral Simulator | 2026-07-14 | 35,516 | 1.90 | 1.90 | 1.90 |  |  |  |  | 9,528 | 0.27 |
| [🎃] Bike For Egg! | 2026-09-15 | 34,951 | 31.60 | 31.10 | 31.10 |  |  |  |  | 15,719 | 0.45 |
| Firefighting Sim 🚒 | 2026-09-22 | 33,486 | 18.70 | 13.00 | 13.50 |  |  | 0.17 | 4.05 | 6,118 | 0.18 |
| [🎃] Peel THE Potato | 2026-09-21 | 31,220 | 17.00 | 12.30 | 12.60 |  |  | 0.22 | 3.13 | 5,897 | 0.19 |
| Anime Ability Arena | 2026-06-26 | 31,119 | 78.90 | 25.80 | 49.80 |  |  | 0.05 | 15.24 | 7,814 | 0.25 |
| [🎃] Bike Universe | 2026-09-27 | 30,971 | 24.10 | 19.60 | 21.00 |  |  | 0.41 | 1.70 | 24,559 | 0.79 |

## C. Format waves (title keyword clusters)

| token | games | first | leader_now | leader_is_first | total_playing | created_last_120d |
|---|---|---|---|---|---|---|
| steal | 14 | [💀] Steal a Brainrot (2025-05-16) | Steal An Egg (2026-07-25) | 0 | 1,002,396 | 11 |
| egg | 9 | [🧟EVENT] Break a Brainrot Egg! (2026-01-02) | Steal An Egg (2026-07-25) | 0 | 893,010 | 8 |
| murder | 3 | Murder Mystery 2 (2014-01-18) | Murder Mystery 2 (2014-01-18) | 1 | 638,657 | 0 |
| anime | 20 | [🎃] Anime Dimensions Simulator (2021-06-11) | [🎃] Anime Dice (2026-08-15) | 0 | 180,906 | 10 |
| simulator | 23 | Pilot Training Flight Simulator (2010-01-04) | 💎 [DIAMOND] Pet Simulator 99! 💎 (2022-02-05) | 0 | 176,831 | 5 |
| rivals | 3 | [🎃] RIVALS (2024-05-26) | [🎃] RIVALS (2024-05-26) | 1 | 133,628 | 0 |
| forest | 3 | 99 Nights in the Forest 🔦 (2025-03-04) | 99 Nights in the Forest 🔦 (2025-03-04) | 1 | 124,701 | 1 |
| fish | 4 | [🎃UPD] Fish It! 🐟 (2024-10-21) | [🎃UPD] Fish It! 🐟 (2024-10-21) | 1 | 81,618 | 1 |
| pet | 3 | 💎 [DIAMOND] Pet Simulator 99! 💎 (2022-02-05) | 💎 [DIAMOND] Pet Simulator 99! 💎 (2022-02-05) | 1 | 62,824 | 0 |
| escape | 11 | Escape Running Head (2021-01-07) | +1 Speed Keyboard Escape | Candy & Chocolate (2026-01-18) | 0 | 54,742 | 1 |
| survive | 9 | 🔪Survive the Killer! (2020-01-06) | 🎃 Creatures of Sonaria 🍬 Survive Kaiju Animals (2020-06-25) | 0 | 47,610 | 3 |
| rng | 7 | Sol's RNG [ Radiant Forest🌙] (2023-12-03) | Sol's RNG [ Radiant Forest🌙] (2023-12-03) | 1 | 46,983 | 2 |
| tower defense | 7 | [🌙 NIGHT 2] Tower Defense Simulator (2019-06-05) | [🎃UPD] Cameraman Tower Defense (2026-08-26) | 0 | 46,943 | 2 |
| tycoon | 10 | 🌳 Lumber Tycoon 2 (2009-07-30) | Pet Store Tycoon (2026-06-06) | 0 | 39,602 | 2 |
| grow | 3 | [🎃] Grow a Garden 🌶️ (2025-03-25) | [🎃] Grow a Garden 🌶️ (2025-03-25) | 1 | 24,064 | 1 |
| obby | 4 | [W41] Obby But You're on a Scooter (2025-08-10) | [HELL] Spiral Difficulty Chart Obby (2026-01-20) | 0 | 10,962 | 2 |

## D. Holding players: games older than 6 months with >= 5k peak since June

- Correlation (Spearman) of 'now / peak since June' with name changes in last 90 days: -0.24 (n=306).
- Median now/peak: with >= 3 name changes in 90 days 0.20 (n=34); with 0-2: 0.27 (n=272).

## E. Monetization and social structure by size tier

| tier | games | median_passes | median_pass_price | median_max_pass | median_like_ratio | median_max_players | median_rw_rev_usd_per_ccu_day (RoWatcher est.) |
|---|---|---|---|---|---|---|---|
| <1k | 47 | 4.00 | 249 | 699 | 0.85 | 16.00 | 0.27 |
| 1k-10k | 457 | 6.00 | 249 | 599 | 0.90 | 16.00 | 0.52 |
| 10k-100k | 96 | 5.00 | 244 | 500 | 0.92 | 16.00 | 0.49 |
| 100k+ | 9 | 5.00 | 388 | 795 | 0.90 | 20.00 | 0.33 |

## F. The bar for Up-and-Coming today

- 94 games; median age 22 days (max 135); median live players 3,645 (min 168); median like ratio 0.89.

| name | created | age_days | playing_now | like_ratio | genre |
|---|---|---|---|---|---|
| Cat Battles 🐾 | 2026-10-05 | 16.00 | 42,207 | 0.73 | Action |
| [🎃] Tap Simulator REBORN | 2026-08-04 | 78.00 | 31,977 | 0.95 | Simulation |
| [🎃] Bike Universe | 2026-09-27 | 24.00 | 24,559 | 0.84 | Simulation |
| 🎃 Sell Fries! [Anomaly] 🍟 | 2026-09-21 | 30.00 | 24,168 | 0.83 | Survival |
| [HALLOWEEN 🎃] DONT SPLASH  | 2026-10-17 | 4.00 | 22,554 | 0.92 | Obby & Platformer |
| Backseat Rally | 2026-10-05 | 16.00 | 19,420 | 0.93 | All |
| [CH2] 🪵 Chop A Forest | 2026-09-21 | 30.00 | 17,643 | 0.93 | Simulation |
| Save the Krusty Krab 🍔 | 2026-09-29 | 22.00 | 17,196 | 0.94 | Survival |
| [🎃] Bike For Egg! | 2026-09-15 | 36.00 | 15,719 | 0.95 | Simulation |
| Steel Fighters | 2026-09-07 | 44.00 | 14,795 | 0.91 | Simulation |
| صيد الضبّان | 2026-10-03 | 18.00 | 13,757 | 0.95 | Simulation |
| Clone Baby Care (Anomaly) | 2026-10-09 | 12.00 | 13,594 | 0.88 | Survival |
| Fake an Egg | 2026-10-04 | 17.00 | 13,332 | 0.89 | Simulation |
| [🌍WORLD 2] +1 Venom Evolution | 2026-10-05 | 16.00 | 12,170 | 0.97 | Simulation |
| Tribes 3v3 | 2026-09-28 | 23.00 | 12,038 | 0.63 | Shooter |
| DIVINE HATCHERS 0.0001% [NEW!] | 2026-10-01 | 20.00 | 12,008 | 0.91 | Simulation |
| [🎃] Kukirin Life [Testing] | 2026-09-19 | 32.00 | 10,920 | 0.83 | Simulation |
| RoFront [World PvP] | 2026-09-26 | 25.00 | 10,784 | 0.82 | Strategy |
| Bunker vs Verity | 2026-09-22 | 29.00 | 10,733 | 0.82 | Survival |
| Free Fire Zone (Max) | 2026-09-27 | 24.00 | 10,375 | 0.85 | Action |
| +1 Assassin Leveling | 2026-09-24 | 27.00 | 9,930 | 0.96 | Simulation |
| Fix My Phone! | 2026-10-05 | 16.00 | 9,128 | 0.90 | Simulation |
| Eat Everything In A Grocery Store | 2026-10-03 | 18.00 | 8,950 | 0.88 | Simulation |
| Crazy Diver | 2026-09-24 | 27.00 | 8,847 | 0.54 | Simulation |
| Pixel Lineage [🎃Spear Class + Dragon Race] | 2026-09-25 | 26.00 | 7,545 | 0.99 | RPG |

