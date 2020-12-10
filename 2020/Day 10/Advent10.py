import re
import itertools
import math

jolts = [0]

with open("input.txt") as f:
	f = f.read().rstrip("\n")
	jolts = itertools.chain(jolts, list(f.split("\n")))

jolts = [int(jolt) for jolt in jolts]
#print(jolts)
max_jolt = max(jolts) + 3
#print(max_jolt)
jolts.sort()
#print(jolts)

diff_1 = 0
diff_3 = 1
previous = jolts[0]
for i in range(1, len(jolts)):
	delta = jolts[i] - jolts[i-1]

	if delta == 1:
		diff_1 += 1
	elif delta == 3:
		diff_3 += 1

	else:
		print(jolts[i-1])
		print(jolts[i])
print(diff_1 * diff_3)

jolts.append(max_jolt)
deltas = itertools.zip_longest(jolts[:-1], jolts[1:])
deltas = [(b-a) for a,b in deltas]
#print(deltas)

combos = 1
##map = {0:1, 1:1, 2:2, 3:4, 4:7, 5:13}
while len(deltas) > 0:
##	combos *= map[deltas.index(3)]
	necessary = max(1, math.floor(deltas.index(3)/3))
	unecessary = deltas.index(3) - necessary
	if unecessary < 0:
		unecessary = 0
	c = 2**unecessary
	if c >= 8:
		c -= necessary
	combos *= c
##	if c != map[deltas.index(3)]:
##		print(c, map[deltas.index(3)])
	del deltas[:deltas.index(3)+1]

print(combos)

deltas = itertools.zip_longest(jolts[:-1], jolts[1:])
deltas = [(b-a) for a,b in deltas]
branches = [1, 1, deltas[:3].count(1)]

for i in range(3, len(jolts)):
	branches.append(branches[i-1])
	if jolts[i] - jolts[i-2] <= 3:
		branches[i] += branches[i-2]
	if jolts[i] - jolts[i-3] <= 3:
		branches[i] += branches[i-3]

print(branches[-1])
