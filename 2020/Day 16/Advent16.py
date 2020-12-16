parts = open("input.txt").read().split("\n\n")
ranges_raw = parts[0]
ranges_raw = list(ranges_raw.split("\n"))
ranges = dict()
for range in ranges_raw:
	field, valids = range.split(": ")
	valids = valids.split(" or ")
	valids = [(int(start), int(end)) for start, end in [valid.split("-") for valid in valids]]
	#print(valids)
	ranges[field] = valids
#print(ranges)
my_ticket = tuple([int(field) for field in parts[1].split("\n")[1].split(",")])

taken_tickets = [tuple([int(field) for field in ticket.split(",")]) for ticket in parts[2].split("\n")[1:]]
#print(ranges.values())

def in_a_range(value, ranges):
	for range in ranges:
		#print(range)
		if range[0] <= field <= range[1]:#if in range
			return True
			break
	return False

error_rate = 0
for ticket in taken_tickets:
	for field in ticket:
		for all_ranges in ranges.values():
			broken = not in_a_range(field, all_ranges)
			if not broken:
				break
		if broken:
			error_rate += field
print(error_rate)

#discardubg ubvakuds
valid_tickets = [my_ticket]
for ticket in taken_tickets:
	for field in ticket:
		broken = True
		for all_ranges in ranges.values():
			for range in all_ranges:
				#print(range)
				if range[0] <= field <= range[1]:
					broken = False
					break
			if not broken:#if its valid for a field, it passes, no need to check others for validity.
				break
		if broken:#if the ticket is already broken, no need to check rest, invalid value
			break
		else:
			valid_tickets.append(ticket)

for field, all_ranges in ranges.items():
	pass
##	for ticket in tickets:
##		for field in ticket:
##			broken = True
##			for range in all_ranges:
##				if range[0] <= field <= range[1]
