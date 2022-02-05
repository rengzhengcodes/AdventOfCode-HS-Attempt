import sys
from itertools import groupby
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 10)

def pt1():
	with open(here + 'input.txt') as input:
		string = input.read().rstrip()

	count = 40
	for i in range(40):
		count_of_groups = groupby(string)
		count_of_groups = [(label, sum(1 for element in group)) for label, group in count_of_groups] #https://stackoverflow.com/questions/34443946/count-consecutive-characters
		# print(string)
		# print(count_of_groups)
		string = ''
		for char, amount in count_of_groups:
			string += str(amount) + char

	clipboard(len(string))

pt1()
