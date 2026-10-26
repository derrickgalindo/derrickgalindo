--!strict
-- Tunables for the shift loop. Balance the game here, not inside the services.

local Config = {
	NIGHTS_PER_RUN = 5,
	NIGHT_SECONDS = 180,
	LOBBY_COUNTDOWN_SECONDS = 10,
	INTERMISSION_SECONDS = 10,
	RUN_OVER_SECONDS = 8,

	-- Pause between one item leaving the desk and the next one arriving.
	ARRIVAL_GAP_SECONDS = 2,
	-- An item left at the desk this long is waved through (counts as "let in").
	DECISION_SECONDS = 15,
	-- Anomalies let in before the night is lost.
	MAX_BREACHES = 3,

	-- Chance the next arrival is an anomaly: base + per night (night 1 = base).
	BASE_ANOMALY_CHANCE = 0.3,
	ANOMALY_CHANCE_PER_NIGHT = 0.06,

	COINS_CORRECT = 5,
	COINS_NIGHT_SURVIVED = 25,

	-- Anti-spam and anti-teleport limits for the Verdict remote.
	VERDICT_COOLDOWN_SECONDS = 0.3,
	DESK_REACH_STUDS = 30,

	AUTOSAVE_SECONDS = 120,
}

return table.freeze(Config)
