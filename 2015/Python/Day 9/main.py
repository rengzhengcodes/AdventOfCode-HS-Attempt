import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 9)

def pt1():
	path_weights = dict() # dictionary with dictionaries of start and end destinations, end destination keys correlate to weight of path
	with open(here + 'input.txt') as input:
		# establishes paths
		for line in input:
			line = line.rstrip()
			parts = line.split()
			city1 = parts[0]
			city2 = parts[2]
			distance = int(parts[4])

			if city1 not in path_weights.keys():
				path_weights[city1] = dict()
			if city2 not in path_weights.keys():
				path_weights[city2] = dict()

			path_weights[city1][city2] = distance
			path_weights[city2][city1] = distance

	print(path_weights)

pt1()
