--!strict
-- The shift loop: wait for guards -> countdown -> nights 1..N -> run over -> repeat.
-- One shift per server for now (set Max Players to 4 in Game Settings); a lobby with reserved servers comes later.
-- The server decides everything. Clients only see public item info and send a verdict, which is validated here.

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local TweenService = game:GetService("TweenService")

local Config = require(ReplicatedStorage.Shared.Config)
local Types = require(ReplicatedStorage.Shared.Types)
local Analytics = require(script.Parent.Analytics)
local Items = require(script.Parent.Items)
local Net = require(script.Parent.Net)
local PlayerData = require(script.Parent.PlayerData)
local World = require(script.Parent.World)

type Current = {
	uid: number,
	def: Items.ItemDef,
	body: Part,
	decideBy: number,
	resolved: boolean,
}

local ShiftService = {}

local layout: World.Layout
local rng = Random.new()
local nextUid = 0
local current: Current? = nil
local lastVerdictAt: { [Player]: number } = {}
local state: Types.ShiftState = {
	phase = "Waiting",
	night = 0,
	nights = Config.NIGHTS_PER_RUN,
	endsAt = 0,
	breaches = 0,
	maxBreaches = Config.MAX_BREACHES,
}

local function now(): number
	return workspace:GetServerTimeNow()
end

local function anyPlayers(): boolean
	return #Players:GetPlayers() > 0
end

local function broadcastState()
	Net.ShiftState:FireAllClients(state)
end

local function setPhase(phase: Types.Phase, seconds: number)
	state.phase = phase
	state.endsAt = now() + seconds
	broadcastState()
end

local function toastAll(text: string)
	Net.Toast:FireAllClients(text)
end

local function move(body: Part, def: Items.ItemDef, to: CFrame, seconds: number): Tween
	local goal = { CFrame = World.bodyCFrame(def, to) }
	local tween = TweenService:Create(body, TweenInfo.new(seconds, Enum.EasingStyle.Sine), goal)
	tween:Play()
	return tween
end

local function randomGallerySpot(): CFrame
	local half = layout.galleryHalfSize
	local position = Vector3.new(
		layout.gallery.X + rng:NextNumber(-half.X, half.X),
		0,
		layout.gallery.Z + rng:NextNumber(-half.Y, half.Y)
	)
	-- lookAt points -Z at the target; items' front face is +Z, so turn around to face the desk.
	local deskFloor = Vector3.new(layout.desk.X, 0, layout.desk.Z)
	return CFrame.lookAt(position, deskFloor) * CFrame.Angles(0, math.pi, 0)
end

local function arrive(def: Items.ItemDef): Current
	nextUid += 1
	local body = World.spawnItem(def, layout.entrance, layout.itemsFolder)
	move(body, def, layout.arrival, 3).Completed:Wait()
	local item: Current = {
		uid = nextUid,
		def = def,
		body = body,
		decideBy = math.min(now() + Config.DECISION_SECONDS, state.endsAt),
		resolved = false,
	}
	current = item
	local public: Types.PublicItem = {
		uid = item.uid,
		kind = def.kind,
		name = def.name,
		clues = def.clues,
		decideBy = item.decideBy,
	}
	Net.ItemArrived:FireAllClients(public)
	return item
end

local function resolve(item: Current, verdict: Types.Verdict, by: Player?)
	item.resolved = true
	if current == item then
		current = nil
	end

	local wasAnomaly = item.def.isAnomaly
	local correct = (verdict == "LockOut") == wasAnomaly
	if verdict == "LetIn" and wasAnomaly then
		state.breaches += 1
		broadcastState()
	end
	if by then
		Analytics.funnel(by, Analytics.Step.FirstVerdict, "FirstVerdict")
		if correct then
			PlayerData.addCoins(by, Config.COINS_CORRECT)
			Analytics.funnel(by, Analytics.Step.FirstCorrect, "FirstCorrect")
		end
		Analytics.custom(by, if correct then "VerdictCorrect" else "VerdictWrong")
	end

	local resolution: Types.Resolution = {
		uid = item.uid,
		verdict = verdict,
		correct = correct,
		wasAnomaly = wasAnomaly,
		by = if by then by.DisplayName else nil,
	}
	Net.ItemResolved:FireAllClients(resolution)

	local body, def = item.body, item.def
	if verdict == "LetIn" then
		-- Let-in items stay in the gallery; anomalies among them are what the patrol phase will hunt.
		move(body, def, randomGallerySpot(), 4)
	else
		move(body, def, layout.exit, 3).Completed:Once(function()
			body:Destroy()
		end)
	end
end

-- Returns true if the guards survived the night.
local function runNight(night: number): boolean
	state.night = night
	state.breaches = 0
	setPhase("Night", Config.NIGHT_SECONDS)
	toastAll(if night == 1 then "Night 1. Check everything that comes in." else `Night {night}. They're getting smarter.`)
	for _, player in Players:GetPlayers() do
		Analytics.custom(player, "NightStarted", night)
	end

	local queue = if night == 1 then Items.tutorial() else {}
	local anomalyChance = Config.BASE_ANOMALY_CHANCE + Config.ANOMALY_CHANCE_PER_NIGHT * (night - 1)

	while anyPlayers() and state.breaches < Config.MAX_BREACHES and state.endsAt - now() > 5 do
		local id = table.remove(queue, 1)
		local def = if id then Items.get(id) else Items.pick(night, anomalyChance, rng)
		local item = arrive(def)
		while not item.resolved and now() < item.decideBy do
			task.wait(0.1)
		end
		if not item.resolved then
			toastAll("Too slow. It walked right in.")
			resolve(item, "LetIn", nil)
		end
		task.wait(Config.ARRIVAL_GAP_SECONDS)
	end

	if state.breaches >= Config.MAX_BREACHES then
		toastAll("Too many got in. The museum is theirs now…")
		return false
	end
	while anyPlayers() and now() < state.endsAt do
		task.wait(0.25)
	end
	return anyPlayers()
end

local function runLoop()
	while true do
		state.night = 0
		state.breaches = 0
		setPhase("Waiting", 0)
		while not anyPlayers() do
			Players.PlayerAdded:Wait()
		end

		setPhase("Countdown", Config.LOBBY_COUNTDOWN_SECONDS)
		task.wait(Config.LOBBY_COUNTDOWN_SECONDS)
		if not anyPlayers() then
			continue
		end
		for _, player in Players:GetPlayers() do
			Analytics.funnel(player, Analytics.Step.ShiftStarted, "ShiftStarted")
			PlayerData.recordRun(player)
		end

		local survived = 0
		for night = 1, Config.NIGHTS_PER_RUN do
			if not runNight(night) then
				break
			end
			survived = night
			for _, player in Players:GetPlayers() do
				PlayerData.addCoins(player, Config.COINS_NIGHT_SURVIVED)
				PlayerData.recordNightSurvived(player, night)
				Analytics.nightSurvived(player, night)
			end
			if night < Config.NIGHTS_PER_RUN then
				toastAll(`Night {night} survived! +{Config.COINS_NIGHT_SURVIVED} coins`)
				setPhase("Intermission", Config.INTERMISSION_SECONDS)
				task.wait(Config.INTERMISSION_SECONDS)
			end
		end

		toastAll(
			if survived == Config.NIGHTS_PER_RUN
				then "You survived every night! The museum is safe… for now."
				else `Shift over. You survived {survived} of {Config.NIGHTS_PER_RUN} nights.`
		)
		setPhase("RunOver", Config.RUN_OVER_SECONDS)
		task.wait(Config.RUN_OVER_SECONDS)
		current = nil
		layout.itemsFolder:ClearAllChildren()
	end
end

local function onVerdict(player: Player, uid: unknown, verdict: unknown)
	if type(uid) ~= "number" or (verdict ~= "LetIn" and verdict ~= "LockOut") then
		return
	end
	local item = current
	if state.phase ~= "Night" or not item or item.resolved or item.uid ~= uid then
		return
	end

	local t = os.clock()
	if t - (lastVerdictAt[player] or -math.huge) < Config.VERDICT_COOLDOWN_SECONDS then
		return
	end
	lastVerdictAt[player] = t

	local character = player.Character
	local root = if character then character:FindFirstChild("HumanoidRootPart") else nil
	if not (root and root:IsA("BasePart")) or (root.Position - layout.desk).Magnitude > Config.DESK_REACH_STUDS then
		Net.Toast:FireClient(player, "Get back to the desk to decide!")
		return
	end

	resolve(item, verdict :: Types.Verdict, player)
end

function ShiftService.start(worldLayout: World.Layout)
	layout = worldLayout
	Net.Verdict.OnServerEvent:Connect(onVerdict)

	-- Late joiners get the current state (remote events queue until the client connects).
	Players.PlayerAdded:Connect(function(player)
		Net.ShiftState:FireClient(player, state)
		local item = current
		if item and not item.resolved then
			local public: Types.PublicItem = {
				uid = item.uid,
				kind = item.def.kind,
				name = item.def.name,
				clues = item.def.clues,
				decideBy = item.decideBy,
			}
			Net.ItemArrived:FireClient(player, public)
		end
	end)
	Players.PlayerRemoving:Connect(function(player)
		lastVerdictAt[player] = nil
	end)

	task.spawn(runLoop)
end

return ShiftService
