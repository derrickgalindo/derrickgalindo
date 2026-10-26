"""Candidate legs, prices and market ladders for DAL @ PHI (snapshot ~6:20 PM ET, Oct 26 2026).

Book prices: DraftKings/ESPN pickcenter, ScoresAndOdds multi-book grid (bet365, BetMGM,
DraftKings, Caesars, FanDuel, Fanatics), SportsBettingDime closing table, TheLines,
BettingPros. Kalshi mids pulled from the public trade API. Pinnacle and Circa were not
reachable from this environment. Re-pull prices before betting; they move.

Each leg:
  col     sim column, side 'over'/'under', line (half points avoid pushes)
  books   {book: (price_this_side, price_other_side or None)}
  kalshi  fair P(this side) from the Kalshi ladder, or None
  mine    my probability when I have a data-driven adjustment (else None -> blend)
  source  why `mine` differs from the market
"""

LEGS = [
    # ---- sides / totals -------------------------------------------------
    dict(id="DAL-4.5", label="Cowboys -4.5", col="DAL_margin", side="over", line=4.5,
         books={"BetMGM": (-102, -108), "DraftKings": (-105, -115), "FanDuel": (-108, -112), "bet365": (-108, -112)},
         kalshi=0.485),
    dict(id="PHI+4.5", label="Eagles +4.5", col="DAL_margin", side="under", line=4.5,
         books={"BetMGM": (-108, -102), "DraftKings": (-115, -105), "FanDuel": (-112, -108), "bet365": (-112, -108)},
         kalshi=0.515),
    dict(id="O43.5", label="Over 43.5", col="total", side="over", line=43.5,
         books={"DraftKings": (-112, -108), "FanDuel": (-120, -102), "bet365": (-114, -106), "Caesars": (-113, -107), "Fanatics": (-115, -105)},
         kalshi=0.515),
    dict(id="U43.5", label="Under 43.5", col="total", side="under", line=43.5,
         books={"DraftKings": (-108, -112), "FanDuel": (-102, -120), "bet365": (-106, -114), "Caesars": (-107, -113), "Fanatics": (-105, -115)},
         kalshi=0.485),
    dict(id="DAL-ML", label="Cowboys ML", col="DAL_margin", side="over", line=0,
         books={"DraftKings": (-225, 185), "FanDuel": (-215, 180), "BetMGM": (-235, 190), "bet365": (-230, 185)},
         kalshi=0.675),
    dict(id="PHI-ML", label="Eagles ML", col="DAL_margin", side="under", line=0,
         books={"DraftKings": (185, -225), "FanDuel": (180, -215), "BetMGM": (190, -235), "bet365": (185, -230)},
         kalshi=0.335),

    # ---- Dallas ---------------------------------------------------------
    dict(id="Dak-U278.5py", label="Dak Prescott U278.5 pass yds", col="Dak Prescott|pass_yds", side="under", line=278.5,
         books={"bet365": (-115, -115), "Caesars": (-113, -113), "FanDuel": (-115, -115)},
         kalshi=0.565,  # 275+ 0.455, 300+ 0.315 -> P(<=278) ~0.565; Polymarket 275+ 0.47
         mine=0.545,
         source="weak: exchanges (Kalshi 0.565, Polymarket 0.55) and my raked sim (0.54) all sit under the books' "
                "278.5; DAL as 4.5-pt fav leads more often (run-heavier 2H); PHI pass D allows 6.7 YPA, near league avg"),
    dict(id="Dak-O1.5ptd", label="Dak Prescott O1.5 pass TD", col="Dak Prescott|pass_td", side="over", line=1.5,
         books={"DraftKings": (-132, 105), "bet365": (-140, 110), "FanDuel": (-135, 104)}, kalshi=0.555),
    dict(id="Dak-O36.5att", label="Dak Prescott O36.5 pass att", col="Dak Prescott|pass_att", side="over", line=36.5,
         books={"bet365": (-120, -110), "Caesars": (-115, -111), "FanDuel": (-111, -122)}, kalshi=None),
    dict(id="Lamb-O80.5ry", label="CeeDee Lamb O80.5 rec yds", col="CeeDee Lamb|rec_yds", side="over", line=80.5,
         books={"ESPN BET": (-115, -115), "FanDuel": (-110, -120)}, kalshi=0.49),
    dict(id="Lamb-ATD", label="CeeDee Lamb anytime TD", col="CeeDee Lamb|anytime_td", side="over", line=0.5,
         books={"bet365": (115, None), "BetMGM": (125, None), "DraftKings": (120, None), "Caesars": (125, None), "FanDuel": (125, None)},
         kalshi=0.415),
    dict(id="Pickens-O66.5ry", label="George Pickens O66.5 rec yds", col="George Pickens|rec_yds", side="over", line=66.5,
         books={"SBD best": (-115, -115)}, kalshi=0.48),
    dict(id="JW-ATD", label="Javonte Williams anytime TD", col="Javonte Williams|anytime_td", side="over", line=0.5,
         books={"bet365": (-180, None), "BetMGM": (-160, None), "DraftKings": (-160, None), "Caesars": (-162, None), "FanDuel": (-165, None)},
         kalshi=0.58,
         mine=0.61,
         source="15/15 DAL carries inside the 5 and 17/18 inside the 10; DAL 4.0 RZ trips/g at 75% TD; "
                "PHI rush D 27th in EPA; E[DAL rush TD] ~1.0 x 88% share -> Poisson 0.61-0.63"),
    dict(id="JW-O16.5att", label="Javonte Williams O16.5 rush att", col="Javonte Williams|rush_att", side="over", line=16.5,
         books={"bet365": (-115, -115), "DraftKings": (-110, -120), "FanDuel": (-112, -118)}, kalshi=0.515),
    dict(id="Flournoy-O33.5ry", label="Ryan Flournoy O33.5 rec yds", col="Ryan Flournoy|rec_yds", side="over", line=33.5,
         books={"DraftKings": (-111, -115)}, kalshi=0.52),

    # ---- Philadelphia ---------------------------------------------------
    dict(id="McKee-U0.5int", label="Tanner McKee U0.5 INT", col="Tanner McKee|int", side="under", line=0.5,
         books={"bet365": (120, -150), "BetMGM": (105, -140), "DraftKings": (112, -143), "Caesars": (-102, -128), "FanDuel": (-100, -130)},
         kalshi=0.43,  # Polymarket 1+ INT 0.57
         mine=0.49,
         source="DAL D: 1 INT on 189 att (0.5%) and 3.9% sack rate, both near league-worst -> little pressure-driven turnover; "
                "McKee 0 INT in ~100 career att, 8.0 aDOT. Shrunk hard: rate 2.0%/att x ~34 att -> P(0)=0.49"),
    dict(id="McKee-O199.5py", label="Tanner McKee O199.5 pass yds", col="Tanner McKee|pass_yds", side="over", line=199.5,
         books={"DraftKings": (104, -135)}, kalshi=0.505),
    dict(id="McKee-U205.5py", label="Tanner McKee U205.5 pass yds", col="Tanner McKee|pass_yds", side="under", line=205.5,
         books={"bet365": (-115, -115), "Caesars": (-113, -113), "FanDuel": (-115, -115)}, kalshi=0.53),
    dict(id="McKee-O33.5att", label="Tanner McKee O33.5 pass att", col="Tanner McKee|pass_att", side="over", line=33.5,
         books={"bet365": (-115, -115), "Caesars": (-113, -113), "FanDuel": (-111, -121)}, kalshi=0.485),
    dict(id="McKee-U1.5ptd", label="Tanner McKee U1.5 pass TD", col="Tanner McKee|pass_td", side="under", line=1.5,
         books={"bet365": (-210, 160), "DraftKings": (-209, 162), "FanDuel": (-205, 154)}, kalshi=0.635),
    dict(id="Goedert-O48.5ry", label="Dallas Goedert O48.5 rec yds", col="Dallas Goedert|rec_yds", side="over", line=48.5,
         books={"BetMGM": (104, -135), "DraftKings": (-115, -115)}, kalshi=0.505),
    dict(id="Goedert-ATD", label="Dallas Goedert anytime TD", col="Dallas Goedert|anytime_td", side="over", line=0.5,
         books={"bet365": (185, None), "BetMGM": (190, None), "DraftKings": (195, None), "Caesars": (180, None)},
         kalshi=0.325),
]

# Kalshi ladders (mid prices) used to rake the simulation: P(X > line)
MARGIN_LADDER = {  # DAL points minus PHI points
    -14.5: 0.935, -10.5: 0.905, -9.5: 0.885, -7.5: 0.865, -6.5: 0.825, -5.5: 0.805, -4.5: 0.795,
    -3.5: 0.775, -2.5: 0.705, -1.5: 0.695, 0: 0.675, 1.5: 0.635, 2.5: 0.615, 3.5: 0.535, 4.5: 0.49,
    5.5: 0.465, 6.5: 0.435, 7.5: 0.375, 9.5: 0.345, 10.5: 0.305, 13.5: 0.245, 14.5: 0.215,
    16.5: 0.185, 17.5: 0.165, 20.5: 0.125,
}
TOTAL_LADDER = {
    23.5: 0.955, 26.5: 0.925, 29.5: 0.885, 32.5: 0.825, 35.5: 0.765, 38.5: 0.675, 41.5: 0.575,
    42.5: 0.565, 43.5: 0.515, 44.5: 0.475, 45.5: 0.455, 46.5: 0.415, 47.5: 0.39, 50.5: 0.315,
    53.5: 0.235, 56.5: 0.185, 59.5: 0.135, 62.5: 0.095, 65.5: 0.065,
}
TARGET_MEANS = {"DAL": 24.6, "PHI": 19.6}  # from Kalshi team-total ladders (sum of survival)

# SGP quotes seen in the wild today (TheLines, Oct 26) -> used to estimate how books price correlation
SGP_QUOTES = [
    dict(book="DraftKings", price=285, legs=[("Dak Prescott|pass_yds", "over", 269.5, 0.485), ("Dak Prescott|pass_att", "over", 37.5, 0.435)]),
    dict(book="DraftKings", price=221, legs=[("CeeDee Lamb|rec_yds", "over", 80.5, 0.487), ("CeeDee Lamb|rec", "over", 6.5, 0.535)]),
    dict(book="FanDuel", price=594, legs=[("DAL_margin", "over", 4.5, 0.49), ("total", "under", 44.5, 0.525), ("DAL_margin_1h", "over", 3.5, 0.445)]),
]

FAV, DOG, SPREAD, TOTAL = "DAL", "PHI", 4.5, 43.5
POOL = [L["id"] for L in LEGS]
