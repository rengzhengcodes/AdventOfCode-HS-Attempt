import requests
import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import session_id

here = path.dirname(path.abspath(__file__)) + '/'

if not path.exists(here + 'input.txt'):
	#takes input and caches it
	year = 2015
	day = 1
	uri = f'http://adventofcode.com/{year}/day/{day}/input'

	response = requests.get(uri, cookies={'session': session_id})

	with open(here + 'input.txt', 'a') as input:
		input.write(response.text)
		input.close()
