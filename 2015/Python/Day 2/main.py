import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 2)

def pt1():
	with open(here + 'input.txt') as input:
		footage = 0

		for line in input:
			dimensions = line.split('x')
			#face area of prism
			dimensions = [int(x) for x in dimensions]
			face_areas = (dimensions[0] * dimensions[1], dimensions[1] * dimensions[2], dimensions[0] * dimensions[2])

			smallest_face =  min(face_areas)

			footage += 2*sum(face_areas) + smallest_face

		clipboard(footage)

def pt2():
	with open(here + 'input.txt') as input:
		ribbon = 0

		for line in input:
			dimensions = line.split('x')
			#face area of prism
			dimensions = [int(x) for x in dimensions]
			dimensions.sort()

			ribbon += 2*(dimensions[0] + dimensions[1]) + dimensions[0]*dimensions[1]*dimensions[2]

		clipboard(ribbon)
pt2()
