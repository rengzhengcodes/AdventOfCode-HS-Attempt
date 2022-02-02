import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 6)

def pt1():
	#generates light grid
	grid = list()
	for i in range(1000):
		grid.append(list())
		for j in range(1000):
			grid[i].append(False)

	#print(grid)

	with open(here + 'input.txt') as input:
		for line in input:
			#gets individual words
			words = line.split()
			#extracts start coordinates
			start = words[-3].split(',')
			start = [int(x) for x in start]
			start = tuple(start)
			# print(start)
			#extracts end coordinates
			end = words[-1].split(',')
			end = [int(x) for x in end]
			end = tuple(end)
			# print(end)

			if words[0] == 'toggle':
				for i in range(start[0], end[0] + 1):
					for j in range(start[1], end[1] + 1):
						grid[i][j] = not grid[i][j]
			else: # words[0] is turn
				if words[1] == 'on':
					for i in range(start[0], end[0] + 1):
						for j in range(start[1], end[1] + 1):
							grid[i][j] = True
				else: #words[1] is off
					for i in range(start[0], end[0] + 1):
						for j in range(start[1], end[1] + 1):
							grid[i][j] = False
	#gets number of lights on
	on_count = 0
	for i in range(1000):
		for j in range(1000):
			if grid[i][j]:
				on_count += 1

	clipboard(on_count)

pt1()
