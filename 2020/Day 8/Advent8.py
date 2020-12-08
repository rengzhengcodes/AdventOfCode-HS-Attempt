instructions = []

with open("input.txt") as f:
	f = f.read()
	instructions = list(f.rstrip('\n').split('\n'))
	for i in range(len(instructions)):
		ins, amt = instructions[i].split(" ")
		amt = int(amt)
		instructions[i] = [ins, amt]

def debug(s):
	if False:
		print(s)
	else:
		pass

debug(instructions)

def isInfinite(instructions):
	acc = 0
	line = 0
	prev_lines = []
	while line < len(instructions):
		debug(line)
		if line in prev_lines:
			return True, acc, prev_lines
		else:
			prev_lines.append(line)
		ins, amt = instructions[line]
		debug(line)
		if ins == 'jmp':
			line += amt
		elif ins == 'acc':
			line += 1
			acc += amt
		elif ins == 'nop':
			line += 1
	return False, acc, prev_lines
infinite, acc, prev_lines = isInfinite(instructions)
if infinite:
	print(acc)


for val in prev_lines:
	ins, amt = instructions[val]

	if ins == 'jmp':
		instructions[val] = ['nop', amt]
	elif ins == 'nop':
		instructions[val] = ['nop', amt]


	infinite, acc, x = isInfinite(instructions)
	if infinite:
		instructions[val] = [ins, amt]
		debug(acc)
	else:
		print(acc)
		break
