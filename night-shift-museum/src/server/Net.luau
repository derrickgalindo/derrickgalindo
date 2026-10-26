--!strict
-- Creates the RemoteEvents listed in Shared/Remotes. Required once by the server before anything fires.

local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Remotes = require(ReplicatedStorage.Shared.Remotes)

local folder = Instance.new("Folder")
folder.Name = Remotes.FOLDER

local function event(name: string): RemoteEvent
	local remote = Instance.new("RemoteEvent")
	remote.Name = name
	remote.Parent = folder
	return remote
end

local Net = {
	ShiftState = event(Remotes.ShiftState),
	ItemArrived = event(Remotes.ItemArrived),
	ItemResolved = event(Remotes.ItemResolved),
	Toast = event(Remotes.Toast),
	Verdict = event(Remotes.Verdict),
}

folder.Parent = ReplicatedStorage

return Net
