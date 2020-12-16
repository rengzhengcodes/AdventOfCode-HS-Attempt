parts = open("input.txt").read().split("\n\n")
intervals_raw = parts[0]
intervals_raw = list(intervals_raw.split("\n"))
intervals = dict()
for interval in intervals_raw:
	field, valids = interval.split(": ")
	valids = valids.split(" or ")
	valids = [(int(start), int(end)) for start, end in [valid.split("-") for valid in valids]]
	#print(valids)
	intervals[field] = valids
#print(intervals)
my_ticket = tuple([int(field) for field in parts[1].split("\n")[1].split(",")])

taken_tickets = [tuple([int(field) for field in ticket.split(",")]) for ticket in parts[2].split("\n")[1:]]
#print(intervals.values())

def in_a_interval(value, intervals):
	for interval in intervals:
		#print(interval)
		if interval[0] <= value <= interval[1]:#if in intervaltype(interval[0])
			return True
			break
	return False

def in_a_series_of_intervals(value, series):
	validity = False
	for serie in series:
		validity = in_a_interval(value, serie)
		if validity:
			return True
	return False

error_rate = 0
for ticket in taken_tickets:
	for field in ticket:
		if not in_a_series_of_intervals(field, intervals.values()):
			error_rate += field
print(error_rate)

#discarding invalid tickets
valid_tickets = [my_ticket]
for ticket in taken_tickets:
	valid = True
	for field in ticket:
		if not in_a_series_of_intervals(field, intervals.values()):
			valid = False
			break
	if valid:
		valid_tickets.append(ticket)

fields = [[field] for field in valid_tickets[0]]#initial list setup

for ticket in valid_tickets[1:]:
	for i in range(len(ticket)):
		fields[i].append(ticket[i])#processing all fields to 1

my_ticket_fields = dict()

print(fields)

def values_in_interval(vals, section):
	for val in vals:
		if not in_a_interval(val, section):
			return False
	return True

for field, all_intervals in intervals.items():
	for i in range(len(fields)):
		correct_field = values_in_interval(fields[i], all_intervals)
		if correct_field and field not in my_ticket_fields.keys():
			my_ticket_fields[field] = [my_ticket[i]]
			break
		elif correct_field:
			my_ticket_fields[field].append([my_ticket[i]])
			break

print(my_ticket_fields)

#product = 1
#for fields in intervals.keys():
#	if "departure" in fields:
#		product *= my_ticket_fields[fields]
#print(product)
