"""20 solo-buildable concepts, coded on the same variables as the dataset, scored by the backtested models.
Writes analysis/concepts.md and the `concepts` table in the DB."""
import os, sqlite3, sys
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "model"))
import fit_model as fm

# name | platform | pitch | session_min | ttff_sec | one_input | rules_preknown | share_artifact | artifact_curiosity | invite_needed |
# daily_sync | scarcity | social_graph | spectator | failure_comedy | emergent_output | free | ip | creator_audience | paid_ua |
# platform_newness | novelty | build_weeks | llm_cost | crowding (count of near-identical live games: 0 none, 1 some, 2 many)
CONCEPTS = """
Group-Chat Fibbage|web|One prompt a day ('What's the real reason koalas sleep 20 hours?'). Friends in a group link each write a fake answer, then everyone votes for the truth; the reveal is a shareable card of the funniest lies.|4|20|1|1|2|1|1|1|1|2|2|1|1|1|0|0|0|1|1|3|0|1
Talk Your Way Out|web|Daily AI gatekeeper with a secret password; you get 5 messages to talk your way past. The share card shows your shortest winning line and the AI's best rebuttal.|4|10|1|0|2|1|0|1|1|0|2|1|1|1|0|0|0|0|2|3|1|1
Telephone Pictionary Chains|web|Async telephone game in a group chat (draw -> describe -> draw); each chain ends as a 6-second GIF for the group.|5|20|1|1|2|0|1|0|0|2|2|1|1|1|0|0|0|0|1|4|0|1
Dupe Day|web|5 pairs a day: real photo or AI fake? Emoji grid of your hits and misses, plus a percentile.|2|5|1|0|2|1|0|1|1|0|1|1|0|1|0|0|0|0|1|2|0|1
Timeline Daily|web|Place 6 events in order (Timeline card-game rules); daily grid.|3|10|1|1|2|1|0|1|1|0|0|0|0|1|0|0|0|0|1|2|0|2
Couple's Daily|web|Two-player co-op daily puzzle: each partner sees half the clues; share card = joint time.|5|20|1|1|2|1|1|1|1|2|0|0|0|1|0|0|0|0|1|4|0|0
Who's Most Likely (Group Edition)|web|Friends answer 'who in this group is most likely to...' about each other; results reveal as superlatives cards.|4|15|1|1|2|1|1|1|0|2|1|1|1|1|0|0|0|0|1|3|0|1
Infinite Kitchen|web|Combine ingredients; an LLM invents (and caches) the dish; a daily target dish to reach in the fewest steps.|10|5|1|0|1|0|0|1|0|0|2|1|1|1|0|0|0|0|0|4|1|1
Higher-Lower Daily|web|Which has more (Google searches, calories, population)? Daily streak grid.|2|5|1|1|2|1|0|1|1|0|0|0|0|1|0|0|0|0|0|1|0|2
Cricket Immaculate Grid|web|Immaculate Grid for cricket fans (South Asia, UK, Australia).|5|20|1|1|2|1|0|1|1|0|0|0|0|1|0|0|0|0|0|2|0|1
Hide as a Painting|roblox|Prop-hunt in a haunted museum: hiders become paintings and statues, seekers hunt them; daily new gallery layout.|10|30|0|1|1|0|0|0|0|2|2|1|1|1|0|0|0|1|1|6|0|1
Daily Heist|roblox|Everyone on Roblox gets the same co-op escape room each day; servers race; global leaderboard and 'first squad' badges.|12|30|0|1|1|0|1|1|1|2|2|1|1|1|0|0|0|1|2|8|0|1
Grow-a-[New Theme] Live-Ops|roblox|Idle grow-and-steal loop with offline growth, restocks and weekly admin events, in an unclaimed theme.|15|30|1|0|1|0|0|0|1|2|1|0|0|1|0|0|0|1|0|5|0|2
Imposter Bot|roblox|Social deduction where one 'player' in every lobby is an AI; find the bot before it convinces you that you are the bot.|10|30|0|1|0|0|1|0|0|2|2|1|1|1|0|0|0|1|2|8|1|1
Pictionary Obby|roblox|Race an obstacle course where the course is drawn live by the previous winner.|10|30|0|1|1|0|0|0|0|2|2|1|1|1|0|0|0|1|2|8|0|1
Rage Hop Replays|mobile|One-tap rage platformer that auto-cuts your best fail into a 6-second vertical clip with the level seed.|1|3|1|0|2|0|0|1|0|0|2|1|0|1|0|0|0|0|1|3|0|2
Server Daily Quiz|discord|Discord Activity: the whole server plays the same 5 questions daily; leaderboard posted in channel.|3|15|1|1|2|0|0|1|1|2|1|0|0|1|0|0|0|2|1|4|0|1
Community Crossword (Reddit)|reddit|Reddit Devvit game: a subreddit co-builds and solves a daily crossword about its own topic.|10|30|1|1|1|0|0|1|0|1|1|0|1|1|0|0|0|2|1|4|0|0
Guess the Year|web|One photo a day; guess the year on a slider; grid of how close you got.|2|5|1|0|2|1|0|1|1|0|1|0|0|1|0|0|0|0|0|2|0|2
Two Truths Live|mobile|Async 'two truths and a lie' with friends using camera-roll photos; reveal reel at the end.|4|30|1|1|2|0|1|0|0|2|1|1|1|1|0|0|0|0|1|5|0|1
"""

COLS = ["name", "platform", "pitch", "session_min", "ttff_sec", "one_input", "rules_preknown", "share_artifact", "artifact_curiosity",
        "invite_needed", "daily_sync", "scarcity", "social_graph", "spectator", "failure_comedy", "emergent_output", "free_to_play",
        "ip_licensed", "creator_audience", "paid_ua", "platform_newness", "novelty", "build_weeks", "llm_cost", "crowding"]

# Channel evidence (zero-paid-marketing breakouts to ~1M+ DAU, 2022-2026, in the dataset + Roblox letters)
CHANNEL = {"roblox": ("high", "Grow a Garden, Steal a Brainrot, 99 Nights, Dead Rails, Dress to Impress: several per year, algorithmic discovery, free hosting"),
           "web": ("medium-low", "Wordle (2022), plus creator-audience/platform launches (Infinite Craft, Password Game, Connections, Queens); daily-word cohort saturated"),
           "mobile": ("low", "organic zero-budget breakouts rare since hypercasual paid UA (Rovio UA EUR69.6M in 2017; Block Blast paid)"),
           "discord": ("unproven", "Discord Activities open to developers since 2024; no 1M-DAU zero-budget case found"),
           "reddit": ("unproven", "Reddit developer platform games; no 1M-DAU case found")}
ARPDAU_MID = {"web": 0.012, "roblox": 0.012, "mobile": 0.05, "discord": 0.005, "reddit": 0.005}


def coded():
    rows = [dict(zip(COLS, l.split("|"))) for l in CONCEPTS.strip().splitlines()]
    df = pd.DataFrame(rows)
    for c in COLS[3:]:
        df[c] = df[c].astype(float)
    df["short_session"] = (df.session_min <= 5).astype(int)
    df["fast_ttff"] = (df.ttff_sec <= 10).astype(int)
    df["share_in_product"] = (df.share_artifact >= 2).astype(int)
    df["daily_or_scarcity"] = ((df.daily_sync == 1) | (df.scarcity == 1)).astype(int)
    df["friends_graph"] = (df.social_graph >= 2).astype(int)
    df["has_audience"] = (df.creator_audience >= 1).astype(int)
    df["new_channel"] = (df.platform_newness >= 2).astype(int)
    df["novel"] = (df.novelty >= 1).astype(int)
    df["spectator_high"] = (df.spectator >= 2).astype(int)
    return df


def main():
    train = fm.load(False)
    full_feats = fm.CONVENTIONAL + fm.CONTEXT + fm.NOVEL
    f_full, coefs = fm.fit(train, full_feats)
    f_conv, _ = fm.fit(train, fm.CONVENTIONAL + fm.CONTEXT)
    f_spec, _ = fm.fit(train, fm.CONVENTIONAL + ["spectator_high"])
    df = coded()
    df["p_full"] = f_full(df)
    df["p_conv_context"] = f_conv(df)
    df["p_conv_plus_spectator"] = f_spec(df)
    # rank-average of the three model variants, so no single fit dominates
    df["model_score"] = df[["p_full", "p_conv_context", "p_conv_plus_spectator"]].rank(pct=True).mean(axis=1)
    df["channel_evidence"] = df.platform.map(lambda p: CHANNEL[p][0])
    df["rev_1M_dau_yr_M"] = df.platform.map(ARPDAU_MID) * 365
    df = df.sort_values("model_score", ascending=False).reset_index(drop=True)
    df["rank"] = np.arange(1, len(df) + 1)
    con = sqlite3.connect(os.path.join(ROOT, "data", "viral_games.db"))
    con.execute("DELETE FROM concepts")
    for r in df.itertuples():
        con.execute("INSERT INTO concepts VALUES (?,?,?,?,?,?,?)", (r.rank, r.name, r.platform, r.pitch, float(r.model_score), int(r.rank),
                    f"p_full={r.p_full:.2f}; p_conv_ctx={r.p_conv_context:.2f}; p_conv+spec={r.p_conv_plus_spectator:.2f}; channel={r.channel_evidence}; crowding={int(r.crowding)}; build_weeks={int(r.build_weeks)}"))
    con.commit(); con.close()
    L = ["# 20 concepts scored against the model", "",
         "Scores come from the models fit on all 122 non-Telegram games: full, conventional+context, and conventional+spectator. They are rank-averaged.",
         "The model has known blind spots (see the backtest), so channel evidence, crowding and build cost are shown next to the score, not folded into it.", "",
         "| Rank | Concept | Platform | Model score | P(hit) full | P(hit) conv+ctx | P(hit) conv+spectator | Channel evidence | Crowding | Build (weeks) | LLM cost | Revenue/yr at 1M DAU (mid) |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in df.itertuples():
        L.append(f"| {r.rank} | {r.name} | {r.platform} | {r.model_score:.2f} | {r.p_full:.2f} | {r.p_conv_context:.2f} | {r.p_conv_plus_spectator:.2f} | "
                 f"{r.channel_evidence} | {['none', 'some', 'many'][int(r.crowding)]} | {int(r.build_weeks)} | {'yes' if r.llm_cost else 'no'} | ${r.rev_1M_dau_yr_M:.1f}M |")
    L += ["", "## Pitches", ""] + [f"- **{r.name}** ({r.platform}): {r.pitch}" for r in df.itertuples()]
    L += ["", "## Full-model coefficients used for scoring (standardized)", ""] + [f"- `{k}`: {v:+.2f}" for k, v in sorted(coefs.items(), key=lambda kv: -abs(kv[1]))]
    open(os.path.join(ROOT, "analysis", "concepts.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
