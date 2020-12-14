from sympy.ntheory.modular import crt
with open('input.txt') as f:
    inputs = [line.rstrip('\n') for line in f]


bus_time_offsets = []
for i, t in enumerate(inputs[1].split(',')):
    if t == 'x':
        continue
    bus_time_offsets.append((int(t), i))

position = 0
increment = bus_time_offsets[0][0]

for bus_time, bus_offset in bus_time_offsets[1:]:
    while True:
        position += increment
        if (position + bus_offset) % bus_time == 0:
            break
    increment = increment * bus_time
print(position)

with open('input.txt') as f:
  _, buses = f.read().splitlines()

moduli = []
residues = []
for i, bus in enumerate(buses.split(',')):
  print(i, bus)
  if bus != 'x':
    bus = int(bus)
    moduli.append(bus)
    residues.append(bus - i)
print(moduli)
print(residues)
print(crt(moduli, residues)[0])
