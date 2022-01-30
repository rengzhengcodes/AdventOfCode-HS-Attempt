import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 4)

def pt1():
	with open(here + 'input.txt') as input:
		from hashlib import md5
		pw = input.read().rstrip()
		number = 1
		hash = md5((pw + str(number)).encode()).hexdigest()

		while str(hash)[0:5] != '00000':
			number += 1
			hash = md5((pw + str(number)).encode()).hexdigest()
			#print(hash)

		clipboard(number)

def pt2():
	with open(here + 'input.txt') as input:
		from hashlib import md5
		pw = input.read().rstrip()
		number = 1
		hash = md5((pw + str(number)).encode()).hexdigest()

		while str(hash)[0:6] != '0'*6:
			number += 1
			hash = md5((pw + str(number)).encode()).hexdigest()
			#print(hash)

		clipboard(number)
pt2()
