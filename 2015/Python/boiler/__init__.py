open('session_id.secret', 'r') as sid:
	session_id = sid.read().rstrip()
	sid.close()
