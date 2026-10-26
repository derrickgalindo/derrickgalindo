--!strict
-- Every artwork and visitor that can arrive at the desk, as data.
-- Server-only on purpose: clients must never be able to read isAnomaly.
-- To add content, add a row. Anomalies copy a normal item and change one clue (and optionally its look).

local Types = require(game:GetService("ReplicatedStorage").Shared.Types)

export type Look = {
	color: Color3,
	size: Vector3,
	eyes: boolean?, -- two glowing eyes on the front face
	glow: boolean?, -- warm point light
	noShadow: boolean?,
}

export type ItemDef = {
	id: string,
	kind: Types.ItemKind,
	name: string,
	clues: { string },
	isAnomaly: boolean,
	minNight: number,
	look: Look,
}

local PAINTING = Vector3.new(4, 3, 0.4)
local BUST = Vector3.new(1.6, 2.4, 1.6)
local VASE = Vector3.new(1.2, 2, 1.2)
local PERSON = Vector3.new(2, 5, 1)

local OIL = Color3.fromRGB(70, 90, 120)
local DUKE = Color3.fromRGB(110, 70, 50)
local MARBLE = Color3.fromRGB(225, 225, 220)
local PORCELAIN = Color3.fromRGB(60, 90, 200)
local MIRROR = Color3.fromRGB(190, 200, 210)
local CLEANER = Color3.fromRGB(70, 130, 90)
local COURIER = Color3.fromRGB(150, 110, 60)

local NOTE_OK = "Delivery note signed by the curator"

local DEFS: { ItemDef } = {
	-- Normal items
	{ id = "harbor", kind = "Artwork", name = "Landscape: Harbor at Dusk", isAnomaly = false, minNight = 1,
		clues = { "Oil on canvas, varnish dry", "The sun is setting over the water", NOTE_OK },
		look = { color = OIL, size = PAINTING } },
	{ id = "duke", kind = "Artwork", name = "Portrait of a Duke", isAnomaly = false, minNight = 1,
		clues = { "The duke looks to the left", "Gold frame, slightly chipped", NOTE_OK },
		look = { color = DUKE, size = PAINTING } },
	{ id = "bust", kind = "Artwork", name = "Marble Bust", isAnomaly = false, minNight = 1,
		clues = { "Cold to the touch", "Chisel marks on the base", "Heavy, about 40 kg" },
		look = { color = MARBLE, size = BUST } },
	{ id = "vase", kind = "Artwork", name = "Blue Porcelain Vase", isAnomaly = false, minNight = 1,
		clues = { "Hairline crack near the rim", "Completely silent", "Catalogue number matches" },
		look = { color = PORCELAIN, size = VASE } },
	{ id = "mirror", kind = "Artwork", name = "Ornate Mirror", isAnomaly = false, minNight = 1,
		clues = { "Reflects the room, and you", "Silver leaf frame", "Catalogue number matches" },
		look = { color = MIRROR, size = PAINTING } },
	{ id = "cleaner", kind = "Visitor", name = "Night Cleaner", isAnomaly = false, minNight = 1,
		clues = { "Badge photo matches their face", "Casts a normal shadow", "Smells like lemon floor polish" },
		look = { color = CLEANER, size = PERSON } },
	{ id = "courier", kind = "Visitor", name = "Late Courier", isAnomaly = false, minNight = 1,
		clues = { "Ticket dated tonight", "Five fingers on each hand", "Clipboard lists tonight's deliveries" },
		look = { color = COURIER, size = PERSON } },

	-- Anomalies (12)
	{ id = "duke_eyes", kind = "Artwork", name = "Portrait of a Duke", isAnomaly = true, minNight = 1,
		clues = { "The duke's eyes follow you", "Gold frame, slightly chipped", NOTE_OK },
		look = { color = DUKE, size = PAINTING, eyes = true } },
	{ id = "mirror_empty", kind = "Artwork", name = "Ornate Mirror", isAnomaly = true, minNight = 1,
		clues = { "Reflects the room, but not you", "Silver leaf frame", "Catalogue number matches" },
		look = { color = MIRROR, size = PAINTING } },
	{ id = "bust_warm", kind = "Artwork", name = "Marble Bust", isAnomaly = true, minNight = 1,
		clues = { "Warm to the touch", "Chisel marks on the base", "Heavy, about 40 kg" },
		look = { color = MARBLE, size = BUST, glow = true } },
	{ id = "harbor_wet", kind = "Artwork", name = "Landscape: Harbor at Dusk", isAnomaly = true, minNight = 1,
		clues = { "The paint is still wet", "The sun is setting over the water", NOTE_OK },
		look = { color = OIL, size = PAINTING } },
	{ id = "cleaner_shadow", kind = "Visitor", name = "Night Cleaner", isAnomaly = true, minNight = 1,
		clues = { "Badge photo matches their face", "Casts no shadow", "Smells like lemon floor polish" },
		look = { color = CLEANER, size = PERSON, noShadow = true } },
	{ id = "vase_hum", kind = "Artwork", name = "Blue Porcelain Vase", isAnomaly = true, minNight = 2,
		clues = { "Hairline crack near the rim", "Hums when you look away", "Catalogue number matches" },
		look = { color = PORCELAIN, size = VASE } },
	{ id = "harbor_sunrise", kind = "Artwork", name = "Landscape: Harbor at Dusk", isAnomaly = true, minNight = 2,
		clues = { "Oil on canvas, varnish dry", "The sun is rising, not setting", NOTE_OK },
		look = { color = OIL, size = PAINTING } },
	{ id = "courier_1887", kind = "Visitor", name = "Late Courier", isAnomaly = true, minNight = 2,
		clues = { "Ticket dated 1887", "Five fingers on each hand", "Clipboard lists tonight's deliveries" },
		look = { color = COURIER, size = PERSON } },
	{ id = "courier_fingers", kind = "Visitor", name = "Late Courier", isAnomaly = true, minNight = 3,
		clues = { "Ticket dated tonight", "Six fingers on each hand", "Clipboard lists tonight's deliveries" },
		look = { color = COURIER, size = PERSON } },
	{ id = "cleaner_badge", kind = "Visitor", name = "Night Cleaner", isAnomaly = true, minNight = 3,
		clues = { "Badge photo is someone else", "Casts a normal shadow", "Smells like lemon floor polish" },
		look = { color = CLEANER, size = PERSON } },
	{ id = "bust_breathing", kind = "Artwork", name = "Marble Bust", isAnomaly = true, minNight = 4,
		clues = { "Cold to the touch", "Its chest rises and falls", "Heavy, about 40 kg" },
		look = { color = MARBLE, size = BUST } },
	{ id = "duke_signed", kind = "Artwork", name = "Portrait of a Duke", isAnomaly = true, minNight = 4,
		clues = { "The duke looks to the left", "Gold frame, slightly chipped", "Delivery note signed by the duke" },
		look = { color = DUKE, size = PAINTING } },
}

-- Night 1 opens with an obvious anomaly, then a harmless visitor (the pitch's first-60-seconds script).
local TUTORIAL: { string } = { "duke_eyes", "cleaner" }

local byId: { [string]: ItemDef } = {}
local normals: { ItemDef } = {}
local anomalies: { ItemDef } = {}
for _, def in DEFS do
	assert(byId[def.id] == nil, `duplicate item id {def.id}`)
	byId[def.id] = def
	table.insert(if def.isAnomaly then anomalies else normals, def)
end

local Items = {}

function Items.get(id: string): ItemDef
	local def = byId[id]
	assert(def, `unknown item id {id}`)
	return def
end

function Items.tutorial(): { string }
	return table.clone(TUTORIAL)
end

function Items.pick(night: number, anomalyChance: number, rng: Random): ItemDef
	local pool = if rng:NextNumber() < anomalyChance then anomalies else normals
	local eligible = {}
	for _, def in pool do
		if def.minNight <= night then
			table.insert(eligible, def)
		end
	end
	return eligible[rng:NextInteger(1, #eligible)]
end

return Items
