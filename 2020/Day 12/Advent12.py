instructions = [line.strip() for line in open("input.txt").readlines()]
instructions = [(line[0], int(line[1:])) for line in instructions]

print(instructions)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direction = 0
x = 0
y = 0

for instruction in instructions:
	component, amount = instruction

	if component == "F":
		x_offset, y_offset = directions[direction]
		x += amount*x_offset
		y += amount*y_offset
	elif component == "N":
		x_offset, y_offset = directions[1]
		y += amount
	elif component == "S":
		x_offset, y_offset = directions[3]
		y -= amount
	elif component == "E":
		x_offset, y_offset = directions[0]
		x += amount
	elif component == "W":
		x_offset, y_offset = directions[2]
		x -= amount
	elif component == "L":
		direction += int(amount / 90)
		direction %= 4
	elif component == "R":
		direction -= int(amount / 90)
		direction %= 4

print(abs(x) + abs(y))

x = 0
y = 0
waypoint = (10, 1)
for instruction in instructions:
	component, amount = instruction

	if component == "F":
		for i in range(amount):
			x_offset, y_offset = waypoint
			x += x_offset
			y += y_offset
	elif component == "N":
		waypoint = (waypoint[0], waypoint[1] + amount)
	elif component == "S":
		waypoint = (waypoint[0], waypoint[1] - amount)
	elif component == "E":
		waypoint = (waypoint[0] + amount, waypoint[1])
	elif component == "W":
		waypoint = (waypoint[0] - amount, waypoint[1])
	elif component == "L":
		rotations = int(amount / 90)
		for i in range(rotations):
			waypoint = (-waypoint[1], waypoint[0])
	elif component == "R":
		rotations = int(amount / 90)
		for i in range(rotations):
			waypoint = (waypoint[1], -waypoint[0])

print(abs(x) + abs(y))
