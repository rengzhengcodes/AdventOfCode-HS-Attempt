import copy

seatgrid = []
def formatgrid(grid):
	output = ""
	for line in grid:
		for char in line:
			output += char
		output += "\n"
	return output

with open("input.txt") as f:
	seatgrid = [list(line.strip()) for line in f.readlines()]

testgrid = [list(line.strip()) for line in open("test.txt").readlines()]

def number_adjacent(current_pos, grid):
	adjacent = 0
	x, y = current_pos
	relative_positions = [(-1, 1), (0, 1), (1, 1),
						  (-1, 0),		   (1, 0),
						  (-1,-1), (0,-1), (1, -1)]

	for relative in relative_positions:
		x_offset, y_offset = relative
		try:

			if not (x + x_offset < 0 or y + y_offset < 0) and (grid[x + x_offset][y + y_offset] == "#"):
				adjacent += 1
		except IndexError:
			continue

	return adjacent

def number_adjacent_test():
	test = [list("###"),list("###"),list("###")]
	for x in range(3):
		for y in range(3):
			print(number_adjacent((x, y), test))

#number_adjacent_test()

def seatfill(grid, tolerance, adjacent_algo):
	original = copy.deepcopy(grid)
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			pos = (x, y)
			status = original[x][y]
			if status == "L" and adjacent_algo(pos, original) == 0:
				grid[x][y] = "#"
			elif status == "#" and adjacent_algo(pos, original) >= tolerance:
				grid[x][y] = "L"

#print(formatgrid(testgrid))

def equilibrium(grid, tolerance, adjacent_algo):
	original = copy.deepcopy(grid)
	seatfill(grid, tolerance, adjacent_algo)

	while(original != grid):
		original = copy.deepcopy(grid)
		seatfill(grid, tolerance, adjacent_algo)

	return grid

##print(formatgrid(equilibrium(testgrid)))

print(str(equilibrium(seatgrid, 4, number_adjacent)).count("#"))

def revised_adjacent(current_pos, grid):
	adjacent = 0
	x, y = current_pos
	relative_positions = [(-1, 1), (0, 1), (1, 1),
						  (-1, 0),		   (1, 0),
						  (-1,-1), (0,-1), (1, -1)]

	for relative in relative_positions:
		x_offset, y_offset = relative
		x_direction, y_direction = relative
		try:
			while True:
				if x + x_offset < 0 or y + y_offset < 0:
					break
				else:
					status = grid[x + x_offset][y + y_offset]
				if status == "#":
					adjacent += 1
					break
				elif status == "L":
					break
				else:
					x_offset += x_direction
					y_offset += y_direction
		except IndexError:
			continue

	return adjacent

def revised_adjacent_test():
	print(revised_adjacent((4,3), [list(line.strip()) for line in open("revisedadjtest1.txt").readlines()]))
	print(revised_adjacent((1,1), [list(line.strip()) for line in open("revisedadjtest2.txt").readlines()]))
	print(revised_adjacent((3,3), [list(line.strip()) for line in open("revisedadjtest3.txt").readlines()]))

#revised_adjacent_test()

seatgrid = [list(line.strip()) for line in open("input.txt").readlines()]

print(str(equilibrium(seatgrid, 5, revised_adjacent)).count("#"))
