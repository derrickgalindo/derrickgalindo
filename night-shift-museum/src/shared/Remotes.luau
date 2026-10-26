--!strict
-- Names of the RemoteEvents the server creates under ReplicatedStorage.Remotes.
-- Payload shapes are in Types.luau.

return table.freeze({
	FOLDER = "Remotes",
	ShiftState = "ShiftState", -- server -> all: ShiftState
	ItemArrived = "ItemArrived", -- server -> all: PublicItem (never says whether it is an anomaly)
	ItemResolved = "ItemResolved", -- server -> all: Resolution
	Toast = "Toast", -- server -> one or all: string
	Verdict = "Verdict", -- client -> server: (uid: number, verdict: Verdict)
})
