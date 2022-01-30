from os import path
here = path.dirname(path.abspath(__file__)) + '/'

with open(here + 'session_id.secret', 'r') as sid:
	session_id = sid.read().rstrip()
	sid.close()
