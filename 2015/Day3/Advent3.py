import re
import itertools

instructions = "";
with open("input.txt") as f:
	f = f.read().rstrip("\n")
	instructions = f

coord = (0, 0)
houses_to_presents = dict()
houses_to_presents[coord] = 1
for char in instructions:
	x, y = coord
	if char == ">":
		x += 1
	elif char == "<":
		x -= 1
	elif char == "^":
		y += 1
	elif char == "v":
		y -= 1
	coord = (x, y)
	if coord in houses_to_presents:
		houses_to_presents[coord] += 1
	else:
		houses_to_presents[coord] = 1

print(len(houses_to_presents))

santa_coord = (0, 0)
robo_coord = (0, 0)
houses_to_presents = dict()
houses_to_presents[santa_coord] = 1
houses_to_presents[robo_coord] += 1
index = 0
for char in instructions:
	if index % 2 == 0:
		x, y = santa_coord
		if char == ">":
			x += 1
		elif char == "<":
			x -= 1
		elif char == "^":
			y += 1
		elif char == "v":
			y -= 1
		santa_coord = (x, y)
		if santa_coord in houses_to_presents:
			houses_to_presents[santa_coord] += 1
		else:
			houses_to_presents[santa_coord] = 1
	else:
		x, y = robo_coord
		if char == ">":
			x += 1
		elif char == "<":
			x -= 1
		elif char == "^":
			y += 1
		elif char == "v":
			y -= 1
		robo_coord = (x, y)
		if robo_coord in houses_to_presents:
			houses_to_presents[robo_coord] += 1
		else:
			houses_to_presents[robo_coord] = 1
	index += 1
print(len(houses_to_presents))
