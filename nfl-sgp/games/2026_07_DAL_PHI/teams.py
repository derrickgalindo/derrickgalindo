"""Inputs for DAL @ PHI, 2026 Week 7 (MNF, Oct 26 2026).

Every number traces to nflverse 2026 weeks 1-6 (see analysis.md) with
shrinkage toward position priors; the comments name the source.
`pass_yds_mult` / `rush_yds_mult` start at 1.0 and are fitted by calibrate()
so the simulated score distribution matches the market.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from sgp.sim import Receiver, Rusher, Team  # noqa: E402

# Set from the 6:45 PM ET inactives list.
BARKLEY_ACTIVE = os.environ.get("BARKLEY_ACTIVE", "1") == "1"


def dallas() -> Team:
    # Targets (wk1-6): Lamb 29.2% / 31.6% RZ / 8 end-zone tgts; Pickens 21.4%; Flournoy 15.2% (21% RZ);
    # Ferguson 9.9%; J.Williams 9.1%; Spann-Ford 4.5%; Turpin 2.9% (OUT -> spread to Mingo/Flournoy).
    rec = [
        Receiver("CeeDee Lamb", 0.285, 0.31, 0.675, 12.0, 1.4),
        Receiver("George Pickens", 0.215, 0.17, 0.635, 12.9, 1.3),
        Receiver("Ryan Flournoy", 0.155, 0.19, 0.625, 10.6, 1.5),
        Receiver("Jake Ferguson", 0.10, 0.10, 0.72, 7.6, 1.8),
        Receiver("Javonte Williams", 0.085, 0.08, 0.82, 6.0, 1.6),
        Receiver("Brevyn Spann-Ford", 0.05, 0.05, 0.66, 9.6, 1.6),
        Receiver("Jonathan Mingo", 0.04, 0.03, 0.55, 11.0, 1.3),
        Receiver("Tyler Goodson", 0.025, 0.02, 0.75, 5.5, 1.6),
        Receiver("Hunter Luepke", 0.02, 0.03, 0.85, 4.5, 2.0),
        Receiver("Luke Schoonmaker", 0.015, 0.02, 0.75, 9.0, 1.6),
    ]
    # Carries (non-scramble): J.Williams 77% overall, 94% inside the 10, 15/15 inside the 5.
    run = [
        Rusher("Javonte Williams", 0.77, 0.86, 3.85),
        Rusher("Tyler Goodson", 0.11, 0.04, 3.6),
        Rusher("Emari Demercado", 0.05, 0.01, 3.9),
        Rusher("Hunter Luepke", 0.03, 0.04, 3.5),
        Rusher("Dak Prescott", 0.02, 0.05, 3.0),   # designed QB runs / sneaks
        Rusher("CeeDee Lamb", 0.02, 0.0, 5.0),
    ]
    # Neutral pass rate 60% season (PROE +3.0, 6th), 71% last two weeks; PHI pass D 25th, run D 27th.
    # Pace 30.6 s/play neutral (2nd fastest). Sack rate allowed 2.6% vs PHI D 3.3% (Nolan Smith OUT).
    return Team(
        name="DAL", qb="Dak Prescott", pass_rate=0.62, sec_per_play=31.0,
        comp_mult=1.0, sack_rate=0.035, int_rate=0.018, scramble_rate=0.02, scramble_ypc=6.5,
        receivers=rec, rushers=run, go_for_it=1.1,
    )


def philly() -> Team:
    # D.Smith (31.8% wk6 share, 48% of air yards) and Wicks OUT -> ~39% of targets to redistribute.
    # Goedert 18% wk6 with both on the field; Lemon 13.6%/70-81% snaps; Cooper 61% snaps, 17.4 YPR deep role.
    rec = [
        Receiver("Dallas Goedert", 0.235, 0.27, 0.71, 10.3, 1.6),
        Receiver("Makai Lemon", 0.195, 0.14, 0.67, 9.4, 1.5),
        Receiver("Darius Cooper", 0.16, 0.20, 0.58, 13.5, 1.2),
        Receiver("Hollywood Brown", 0.085, 0.07, 0.60, 11.5, 1.3),
        Receiver("Elijah Moore", 0.06, 0.05, 0.64, 10.0, 1.5),
        Receiver("Zach Ertz", 0.035, 0.07, 0.65, 8.0, 1.8),   # 8 tgts wk1-5
        Receiver("Johnny Mundt", 0.025, 0.04, 0.74, 7.5, 1.8),
        Receiver("Grant Calcaterra", 0.02, 0.03, 0.70, 9.0, 1.6),
    ]
    # RB room: Shipley/Bigsby on IR, Carson Steele not on the active roster; Elijah Mitchell is RB3.
    if BARKLEY_ACTIVE:
        rec += [Receiver("Saquon Barkley", 0.07, 0.06, 0.74, 6.5, 1.4),
                Receiver("Dameon Pierce", 0.04, 0.03, 0.75, 5.0, 1.6)]
        # Barkley 5.1 YPC this year but left 2 of 4 games early with the hamstring and returns behind a
        # patched OL (L.Johnson retired); shrink to 4.3. Books hang 15.5-16.5 carries.
        run = [Rusher("Saquon Barkley", 0.65, 0.60, 4.3),
               Rusher("Dameon Pierce", 0.25, 0.25, 3.3),
               Rusher("Tanner McKee", 0.03, 0.10, 2.0),
               Rusher("Makai Lemon", 0.02, 0.0, 5.0),
               Rusher("Elijah Mitchell", 0.05, 0.05, 3.8)]
    else:
        rec += [Receiver("Dameon Pierce", 0.08, 0.06, 0.75, 5.0, 1.6),
                Receiver("Elijah Mitchell", 0.03, 0.03, 0.75, 5.0, 1.6)]
        run = [Rusher("Dameon Pierce", 0.62, 0.60, 3.3),
               Rusher("Elijah Mitchell", 0.28, 0.25, 3.8),
               Rusher("Tanner McKee", 0.04, 0.12, 2.0),
               Rusher("Makai Lemon", 0.03, 0.0, 5.0),
               Rusher("Hollywood Brown", 0.03, 0.03, 5.0)]
    # McKee wk6: 26/48, 215 yds, 6.3% sacks, 73% neutral pass rate (PROE +10.3).
    # PHI OL sack rate 7.0% vs DAL D 3.9%; DAL D allows 65.6% comp, 7.59 YPA, 0.5% INT (all 32nd/near).
    return Team(
        name="PHI", qb="Tanner McKee", pass_rate=0.52, sec_per_play=32.5,
        comp_mult=0.95, sack_rate=0.055, int_rate=0.020, scramble_rate=0.025, scramble_ypc=5.0,
        receivers=rec, rushers=run, go_for_it=1.0,
    )


HOME, AWAY = philly, dallas
