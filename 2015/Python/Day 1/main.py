import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 1)

def pt1():
	with open(here + 'input.txt', 'r') as input:
		input = input.read().rstrip()
		floor = 0

		for char in input:
			if char == '(':
				floor += 1
			else:
				floor -= 1

		clipboard(floor)

def pt2():
	with open(here + 'input.txt', 'r') as input:
		input = input.read().rstrip()
		floor = 0
		instruction = 0

		while floor >= 0:
			char = input[instruction]
			instruction += 1
			if char == '(':
				floor += 1
			else:
				floor -= 1

		clipboard(instruction)

if __name__ == '__main__':
	pt2()
