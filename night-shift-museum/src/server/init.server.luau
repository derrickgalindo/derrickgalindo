--!strict
-- Server entry point. Rojo turns this folder into a Script named "Server" with the modules as children.

local Analytics = require(script.Analytics)
local PlayerData = require(script.PlayerData)
local ShiftService = require(script.ShiftService)
local World = require(script.World)

local layout = World.build()
Analytics.start()
PlayerData.start()
ShiftService.start(layout)
