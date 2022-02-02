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
	with open(here + 'input.txt') as input:
		for line in input:
			words = line.split()
			if words[0] is 'toggle':
			else: # words[0] is turn
