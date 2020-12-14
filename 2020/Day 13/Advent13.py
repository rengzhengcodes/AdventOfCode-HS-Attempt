import time
import math
from sympy.ntheory.modular import crt

earliest_time = int(open("input.txt").readlines()[0])
buses = list(open("input.txt").readlines()[1].split(","))

while "x" in buses:
	buses.pop(buses.index("x"))

buses = [int(bus) for bus in buses]

lowest_delta = 2 ** 8
take = 0
for bus in buses:
	leave = bus
	while leave < earliest_time:
		leave += bus
	if leave-earliest_time < lowest_delta:
		lowest_delta = leave-earliest_time
		take = bus

print(lowest_delta * take)

buses = list(open("input.txt").readlines()[1].split(","))
offsets = {}
x = 0
for bus in buses:
	if bus != "x":
		offsets[int(bus)] = int(bus) - buses.index(bus)

position = buses[0]
while "x" in buses:
	buses.pop(buses.index("x"))

buses = [int(bus) for bus in buses]
print(offsets)
print(crt(offsets.keys(), offsets.values())[0])
#position = buses[0]
#increment = position
#while True:
#	for bus in buses:
#		if (position + offsets[bus]) % bus == 0:
#			buses.pop(buses.index(bus))
#			increment = position
#			break
#	#print(position)
#	if len(buses) == 0:
#		break
#	##print(position)
#	position += increment
#print(position)
