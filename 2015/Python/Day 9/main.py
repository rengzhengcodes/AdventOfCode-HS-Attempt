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

	paths = dict() # path & its corresponding weights
	def find_weight(path: list, map: dict):
		weight = 0

		for i in range(1, len(path)):
			weight += map[path[i-1]][path[i]]

		return weight

	def find_paths(map: dict, current_path: list, available_cities: list) -> list: #returns 2d list of paths
		if len(available_cities) == 1:
			current_path.append(available_cities[0])
			paths[tuple(current_path)] = find_weight(current_path, map)
		else:
			for i in range(len(available_cities)):
				new_path = current_path.copy()
				new_path.append(available_cities[i])

				new_available = available_cities.copy()
				new_available.pop(i)

				find_paths(map, new_path, new_available)

	find_paths(path_weights, list(), list(path_weights.keys()))
	clipboard(min(paths.values()))

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

	paths = dict() # path & its corresponding weights
	def find_weight(path: list, map: dict):
		weight = 0

		for i in range(1, len(path)):
			weight += map[path[i-1]][path[i]]

		return weight

	def find_paths(map: dict, current_path: list, available_cities: list) -> list: #returns 2d list of paths
		if len(available_cities) == 1:
			current_path.append(available_cities[0])
			paths[tuple(current_path)] = find_weight(current_path, map)
		else:
			for i in range(len(available_cities)):
				new_path = current_path.copy()
				new_path.append(available_cities[i])

				new_available = available_cities.copy()
				new_available.pop(i)

				find_paths(map, new_path, new_available)

	find_paths(path_weights, list(), list(path_weights.keys()))
	clipboard(min(paths.values()))

def pt2():
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

	paths = dict() # path & its corresponding weights
	def find_weight(path: list, map: dict):
		weight = 0

		for i in range(1, len(path)):
			weight += map[path[i-1]][path[i]]

		return weight

	def find_paths(map: dict, current_path: list, available_cities: list) -> list: #returns 2d list of paths
		if len(available_cities) == 1:
			current_path.append(available_cities[0])
			paths[tuple(current_path)] = find_weight(current_path, map)
		else:
			for i in range(len(available_cities)):
				new_path = current_path.copy()
				new_path.append(available_cities[i])

				new_available = available_cities.copy()
				new_available.pop(i)

				find_paths(map, new_path, new_available)

	find_paths(path_weights, list(), list(path_weights.keys()))
	clipboard(max(paths.values()))

pt2()
