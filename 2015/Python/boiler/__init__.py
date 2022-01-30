import requests
from os import path
here = path.dirname(path.abspath(__file__)) + '/'
# gets session id
with open(here + 'session_id.secret', 'r') as sid:
	session_id = sid.read().rstrip()
	sid.close()
# method for imports
def get_input(here:str, year:int, day:int):
	global session_id

	if not path.exists(here + 'input.txt'):
		#takes input and caches it
		year = year
		day = day
		uri = f'http://adventofcode.com/{year}/day/{day}/input'

		response = requests.get(uri, cookies={'session': session_id})

		with open(here + 'input.txt', 'a') as input:
			input.write(response.text)
			input.close()

		print('Copied input')
# copies stuff to clipboard
import pyperclip
def clipboard(input:str):
	pyperclip.copy(input)
