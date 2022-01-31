import string
import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 5)

def pt1():
	vowels = 'aeiou'
	alphabet = string.ascii_lowercase
	forbidden = ['ab', 'cd', 'pq', 'xy']

	with open(here + 'input.txt') as input:
		nice_strings = 0
		for line in input:
			# checks number of vowels
			num_vowels = 0
			for char in vowels:
				num_vowels += line.count(char)
				if num_vowels >= 3:
					break
			# checks for double letters
			double_letters = False
			for char in alphabet:
				if char * 2 in line:
					double_letters = True
					break
			# checks for forbidden strings
			has_forbidden = False
			for item in forbidden:
				if item in line:
					has_forbidden = True
					break
			# checks for niceity
			if num_vowels >= 3 and double_letters and not has_forbidden:
				nice_strings += 1

	clipboard(nice_strings)

def pt2():
	with open(here + 'input.txt') as input:
		nice_strings = 0
		
