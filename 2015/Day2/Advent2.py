import re
import itertools
import math

boxes = []

with open("input.txt") as f:
	f = f.read().rstrip("\n")
	boxes = list(f.split("\n"))
#print(boxes)
surface_area = 0


for box in boxes:
	dimensions = list(box.split("x"))
	dimensions = [int(element) for element in dimensions]
	x, y, z = dimensions
	sides = [x*y, x*z, y*z]
	surface_area += 2 * sum(sides) + min(sides)

print(surface_area)

ribbon_length = 0

for box in boxes:
	dimensions = list(box.split("x"))
	dimensions = [int(element) for element in dimensions]
	x, y, z = dimensions
	perimeters = [2*x + 2*y, 2*x + 2*z, 2*y + 2*z]
	ribbon_length += min(perimeters) + math.prod(dimensions)

print(ribbon_length)
