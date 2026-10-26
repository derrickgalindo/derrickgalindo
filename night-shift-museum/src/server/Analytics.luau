--!strict
-- Funnel and custom events for Creator Analytics. The analyst agent reads these.
-- Onboarding funnel steps must be logged in increasing order, once per player.

local AnalyticsService = game:GetService("AnalyticsService")
local Players = game:GetService("Players")

local Analytics = {}

Analytics.Step = table.freeze({
	Joined = 1,
	ShiftStarted = 2,
	FirstVerdict = 3,
	FirstCorrect = 4,
	-- Night N survived = 4 + N (5..9)
})

local reached: { [Player]: { [number]: boolean } } = {}

function Analytics.funnel(player: Player, step: number, stepName: string)
	local steps = reached[player]
	if not steps then
		steps = {}
		reached[player] = steps
	end
	if steps[step] then
		return
	end
	steps[step] = true
	local ok, err = pcall(function()
		AnalyticsService:LogOnboardingFunnelStepEvent(player, step, stepName)
	end)
	if not ok then
		warn(`[Analytics] funnel {stepName}: {err}`)
	end
end

function Analytics.nightSurvived(player: Player, night: number)
	Analytics.funnel(player, 4 + night, `Night{night}Survived`)
end

function Analytics.custom(player: Player, eventName: string, value: number?)
	local ok, err = pcall(function()
		AnalyticsService:LogCustomEvent(player, eventName, value or 1)
	end)
	if not ok then
		warn(`[Analytics] {eventName}: {err}`)
	end
end

function Analytics.start()
	Players.PlayerAdded:Connect(function(player)
		Analytics.funnel(player, Analytics.Step.Joined, "Joined")
	end)
	Players.PlayerRemoving:Connect(function(player)
		reached[player] = nil
	end)
end

return Analytics
