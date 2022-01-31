import re
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
		for line in input:
			# finds non-overlapping repetitions
			has_double = False # checks if it has two non-overlapping instances of 2 chars.
			for char1 in string.ascii_lowercase:
				for char2 in string.ascii_lowercase:
					segment = char1 + char2 # generates all 26^2 combinations of letter sto be repeated.
					# print(segment)
					if len(re.findall(segment, line)) >= 2: #findall is already non overlapping
						has_double = True
						break
				if has_double:
					break
			# finds instance of a character + any character + first character in a string, if it exists.
			# print(line)
			has_x_x = False
			for char in string.ascii_lowercase:
				if re.search(f'{char}.{char}', line) is not None:
					has_x_x = True
					break
			# nicety check
			# print(has_x_x, has_double)
			if has_x_x and has_double:
				nice_strings += 1
	clipboard(nice_strings)

pt2()
