import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 8)

def pt1():
	with open(here + 'input.txt') as input:
		raw = 0
		escaped = 0

		for line in input:
			line = line.rstrip()
			raw += len(line)
			escaped += len(eval(line))

		clipboard(raw-escaped)

pt1()
