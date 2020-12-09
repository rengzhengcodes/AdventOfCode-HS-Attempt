import re
import itertools

boxes = []

with open("input.txt") as f:
	f = f.read().rstrip("\n")
	boxes = list(f.split("\n"))
print(boxes)
surface_area = 0

for box in boxes:
	dimensions = list(box.split("x"))
	dimensions = [int(element) for element in dimensions]
	x, y, z = dimensions
	surface_area += 2*x*y + 2*x*z + 2*y*z

print(surface_area)
