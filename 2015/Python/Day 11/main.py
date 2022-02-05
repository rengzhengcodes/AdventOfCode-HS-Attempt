import string
import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 11)

def pt1():
	with open(here + 'input.txt') as input:
		#converts alphanumerics to numbers
		pw = input.read().rstrip()

	def increment_pw(password: str) -> str:
		if password[-1] == 'z': # goes in reverse
			return increment_pw(password[0:-1]) + 'a'
		else:
			#print(pw[-1])
			return password[0:-1] + chr(ord(password[-1]) + 1) # ord == ascii of char. + 1 to get to next letter

	def validity_check(pw: str) -> bool:
		invalids = ('i', 'o', 'l')
		# checks for invalid chars
		for invalid in invalids:
			if invalid in pw:
				return False
		# checks for at least two unique doubles that do not overlap
		doubles = 0
		for char in string.ascii_lowercase:
			doubles += pw.count(char * 2)
			if doubles >= 2:
				break
		if doubles < 2:
			return False
		#checks for increments, very naive but cheap to dev cost
		for i in range(3, 27): #remember range is exclusive
			#print(string.ascii_lowercase[i-3:i])
			if string.ascii_lowercase[i-3:i] in pw:
				return True

		return False # failed third validity check if you got here

	while not validity_check(pw):
		pw = increment_pw(pw)

	clipboard(pw)

pt1()
