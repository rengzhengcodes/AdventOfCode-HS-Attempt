import sys
from os import path
# adds repo of boiler
boiler_parent = path.dirname(path.dirname(path.abspath(__file__)))
print(boiler_parent)
sys.path.append(boiler_parent)
from boiler import *

here = path.dirname(path.abspath(__file__)) + '/'

get_input(here, 2015, 7)

def pt1():
	# wires = {wire: instruction}
	wires = dict()

	with open(here + 'input.txt') as input:
		for line in input:
			line = line.rstrip() # cleans off the newlines
			# wires to their text literals
			components = line.split(' -> ')
			wires[components[-1]] = components[0]
		# sets literal strings
		for key, value in wires.items():
			if value.isnumeric(): # checks if the wire just gets a straight up input
				wires[key] = int(value)

		# print(wires)

	def check_wire_load(wire: str) -> None:
		# checks wire has binary value, if not, sets it
		if wire.isnumeric():
			wires[wire] = int(wire) # cheap and dirty solution to avoid having to deal with actual numerics in wires during AND and OR operations
		elif isinstance(wires[wire], str):
			wires[wire] = calculate_load(wire)

	def rshift(instructions: str) -> int:
		wire, value = instructions.split(' RSHIFT ')
		value = int(value)
		check_wire_load(wire)
		return wires[wire] >> value

	def lshift(instructions: str) -> int:
		wire, value = instructions.split(' LSHIFT ')
		value = int(value)
		check_wire_load(wire)
		return wires[wire] << value

	def AND(instructions: str) -> int:
		wire1, wire2 = instructions.split(' AND ')
		check_wire_load(wire1)
		check_wire_load(wire2)
		return wires[wire1] & wires[wire2]

	def OR(instructions: str) -> int:
		wire1, wire2 = instructions.split(' OR ')
		check_wire_load(wire1)
		check_wire_load(wire2)
		return wires[wire1] | wires[wire2]

	def NOT(instructions: str) -> int:
		wire = instructions[4::]
		check_wire_load(wire)
		complement = ~wires[wire]
		complement = format(complement, 'b')[1::] #cheap trick to get rid of - sign
		complement = '1'*(16 - len(complement)) + complement # puts not into 16 bit format
		return int(complement, 2)

	def calculate_load(wire:str) -> str:
		if isinstance(wires[wire], bytes):
			return wires[wire]
		elif 'RSHIFT' in wires[wire]:
			return rshift(wires[wire])
		elif 'LSHIFT' in wires[wire]:
			return lshift(wires[wire])
		elif 'AND' in wires[wire]:
			return AND(wires[wire])
		elif 'OR' in wires[wire]:
			return OR(wires[wire])
		elif 'NOT' in wires[wire]:
			return NOT(wires[wire])
		elif wires[wire] in wires.keys():
			return calculate_load(wires[wire])
		else:
			raise Exception('Bad input: ' + wire)

	return calculate_load('a')

def pt2():
	# wires = {wire: instruction}
	wires = dict()

	with open(here + 'input.txt') as input:
		for line in input:
			line = line.rstrip() # cleans off the newlines
			# wires to their text literals
			components = line.split(' -> ')
			wires[components[-1]] = components[0]
		# sets literal strings
		for key, value in wires.items():
			if value.isnumeric(): # checks if the wire just gets a straight up input
				wires[key] = int(value)

		wires['b'] = pt1() #override

	def check_wire_load(wire: str) -> None:
		# checks wire has binary value, if not, sets it
		if wire.isnumeric():
			wires[wire] = int(wire) # cheap and dirty solution to avoid having to deal with actual numerics in wires during AND and OR operations
		elif isinstance(wires[wire], str):
			wires[wire] = calculate_load(wire)

	def rshift(instructions: str) -> int:
		wire, value = instructions.split(' RSHIFT ')
		value = int(value)
		check_wire_load(wire)
		return wires[wire] >> value

	def lshift(instructions: str) -> int:
		wire, value = instructions.split(' LSHIFT ')
		value = int(value)
		check_wire_load(wire)
		return wires[wire] << value

	def AND(instructions: str) -> int:
		wire1, wire2 = instructions.split(' AND ')
		check_wire_load(wire1)
		check_wire_load(wire2)
		return wires[wire1] & wires[wire2]

	def OR(instructions: str) -> int:
		wire1, wire2 = instructions.split(' OR ')
		check_wire_load(wire1)
		check_wire_load(wire2)
		return wires[wire1] | wires[wire2]

	def NOT(instructions: str) -> int:
		wire = instructions[4::]
		check_wire_load(wire)
		complement = ~wires[wire]
		complement = format(complement, 'b')[1::] #cheap trick to get rid of - sign
		complement = '1'*(16 - len(complement)) + complement # puts not into 16 bit format
		return int(complement, 2)

	def calculate_load(wire:str) -> str:
		if isinstance(wires[wire], bytes):
			return wires[wire]
		elif 'RSHIFT' in wires[wire]:
			return rshift(wires[wire])
		elif 'LSHIFT' in wires[wire]:
			return lshift(wires[wire])
		elif 'AND' in wires[wire]:
			return AND(wires[wire])
		elif 'OR' in wires[wire]:
			return OR(wires[wire])
		elif 'NOT' in wires[wire]:
			return NOT(wires[wire])
		elif wires[wire] in wires.keys():
			return calculate_load(wires[wire])
		else:
			raise Exception('Bad input: ' + wire)

	return calculate_load('a')

clipboard(pt2())
