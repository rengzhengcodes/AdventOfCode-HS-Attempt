cypher = []

with open("input.txt") as f:
	f = f.read()
	cypher = list(f.split("\n"))

cypher = [int(element) for element in cypher]

def debug(s):
	if True:
		print(s)
	else:
		pass
debug(cypher)

def equal_last_x(num, last_x):
	last_x.sort()
	i_1 = 0;
	i_2 = len(last_x) - 1;

	while (last_x[i_1] != last_x[i_2]):
		sum = last_x[i_1] + last_x[i_2]
		if sum == num:
			return True;
		elif sum < num:
			i_1 += 1
		elif sum > num:
			i_2 -= 1

	return False

last_n = 25
weakness = 0

for i in range(last_n, len(cypher)):
	num = cypher[i]
	last_25 = cypher[i-last_n : i]
	val = equal_last_x(num, last_25)
	if not val:
		print(num)
		weakness = num
		break


for i in range(cypher.index(weakness)):
	for j in range(i + 2, cypher.index(weakness)):
		previous = cypher[i:j]
		s = sum(previous)
		previous.sort()
		if s == weakness:
			print(previous[0] + previous[-1])

##previous = [cypher[0]]
##for i in range(1, len(cypher)):
##	previous.append(cypher[i])
##	s = sum(previous)
##
##	if (s == weakness):
##		print(previous[0] + previous[-1])
##		break
##	elif s > weakness:
##		while (s > weakness and len(previous) > 1):
##			del previous[0]
