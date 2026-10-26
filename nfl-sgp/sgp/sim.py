"""Play-by-play Monte Carlo of one NFL game.

Every simulated game shares one script: the score and clock drive play calling
(trailing teams pass more and hurry, leading teams run and bleed clock), so
player stats, team scores, margin and total are correlated the way they are on
the field. Each run returns one row per game with every team and player stat,
which is what the parlay pricer thresholds.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class Receiver:
    name: str
    tgt: float           # share of targets outside the red zone
    rz_tgt: float        # share of targets inside the 20
    catch: float         # catch rate per target (before team/defense adjustment)
    ypr: float           # yards per reception
    shape: float = 1.4   # gamma shape for yards per catch (lower = more boom/bust)


@dataclass
class Rusher:
    name: str
    carry: float         # share of designed runs outside the 10
    i10: float           # share of designed runs inside the 10
    ypc: float


@dataclass
class Team:
    name: str
    qb: str
    pass_rate: float                 # neutral-situation pass rate (dropbacks / plays)
    sec_per_play: float              # neutral pace, snap to snap
    comp_mult: float = 1.0           # multiplies receiver catch rates (QB accuracy x opp coverage)
    sack_rate: float = 0.06
    int_rate: float = 0.02
    scramble_rate: float = 0.03
    scramble_ypc: float = 6.0
    pass_yds_mult: float = 1.0       # calibration knob on yards per catch
    rush_yds_mult: float = 1.0       # calibration knob on yards per carry
    fg_mult: float = 1.0
    go_for_it: float = 1.0           # 4th-down aggressiveness multiplier
    receivers: list[Receiver] = field(default_factory=list)
    rushers: list[Rusher] = field(default_factory=list)


def _fg_prob(dist: int, mult: float) -> float:
    base = 0.99 if dist <= 30 else 0.95 if dist <= 40 else 0.85 if dist <= 50 else 0.70 if dist <= 55 else 0.45 if dist <= 60 else 0.0
    return min(0.995, base * mult)


class GameSim:
    def __init__(self, home: Team, away: Team, penalty_rate: float = 0.075, seed: int = 7,
                 form_sd: float = 0.12, pace_sd: float = 2.0, pass_shock_sd: float = 0.25):
        self.t = {"home": home, "away": away}
        self.penalty_rate = penalty_rate
        # Game-level shocks shared by every play of a simulated game: each offense's efficiency
        # that night, the game's pace, and each team's play-calling lean. They widen the score
        # distribution to NFL levels and are what makes a QB's and his receivers' stats move together.
        self.form_sd, self.pace_sd, self.pass_shock_sd = form_sd, pace_sd, pass_shock_sd
        self.rng = random.Random(seed)
        for tm in (home, away):
            tm._rec_w = [r.tgt for r in tm.receivers]
            tm._rz_w = [r.rz_tgt for r in tm.receivers]
            tm._run_w = [r.carry for r in tm.rushers]
            tm._i10_w = [r.i10 for r in tm.rushers]

    # ---- one game -------------------------------------------------------
    def play_game(self) -> dict:
        R = self.rng
        st = {"score": {"home": 0, "away": 0}}
        pace = R.gauss(0, self.pace_sd)
        st["form"] = {k: math.exp(R.gauss(0, self.form_sd)) for k in ("home", "away")}
        st["lean"] = {k: R.gauss(0, self.pass_shock_sd) for k in ("home", "away")}
        st["pace"] = pace
        stats: dict[str, float] = {}

        def add(k, v=1.0):
            stats[k] = stats.get(k, 0.0) + v

        receive_first = "home" if R.random() < 0.5 else "away"
        poss = receive_first
        for half in (1, 2):
            clock = 1800
            if half == 2:
                poss = "away" if receive_first == "home" else "home"
            yl = self._kick_start()
            while clock > 0:
                poss, yl, clock = self._drive(poss, yl, clock, half, st, add)
            if half == 1:
                stats["home_pts_1h"], stats["away_pts_1h"] = st["score"]["home"], st["score"]["away"]
        # overtime: 10 minutes, both teams get a possession, then sudden death
        if st["score"]["home"] == st["score"]["away"]:
            clock, poss, possessed = 600, ("home" if R.random() < 0.5 else "away"), set()
            yl = self._kick_start()
            while clock > 0:
                possessed.add(poss)
                poss, yl, clock = self._drive(poss, yl, clock, 3, st, add)
                if len(possessed) == 2 and st["score"]["home"] != st["score"]["away"]:
                    break
        stats["home_pts"] = st["score"]["home"]
        stats["away_pts"] = st["score"]["away"]
        return stats

    def _kick_start(self) -> int:
        # 2025+ kickoff rules: median start near own 30, touchback at the 35
        return int(min(80, max(50, 100 - self.rng.gauss(31, 6))))

    # ---- one possession -------------------------------------------------
    def _drive(self, poss, yl, clock, half, st, add):
        R = self.rng
        off, de = self.t[poss], self.t["away" if poss == "home" else "home"]
        other = "away" if poss == "home" else "home"
        down, dist = 1, min(10, yl)
        while True:
            if clock <= 0:
                return other, self._kick_start(), 0
            diff = st["score"][poss] - st["score"][other]
            game_left = clock + (1800 if half == 1 else 0)
            q4_late = half >= 2 and clock < 300
            hurry = (clock < 120 and diff <= 8) or (q4_late and diff < 0)
            # ---------------- 4th down ----------------
            if down == 4:
                fg_dist = yl + 17
                need_td = half >= 2 and clock < 240 and -8 <= diff < -3
                desperate = half >= 2 and clock < 240 and diff < 0
                go = False
                if desperate and (fg_dist > 55 or need_td or diff < -3):
                    go = True
                elif dist <= 1 and yl <= 60:
                    go = R.random() < min(0.95, 0.55 * off.go_for_it)
                elif dist <= 3 and 35 < yl <= 50:
                    go = R.random() < 0.35 * off.go_for_it
                elif dist <= 2 and yl <= 5:
                    go = R.random() < 0.55 * off.go_for_it
                if not go:
                    if fg_dist <= 57 and (fg_dist <= 52 or clock < 30 or half == 2):
                        clock -= 5
                        add(f"{off.name}|fga")
                        if R.random() < _fg_prob(fg_dist, off.fg_mult):
                            add(f"{off.name}|fg")
                            st["score"][poss] += 3
                            return other, self._kick_start(), clock
                        return other, min(80, max(20, 100 - (yl + 7))), clock
                    # punt
                    clock -= 8
                    land = yl - R.gauss(42, 7)
                    land = 20 if land < 0 else max(land, 6)
                    return other, int(100 - land), clock
            # ---------------- play call ----------------
            form = st["form"][poss]
            logit = math.log(off.pass_rate / (1 - off.pass_rate)) + st["lean"][poss]
            if down == 3 and dist >= 7:
                logit += 1.6
            elif down == 3 and dist <= 2:
                logit -= 0.9
            elif down == 2 and dist >= 8:
                logit += 0.4
            elif down == 1:
                logit -= 0.15
            if yl <= 3:
                logit -= 0.7
            tf = 1 + 2 * (1 - game_left / 3600) if half <= 2 else 2.0
            logit += -0.03 * diff * tf
            if hurry:
                logit += 1.8
            if half >= 2 and clock < 300 and diff > 0:
                logit -= 1.0
            is_pass = R.random() < 1 / (1 + math.exp(-logit))

            # ---------------- penalty ----------------
            if R.random() < self.penalty_rate:
                if R.random() < 0.5:   # offensive
                    yards = 10 if R.random() < 0.45 else 5
                    yl = min(99, yl + yards)
                    dist += yards
                else:
                    yards = 5 if R.random() < 0.5 else 12
                    yl = max(1, yl - yards)
                    if yards >= 10 or yards >= dist:
                        down, dist = 1, min(10, yl)
                    else:
                        dist -= yards
                clock -= 6
                continue

            gained, td, turnover, stop_clock = 0, False, False, False
            if is_pass:
                r = R.random()
                if r < off.sack_rate:
                    gained = -int(R.gauss(7, 2.5))
                    add(f"{off.qb}|sacks")
                    if R.random() < 0.08:  # strip sack
                        turnover = True
                elif r < off.sack_rate + off.scramble_rate:
                    gained = int(R.gammavariate(1.3, off.scramble_ypc / 1.3) - 0.5)
                    add(f"{off.qb}|rush_att")
                    if gained >= yl:
                        gained, td = yl, True
                        add(f"{off.qb}|rush_td")
                    add(f"{off.qb}|rush_yds", gained)
                else:
                    w = off._rz_w if yl <= 20 else off._rec_w
                    rec = R.choices(off.receivers, weights=w)[0]
                    add(f"{off.qb}|pass_att")
                    add(f"{rec.name}|targets")
                    if R.random() < min(0.92, rec.catch * off.comp_mult * form ** 0.5):
                        y = R.gammavariate(rec.shape, rec.ypr * off.pass_yds_mult * form / rec.shape)
                        gained = int(round(y))
                        if gained >= yl:
                            gained, td = yl, True
                            add(f"{rec.name}|rec_td")
                            add(f"{off.qb}|pass_td")
                        add(f"{rec.name}|rec")
                        add(f"{rec.name}|rec_yds", gained)
                        add(f"{off.qb}|comp")
                        add(f"{off.qb}|pass_yds", gained)
                        if not td and R.random() < 0.006:
                            turnover = True
                    else:
                        stop_clock = True
                        if R.random() < off.int_rate / max(1e-9, 1 - rec.catch * off.comp_mult):
                            turnover = True
                            add(f"{off.qb}|int")
                            gained = max(0, min(yl - 1, int(R.gauss(9, 6))))
            else:
                w = off._i10_w if yl <= 10 else off._run_w
                ru = R.choices(off.rushers, weights=w)[0]
                mean = ru.ypc * off.rush_yds_mult * form
                y = R.gammavariate(1.15, (mean + 2.2) / 1.15) - 2.2
                gained = int(round(y))
                if yl <= 2 and gained < yl:   # goal-line pile: sneaks/dives convert often
                    gained = yl if R.random() < 0.45 else gained
                add(f"{ru.name}|rush_att")
                if gained >= yl:
                    gained, td = yl, True
                    add(f"{ru.name}|rush_td")
                add(f"{ru.name}|rush_yds", gained)
                if not td and R.random() < 0.007:
                    turnover = True

            # clock
            if stop_clock:
                clock -= 6
            elif hurry:
                clock -= 16
            elif half >= 2 and clock < 360 and diff > 0:
                clock -= 39
            else:
                # sec_per_play is the neutral snap-to-snap average including incompletions,
                # so plays that keep the clock running take ~4s longer than it
                clock -= int(R.gauss(off.sec_per_play + 4 + st["pace"], 4))

            if td:
                add(f"{off.name}|td")
                st["score"][poss] += 7 if R.random() < 0.95 else 6
                return other, self._kick_start(), clock - 6
            if turnover:
                if is_pass and R.random() < 0.06:  # pick six / scoop and score
                    st["score"][other] += 7
                    return poss, self._kick_start(), clock
                new = 100 - max(1, yl - gained)
                return other, int(min(99, max(1, new))), clock
            yl -= gained
            if yl >= 100:   # safety
                st["score"][other] += 2
                return other, 60, clock
            if gained >= dist:
                down, dist = 1, min(10, yl)
            else:
                down += 1
                dist -= gained
                if down > 4:
                    return other, int(min(99, max(1, 100 - yl))), clock

    # ---- many games ------------------------------------------------------
    def run(self, n: int) -> pd.DataFrame:
        rows = [self.play_game() for _ in range(n)]
        df = pd.DataFrame(rows).fillna(0.0)
        h, a = self.t["home"].name, self.t["away"].name
        df[f"{h}_pts"], df[f"{a}_pts"] = df.pop("home_pts"), df.pop("away_pts")
        df["total"] = df[f"{h}_pts"] + df[f"{a}_pts"]
        df[f"{a}_margin"] = df[f"{a}_pts"] - df[f"{h}_pts"]
        df[f"{h}_margin"] = -df[f"{a}_margin"]
        h1, a1 = df.pop("home_pts_1h"), df.pop("away_pts_1h")
        df["total_1h"] = h1 + a1
        df[f"{a}_margin_1h"] = a1 - h1
        df[f"{h}_margin_1h"] = -df[f"{a}_margin_1h"]
        for tm in (self.t["home"], self.t["away"]):
            for p in {r.name for r in tm.rushers} | {r.name for r in tm.receivers} | {tm.qb}:
                rt = df.get(f"{p}|rush_td", 0) + df.get(f"{p}|rec_td", 0)
                df[f"{p}|anytime_td"] = rt
        return df


def summarize_calibration(df: pd.DataFrame, fav: str, dog: str) -> dict:
    m = df[f"{fav}_margin"] if f"{fav}_margin" in df else -df[f"{dog}_margin"]
    return {
        "median_margin": float(np.median(m)), "mean_margin": float(m.mean()), "sd_margin": float(m.std()),
        "p_fav_win": float((m > 0).mean() + 0.5 * (m == 0).mean()),
        "median_total": float(df.total.median()), "mean_total": float(df.total.mean()), "sd_total": float(df.total.std()),
        f"mean_{fav}": float(df[f"{fav}_pts"].mean()), f"mean_{dog}": float(df[f"{dog}_pts"].mean()),
    }
