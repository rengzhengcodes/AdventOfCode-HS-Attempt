import re
import itertools as it
from copy import deepcopy

instructions = [tuple(line.strip().split(" = ")) for line in open("input.txt").readlines()]
#print(instructions)


mem = dict()
mask = ""
for line in instructions:
	command, value = line
	if "mask" in command:
		value = "'" + value + "'"
		exec(command + " = " + value)
	else:
		binary = bin(int(value))[2:]
		start_index = len(mask) - len(binary)
		binary = "0" * start_index + binary
		binary = list(binary)
		for i in range(len(mask)):
			if mask[i] != "X":
				binary[i] = mask[i]
		value = ""
		for bit in binary:
			value += bit
		value = "'" + value + "'"
		#print(value)
		exec(command + " = " + value)
#print(mem)
for key, value in mem.items():
	mem[key] = int(value, base=2)
print(sum(mem.values()))

mask = ""
mem = dict()

for line in instructions:
	command, value = line
	if "mask" in command:
		value = "'" + value + "'"
		exec(command + " = " + value)
		indices = [span.start() for span in re.finditer("X", mask)]
	else:
		key = re.search("\[(.*?)\]", command).group(1)
		#print(key)
		binary = bin(int(key))[2:]
		start_index = len(mask) - len(binary)
		binary = "0" * start_index + binary
		binary = list(binary)

		for i in range(len(mask)):
			if mask[i] != "0":
				binary[i] = mask[i]

		key = ""
		for bit in binary:
			key += bit

		key = key.replace("X", "0")
		key = int(key, base=2)
		mem[key] = int(value)

		for i in range(len(indices) + 1):
			sets = list(it.combinations(indices, i))
			for set in sets:
				bin_copy = binary.copy()
				for index in set:
					bin_copy[index] = "1"
				key = ""
				for bit in bin_copy:
					key += bit

				key = key.replace("X", "0")
				key = int(key, base=2)
				mem[key] = int(value)

print(mem)
print(sum(mem.values()))
