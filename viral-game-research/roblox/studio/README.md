# Studio: agent team

Seven agents, defined in `/.claude/agents/`. Each stands in for a role on the small teams behind Roblox hits (see `../STUDIO_BLUEPRINT.md`). Their output goes in the folders here.

| Agent | Role on a hit team | Writes to | When |
|---|---|---|---|
| `trend-scout` | studio scout | `teardowns/` | weekly, after the chart refresh |
| `game-designer` | design lead / director | `design/` | pitch → design doc → build reviews |
| `luau-engineer` | programmer | the Roblox project repo | whenever there's code to write |
| `economy-designer` | economy / monetization | `economy/` | before the retention-and-money step, then on each rebalance |
| `liveops-producer` | events team | `liveops/` | from 3 weeks before launch, then weekly |
| `analyst` | data lead | `analytics/` | weekly after launch (drop Creator Analytics CSVs into `analytics/raw/<date>/`) |
| `packaging-community` | growth + community | `packaging/` | before the soft launch, then with each update |

**How to use them:** ask in plain words, e.g. "have the game-designer write a pitch for Night-Shift Museum", or "run the analyst on this week's export". Claude Code picks up the agents in new sessions automatically.

**The order through idea → release** (the steps in STUDIO_BLUEPRINT.md):

trend-scout (1) → game-designer pitch (1) → luau-engineer jam prototype (2) → game-designer playtest review (3) → luau-engineer vertical slice (4) → economy-designer (5) → packaging-community (6) → soft launch (7) → liveops-producer weekly (8) → analyst weekly (9)

**Still done by people:**
- **3D building, art and animation:** Creator Store assets, freelancers, or Roblox's AI 3D tool.
- **Watching real players.**
