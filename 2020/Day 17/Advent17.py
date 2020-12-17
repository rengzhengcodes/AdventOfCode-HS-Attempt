from copy import deepcopy

def setup(file, hashmap):
	raw_input = [list(line.strip()) for line in open(file).readlines()]

	for y in range(len(raw_input)):
		for x in range(len(raw_input[0])):
			voxel_position = (x, y, 0)
			if raw_input[y][x] == "#":
				hashmap[voxel_position] = True
			else:
				hashmap[voxel_position] = False

def border_voxels_fill(state):
	adjacency_offsets = [
	(-1, 1, 1), (0, 1, 1), (1, 1, 1),
	(-1, 0, 1), (0, 0, 1), (1, 0, 1),
	(-1,-1, 1), (0,-1, 1), (1,-1, 1),

	(-1, 1, 0), (0, 1, 0), (1, 1, 0),
	(-1, 0, 0), (0, 0, 0), (1, 0, 0),
	(-1,-1, 0), (0,-1, 0), (1,-1, 0),

	(-1, 1,-1), (0, 1,-1), (1, 1,-1),
	(-1, 0,-1), (0, 0,-1), (1, 0,-1),
	(-1,-1,-1), (0,-1,-1), (1,-1,-1),
	]
	current_voxels = list(state.keys())
	for voxel_position in current_voxels:
		for offset in adjacency_offsets:
			x,y,z = voxel_position
			x_off, y_off, z_off = offset
			adjacent_position = (x+x_off, y+y_off, z+z_off)

			if adjacent_position not in current_voxels:
				state[adjacent_position] = False

def state_change(states):
	adjacency_offsets = [
	(-1, 1, 1), (0, 1, 1), (1, 1, 1),
	(-1, 0, 1), (0, 0, 1), (1, 0, 1),
	(-1,-1, 1), (0,-1, 1), (1,-1, 1),

	(-1, 1, 0), (0, 1, 0), (1, 1, 0),
	(-1, 0, 0), 		   (1, 0, 0),
	(-1,-1, 0), (0,-1, 0), (1,-1, 0),

	(-1, 1,-1), (0, 1,-1), (1, 1,-1),
	(-1, 0,-1), (0, 0,-1), (1, 0,-1),
	(-1,-1,-1), (0,-1,-1), (1,-1,-1),
	]

	current_states = states.copy()
	for voxel_position in states.keys():
		adjacents = 0
		for offset in adjacency_offsets:
			x,y,z = voxel_position
			x_off, y_off, z_off = offset
			adjacent_position = (x+x_off, y+y_off, z+z_off)

			if adjacent_position in states.keys():
				if current_states[adjacent_position]:
					adjacents += 1

		if current_states[voxel_position]:
			if adjacents == 2 or adjacents == 3:
				states[voxel_position] = True
			else:
				states[voxel_position] = False
		else:
			if adjacents == 3:
				states[voxel_position] = True

def part1():
	voxel_states = dict()
	setup("input.txt", voxel_states)
	for i in range(6):
		border_voxels_fill(voxel_states)
		state_change(voxel_states)
	print(list(voxel_states.values()).count(True))

part1()

def setup_4D(file, hashmap):
	raw_input = [list(line.strip()) for line in open(file).readlines()]

	for y in range(len(raw_input)):
		for x in range(len(raw_input[0])):
			voxel_position = (x, y, 0, 0)
			if raw_input[y][x] == "#":
				hashmap[voxel_position] = True
			else:
				hashmap[voxel_position] = False

def state_change_4D(states):
	adjacency_offsets = [
	(-1, 1, 1,-1), (0, 1, 1,-1), (1, 1, 1,-1),	(-1, 1, 1, 0), (0, 1, 1, 0), (1, 1, 1, 0),	(-1, 1, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1),
	(-1, 0, 1,-1), (0, 0, 1,-1), (1, 0, 1,-1),	(-1, 0, 1, 0), (0, 0, 1, 0), (1, 0, 1, 0),	(-1, 0, 1, 1), (0, 0, 1, 1), (1, 0, 1, 1),
	(-1,-1, 1,-1), (0,-1, 1,-1), (1,-1, 1,-1),	(-1,-1, 1, 0), (0,-1, 1, 0), (1,-1, 1, 0),	(-1,-1, 1, 1), (0,-1, 1, 1), (1,-1, 1, 1),

	(-1, 1, 0,-1), (0, 1, 0,-1), (1, 1, 0,-1),	(-1, 1, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0),	(-1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1),
	(-1, 0, 0,-1), (0, 0, 0,-1), (1, 0, 0,-1),	(-1, 0, 0, 0), 				 (1, 0, 0, 0),	(-1, 0, 0, 1), (0, 0, 0, 1), (1, 0, 0, 1),
	(-1,-1, 0,-1), (0,-1, 0,-1), (1,-1, 0,-1),	(-1,-1, 0, 0), (0,-1, 0, 0), (1,-1, 0, 0),	(-1,-1, 0, 1), (0,-1, 0, 1), (1,-1, 0, 1),

	(-1, 1,-1,-1), (0, 1,-1,-1), (1, 1,-1,-1),	(-1, 1,-1, 0), (0, 1,-1, 0), (1, 1,-1, 0),	(-1,-1, 0, 1), (0,-1, 0, 1), (1,-1, 0, 1),
	(-1, 0,-1,-1), (0, 0,-1,-1), (1, 0,-1,-1),	(-1, 0,-1, 0), (0, 0,-1, 0), (1, 0,-1, 0),	(-1,-1, 0, 1), (0,-1, 0, 1), (1,-1, 0, 1),
	(-1,-1,-1,-1), (0,-1,-1,-1), (1,-1,-1,-1),	(-1,-1,-1, 0), (0,-1,-1, 0), (1,-1,-1, 0),	(-1,-1, 0, 1), (0,-1, 0, 1), (1,-1, 0, 1),
	]

	current_states = states.copy()
	for voxel_position in current_states.keys():
		adjacents = 0
		x,y,z,w = voxel_position
		for offset in adjacency_offsets:
			x_off, y_off, z_off, w_off = offset
			adjacent_position = (x+x_off, y+y_off, z+z_off, w+w_off)

			if adjacent_position in current_states.keys():
				if current_states[adjacent_position]:
					adjacents += 1
			else:
				nu_adjacents = 0
				for offset1 in adjacency_offsets:
					x1,y1,z1,w1 = adjacent_position
					x1_off, y1_off, z1_off, w1_off = offset1
					adjacent1_position = (x1+x1_off, y1+y1_off, z1+z1_off, w1+w1_off)

					if adjacent1_position in current_states.keys():
						if current_states[adjacent1_position]:
							nu_adjacents += 1
				if nu_adjacents == 3:
					states[adjacent_position] = True
		if current_states[voxel_position]:
			if adjacents == 2 or adjacents == 3:
				states[voxel_position] = True
			else:
				states[voxel_position] = False
		else:
			if adjacents == 3:
				states[voxel_position] = True

def part2():
	voxel_states = dict()
	setup_4D("input.txt", voxel_states)
	for i in range(6):
		state_change_4D(voxel_states)
	print(list(voxel_states.values()).count(True))

part2()
