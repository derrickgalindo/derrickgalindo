--!strict
-- Types shared by server and client. Item answers (isAnomaly) live only in ServerScriptService.

export type Phase = "Waiting" | "Countdown" | "Night" | "Intermission" | "RunOver"
export type Verdict = "LetIn" | "LockOut"
export type ItemKind = "Artwork" | "Visitor"

export type ShiftState = {
	phase: Phase,
	night: number,
	nights: number,
	endsAt: number, -- workspace:GetServerTimeNow() when the current phase ends
	breaches: number,
	maxBreaches: number,
}

-- What clients are told about the item at the desk.
export type PublicItem = {
	uid: number,
	kind: ItemKind,
	name: string,
	clues: { string },
	decideBy: number, -- server time when the item is waved through
}

export type Resolution = {
	uid: number,
	verdict: Verdict,
	correct: boolean,
	wasAnomaly: boolean,
	by: string?, -- display name of the guard who decided; nil if it timed out
}

return {}
