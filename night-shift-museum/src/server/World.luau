--!strict
-- Grey-box museum built in code, so the project runs from an empty baseplate.
-- Replace with real models later; ShiftService only needs the anchor points in Layout.

local Lighting = game:GetService("Lighting")

local Items = require(script.Parent.Items)

export type Layout = {
	desk: Vector3, -- where the guard stands to inspect
	arrival: CFrame, -- where items wait to be judged
	entrance: CFrame, -- where items come in from
	exit: CFrame, -- where locked-out items are taken
	gallery: Vector3, -- center of the gallery that let-in items walk into
	galleryHalfSize: Vector2, -- x/z half-extents for random gallery positions
	itemsFolder: Folder,
}

local World = {}

local function part(props: { [string]: any }, parent: Instance): Part
	local p = Instance.new("Part")
	p.Anchored = true
	p.TopSurface = Enum.SurfaceType.Smooth
	p.BottomSurface = Enum.SurfaceType.Smooth
	for key, value in props do
		(p :: any)[key] = value
	end
	p.Parent = parent
	return p
end

function World.build(): Layout
	local root = Instance.new("Folder")
	root.Name = "Greybox"
	root.Parent = workspace

	local baseplate = workspace:FindFirstChild("Baseplate")
	if baseplate then
		baseplate:Destroy()
	end

	part({ Name = "Floor", Size = Vector3.new(80, 1, 120), Position = Vector3.new(0, -0.5, 0), Color = Color3.fromRGB(60, 55, 50) }, root)
	-- Wall between the entrance hall (z < 0) and the gallery (z > 0), with a gap at the desk.
	part({ Name = "WallLeft", Size = Vector3.new(34, 14, 1), Position = Vector3.new(-23, 7, 0), Color = Color3.fromRGB(90, 85, 80) }, root)
	part({ Name = "WallRight", Size = Vector3.new(34, 14, 1), Position = Vector3.new(23, 7, 0), Color = Color3.fromRGB(90, 85, 80) }, root)
	part({ Name = "Desk", Size = Vector3.new(10, 3, 2), Position = Vector3.new(0, 1.5, 2), Color = Color3.fromRGB(100, 70, 45) }, root)
	local lamp = part({ Name = "DeskLamp", Size = Vector3.new(0.6, 0.6, 0.6), Position = Vector3.new(3.5, 3.4, 2), Material = Enum.Material.Neon, Color = Color3.fromRGB(255, 220, 150), CanCollide = false }, root)
	local light = Instance.new("PointLight")
	light.Range = 22
	light.Brightness = 2
	light.Color = Color3.fromRGB(255, 220, 160)
	light.Parent = lamp

	local spawn = Instance.new("SpawnLocation")
	spawn.Anchored = true
	spawn.Size = Vector3.new(6, 1, 6)
	spawn.Position = Vector3.new(0, 0.5, 8)
	spawn.Transparency = 1
	spawn.CanCollide = false
	spawn.Neutral = true
	spawn.Parent = root

	-- Night.
	Lighting.ClockTime = 0
	Lighting.Brightness = 1
	Lighting.Ambient = Color3.fromRGB(40, 40, 60)
	Lighting.OutdoorAmbient = Color3.fromRGB(30, 30, 45)

	local itemsFolder = Instance.new("Folder")
	itemsFolder.Name = "Items"
	itemsFolder.Parent = workspace

	return {
		desk = Vector3.new(0, 3, 5),
		arrival = CFrame.new(0, 0, -3),
		entrance = CFrame.new(0, 0, -45),
		exit = CFrame.new(18, 0, -45),
		gallery = Vector3.new(0, 0, 32),
		galleryHalfSize = Vector2.new(30, 22),
		itemsFolder = itemsFolder,
	}
end

-- Where an item's root part sits when the item stands at floor-level CFrame `at`.
-- Artwork is raised to chest height, as if on an easel.
function World.bodyCFrame(def: Items.ItemDef, at: CFrame): CFrame
	return at * CFrame.new(0, def.look.size.Y / 2 + (if def.kind == "Artwork" then 1.5 else 0), 0)
end

-- Builds the grey-box model for an item. Returns the anchored root part; decorations are welded to it,
-- so tweening the root's CFrame moves the whole item. The front face (+Z) faces the guard at the desk.
function World.spawnItem(def: Items.ItemDef, at: CFrame, parent: Instance): Part
	local look = def.look
	local body = part({
		Name = def.id,
		Size = look.size,
		CFrame = World.bodyCFrame(def, at),
		Color = look.color,
		CastShadow = not look.noShadow,
		CanCollide = false,
	}, parent)

	local function decor(size: Vector3, offset: CFrame, color: Color3, material: Enum.Material)
		local d = part({ Size = size, CFrame = body.CFrame * offset, Color = color, Material = material, CanCollide = false, Massless = true, CastShadow = not look.noShadow }, body)
		local weld = Instance.new("WeldConstraint")
		weld.Part0 = body
		weld.Part1 = d
		weld.Parent = d
		d.Anchored = false
	end

	if look.eyes then
		local front = look.size.Z / 2 + 0.05
		decor(Vector3.new(0.35, 0.2, 0.1), CFrame.new(-0.5, 0.4, front), Color3.fromRGB(255, 240, 150), Enum.Material.Neon)
		decor(Vector3.new(0.35, 0.2, 0.1), CFrame.new(0.5, 0.4, front), Color3.fromRGB(255, 240, 150), Enum.Material.Neon)
	end
	if look.glow then
		local glow = Instance.new("PointLight")
		glow.Range = 8
		glow.Color = Color3.fromRGB(255, 120, 60)
		glow.Parent = body
	end

	local billboard = Instance.new("BillboardGui")
	billboard.Size = UDim2.fromOffset(220, 40)
	billboard.StudsOffset = Vector3.new(0, look.size.Y / 2 + 1.2, 0)
	billboard.AlwaysOnTop = true
	billboard.MaxDistance = 60
	local label = Instance.new("TextLabel")
	label.Size = UDim2.fromScale(1, 1)
	label.BackgroundTransparency = 1
	label.Text = def.name
	label.TextScaled = true
	label.Font = Enum.Font.GothamBold
	label.TextColor3 = Color3.new(1, 1, 1)
	label.TextStrokeTransparency = 0.4
	label.Parent = billboard
	billboard.Parent = body

	return body
end

return World
