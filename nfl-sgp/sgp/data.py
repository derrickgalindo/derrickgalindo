"""Pull nflverse data and derive the team and player inputs the simulator needs."""
from __future__ import annotations

import numpy as np
import pandas as pd

try:
    import nflreadpy as nfl  # successor to nfl_data_py (which no longer installs on Python 3.12+)
except ImportError:  # pragma: no cover
    nfl = None


def load(season: int, cache_dir: str | None = None) -> dict[str, pd.DataFrame]:
    """Load the season's pbp, weekly player stats, snap counts, injuries, schedules, officials."""
    loaders = {
        "pbp": lambda: nfl.load_pbp([season]),
        "player_stats": lambda: nfl.load_player_stats([season]),
        "snaps": lambda: nfl.load_snap_counts([season]),
        "injuries": lambda: nfl.load_injuries([season]),
        "schedules": lambda: nfl.load_schedules([season]),
        "officials": lambda: nfl.load_officials(list(range(season - 3, season + 1))),
        "rosters": lambda: nfl.load_rosters_weekly([season]),
    }
    out = {}
    for name, fn in loaders.items():
        path = f"{cache_dir}/{name}_{season}.parquet" if cache_dir else None
        try:
            out[name] = pd.read_parquet(path) if path else fn().to_pandas()
        except (FileNotFoundError, OSError):
            df = fn().to_pandas()
            df.to_parquet(path)
            out[name] = df
    return out


def _plays(pbp: pd.DataFrame) -> pd.DataFrame:
    q = pbp[(pbp.season_type == "REG") & pbp.play_type.isin(["pass", "run"]) & pbp.epa.notna()].copy()
    q["neutral"] = q.wp.between(0.2, 0.8) & (q.qtr <= 3)
    return q


def team_profile(pbp: pd.DataFrame, team: str, weeks: list[int] | None = None) -> dict:
    """Offense and defense efficiency, pace, PROE and red-zone conversion for one team."""
    q = _plays(pbp)
    if weeks is not None:
        q = q[q.week.isin(weeks)]
    off, de = q[q.posteam == team], q[q.defteam == team]

    def eff(d):
        return {
            "plays": len(d),
            "epa": d.epa.mean(),
            "success": d.success.mean(),
            "pass_epa": d[d.pass_attempt == 1].epa.mean(),
            "rush_epa": d[d.rush_attempt == 1].epa.mean(),
            "ypp": d.yards_gained.mean(),
        }

    o = eff(off)
    o["proe_neutral"] = off[off.neutral].pass_oe.mean()
    o["pass_rate_neutral"] = off[off.neutral].pass_attempt.mean()
    # pace: seconds between snaps within a drive in neutral game state
    s = off.sort_values(["game_id", "play_id"])
    gap = s.groupby(["game_id", "drive"]).game_seconds_remaining.diff(-1)
    o["sec_per_play_neutral"] = gap[s.neutral & gap.between(5, 60)].mean()
    o["plays_per_game"] = len(off) / max(off.game_id.nunique(), 1)

    drives = pbp[(pbp.posteam == team) & pbp.fixed_drive_result.notna()]
    if weeks is not None:
        drives = drives[drives.week.isin(weeks)]
    d = drives.groupby(["game_id", "fixed_drive"]).agg(
        res=("fixed_drive_result", "first"), min_yl=("yardline_100", "min"))
    o["drives_per_game"] = len(d) / max(d.index.get_level_values(0).nunique(), 1)
    o["td_per_drive"] = (d.res == "Touchdown").mean()
    o["pts_per_drive"] = d.res.map({"Touchdown": 6.95, "Field goal": 3}).fillna(0).mean()
    rz = d[d.min_yl <= 20]
    o["rz_trips_per_game"] = len(rz) / max(d.index.get_level_values(0).nunique(), 1)
    o["rz_td_rate"] = (rz.res == "Touchdown").mean() if len(rz) else np.nan
    return {"team": team, "off": o, "def": eff(de)}


def league_baseline(pbp: pd.DataFrame) -> dict:
    q = _plays(pbp)
    return {
        "epa": q.epa.mean(), "success": q.success.mean(), "ypp": q.yards_gained.mean(),
        "pass_epa": q[q.pass_attempt == 1].epa.mean(), "rush_epa": q[q.rush_attempt == 1].epa.mean(),
        "comp_pct": q[q.pass_attempt == 1].complete_pass.mean(),
        "sack_rate": q[q.qb_dropback == 1].sack.mean(),
        "int_rate": q[q.pass_attempt == 1].interception.mean(),
        "ypc": q[(q.rush_attempt == 1) & (q.qb_scramble == 0)].yards_gained.mean(),
    }


def player_usage(pbp: pd.DataFrame, player_stats: pd.DataFrame, snaps: pd.DataFrame,
                 team: str, weeks: list[int]) -> pd.DataFrame:
    """Per-player usage over the chosen weeks: snap %, target/air-yard/carry share, RZ and GL work."""
    q = _plays(pbp)
    q = q[(q.posteam == team) & q.week.isin(weeks)]
    passes = q[(q.pass_attempt == 1) & q.receiver_player_name.notna()]
    runs = q[(q.rush_attempt == 1) & q.rusher_player_name.notna() & (q.qb_scramble == 0)]
    tgt = passes.groupby("receiver_player_id").agg(
        name=("receiver_player_name", "first"), targets=("play_id", "size"),
        rec=("complete_pass", "sum"), air=("air_yards", "sum"),
        rec_yds=("receiving_yards", "sum"),
        rz_tgt=("yardline_100", lambda s: (s <= 20).sum()))
    tgt["ez_tgt"] = passes.assign(ez=(passes.air_yards >= passes.yardline_100)).groupby("receiver_player_id").ez.sum()
    tgt["tgt_share"] = tgt.targets / len(passes)
    tgt["air_share"] = tgt.air / passes.air_yards.clip(lower=0).sum()
    tgt["rz_tgt_share"] = tgt.rz_tgt / max((passes.yardline_100 <= 20).sum(), 1)
    car = runs.groupby("rusher_player_id").agg(
        name=("rusher_player_name", "first"), carries=("play_id", "size"),
        rush_yds=("rushing_yards", "sum"),
        gl_car=("yardline_100", lambda s: (s <= 5).sum()),
        i10_car=("yardline_100", lambda s: (s <= 10).sum()))
    car["carry_share"] = car.carries / len(runs)
    car["gl_share"] = car.gl_car / max((runs.yardline_100 <= 5).sum(), 1)
    car["i10_share"] = car.i10_car / max((runs.yardline_100 <= 10).sum(), 1)
    df = tgt.join(car.drop(columns="name"), how="outer", rsuffix="_r")
    df["name"] = df["name"].fillna(car["name"])
    sn = snaps[(snaps.team == team) & snaps.week.isin(weeks)]
    sn = sn.groupby("player").agg(off_pct=("offense_pct", "mean"), games=("week", "nunique"))
    df = df.fillna({c: 0 for c in df.columns if c not in ("name",)})
    return df.sort_values("targets", ascending=False), sn.sort_values("off_pct", ascending=False)


def referee_profile(schedules_hist: pd.DataFrame, pbp_hist: pd.DataFrame | None, referee: str) -> dict:
    """Points and penalty tendencies for a referee's crew vs league over the loaded seasons."""
    s = schedules_hist[schedules_hist.total.notna()]
    mine = s[s.referee == referee]
    out = {"games": len(mine), "avg_total": mine.total.mean(), "league_avg_total": s.total.mean(),
           "over_rate_vs_close": (mine.total > mine.total_line).mean(),
           "league_over_rate": (s.total > s.total_line).mean(),
           "home_cover_rate": ((mine.result + mine.spread_line) > 0).mean() if len(mine) else np.nan}
    if pbp_hist is not None and len(pbp_hist):
        pen = pbp_hist[pbp_hist.penalty == 1].groupby("game_id").size()
        games = pbp_hist.groupby("game_id").size().index
        pen = pen.reindex(games, fill_value=0)
        ref_games = set(mine.game_id)
        out["pen_per_game"] = pen[pen.index.isin(ref_games)].mean()
        out["league_pen_per_game"] = pen.mean()
    return out
