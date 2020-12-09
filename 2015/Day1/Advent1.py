import re
import itertools

instructions = ""

with open("input.txt") as f:
	f = f.read().rstrip("\n")
	instructions = f

print(instructions.count("(") - instructions.count(")"))

floor = 0
position = 0

for step in instructions:
	position += 1
	if step == "(":
		floor += 1
	elif step == ")":
		floor -= 1

	if floor == -1:
		print(position)
		break
