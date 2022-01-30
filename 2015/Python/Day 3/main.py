import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 3)

def pt1():
	with open(here + 'input.txt') as input:
		#houses represented as xy tuples
		houses = []

		x = 0
		y = 0

		for char in input.read():
			if char == '^':
				y += 1
			elif char == 'v':
				y -= 1
			elif char == '>':
				x += 1
			else:
				x -= 1

			coord = (x, y)
			if coord not in houses:
				houses.append(coord)

		clipboard(len(houses))

def pt2():
	with open(here + 'input.txt') as input:
		#houses represented as xy tuples
		houses = []

		santa = [0, 0]
		robo = [0, 0]
		current_mover = santa

		order = 0
		for char in input.read():
			if char == '^':
				current_mover[0] += 1
			elif char == 'v':
				current_mover[0] -= 1
			elif char == '>':
				current_mover[1] += 1
			else:
				current_mover[1] -= 1

			coord = tuple(current_mover)
			if coord not in houses:
				houses.append(coord)

			#swaps who's currently moving
			if current_mover is santa:
				current_mover = robo
			else:
				current_mover = santa

		clipboard(len(houses))

pt2()
