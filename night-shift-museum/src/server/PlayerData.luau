--!strict
-- Saves coins and progress with DataStoreService.
-- If loading fails (or Studio has no API access), the player plays on defaults and nothing is saved,
-- so a failed load can never overwrite real data.
-- Before selling anything for Robux, switch to session locking (ProfileStore) and idempotent receipts.

local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")

local Config = require(game:GetService("ReplicatedStorage").Shared.Config)

export type Profile = {
	version: number,
	coins: number,
	bestNight: number,
	nightsSurvived: number,
	runs: number,
}

local SCHEMA_VERSION = 1
local DEFAULT: Profile = { version = SCHEMA_VERSION, coins = 0, bestNight = 0, nightsSurvived = 0, runs = 0 }

local store = DataStoreService:GetDataStore("PlayerData_v1")
local profiles: { [Player]: Profile } = {}
local canSave: { [Player]: boolean } = {}

local PlayerData = {}

local function key(player: Player): string
	return `u_{player.UserId}`
end

-- Fill in fields added since the data was saved.
local function reconcile(saved: any): Profile
	local profile = table.clone(DEFAULT)
	if type(saved) == "table" then
		for field, default in DEFAULT :: any do
			if type(saved[field]) == type(default) then
				(profile :: any)[field] = saved[field]
			end
		end
	end
	profile.version = SCHEMA_VERSION
	return profile
end

local function setStat(player: Player, name: string, value: number)
	local leaderstats = player:FindFirstChild("leaderstats")
	local stat = leaderstats and leaderstats:FindFirstChild(name)
	if stat and stat:IsA("IntValue") then
		stat.Value = value
	end
end

local function makeLeaderstats(player: Player, profile: Profile)
	local folder = Instance.new("Folder")
	folder.Name = "leaderstats"
	for _, entry in { { "Coins", profile.coins }, { "Best Night", profile.bestNight } } do
		local value = Instance.new("IntValue")
		value.Name = entry[1] :: string
		value.Value = entry[2] :: number
		value.Parent = folder
	end
	folder.Parent = player
end

local function load(player: Player)
	local loaded: Profile? = nil
	for attempt = 1, 3 do
		local ok, result = pcall(function()
			return store:GetAsync(key(player))
		end)
		if ok then
			loaded = reconcile(result)
			break
		end
		warn(`[PlayerData] load failed for {player.UserId} (attempt {attempt}): {result}`)
		task.wait(2 ^ attempt)
	end
	if not player.Parent then
		return
	end
	canSave[player] = loaded ~= nil
	local profile = loaded or table.clone(DEFAULT)
	profiles[player] = profile
	makeLeaderstats(player, profile)
end

local function save(player: Player)
	local profile = profiles[player]
	if not profile or not canSave[player] then
		return
	end
	local snapshot = table.clone(profile)
	for attempt = 1, 3 do
		local ok, err = pcall(function()
			store:UpdateAsync(key(player), function()
				return snapshot
			end)
		end)
		if ok then
			return
		end
		warn(`[PlayerData] save failed for {player.UserId} (attempt {attempt}): {err}`)
		task.wait(attempt)
	end
end

function PlayerData.get(player: Player): Profile?
	return profiles[player]
end

function PlayerData.addCoins(player: Player, amount: number)
	local profile = profiles[player]
	if profile then
		profile.coins += amount
		setStat(player, "Coins", profile.coins)
	end
end

function PlayerData.recordNightSurvived(player: Player, night: number)
	local profile = profiles[player]
	if profile then
		profile.nightsSurvived += 1
		if night > profile.bestNight then
			profile.bestNight = night
			setStat(player, "Best Night", night)
		end
	end
end

function PlayerData.recordRun(player: Player)
	local profile = profiles[player]
	if profile then
		profile.runs += 1
	end
end

function PlayerData.start()
	Players.PlayerAdded:Connect(load)
	for _, player in Players:GetPlayers() do
		task.spawn(load, player)
	end
	Players.PlayerRemoving:Connect(function(player)
		save(player)
		profiles[player] = nil
		canSave[player] = nil
	end)
	game:BindToClose(function()
		local pending = 0
		for _, player in Players:GetPlayers() do
			pending += 1
			task.spawn(function()
				save(player)
				pending -= 1
			end)
		end
		while pending > 0 do
			task.wait()
		end
	end)
	task.spawn(function()
		while true do
			task.wait(Config.AUTOSAVE_SECONDS)
			for _, player in Players:GetPlayers() do
				task.spawn(save, player)
			end
		end
	end)
end

return PlayerData
