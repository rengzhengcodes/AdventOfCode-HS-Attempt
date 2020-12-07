import math

with open("input.txt") as f:
    passes = list(f.read().split("\n"))

def bisection(top_half, bottom_half, inp):
    r = list(range(2 ** len(inp)))
    for char in inp:
        if char == bottom_half:
            del r[int(len(r)/2)::]
        elif char == top_half:
            del r[0:int(len(r)/2)]
    if len(r) != 1:
        print(r)
    return r[0]


highest_id = 0;
for p in passes:
    row = p[0:7]
    column = p[7:]
    
    row = bisection("B", "F", row)
    column = bisection("R", "L", column)

    pid = row * 8 + column
    if (pid > highest_id):
        highest_id = pid

print(highest_id)

ids = list()
for p in passes:
    row = p[0:7]
    column = p[7:]
    
    row = bisection("B", "F", row)
    column = bisection("R", "L", column)

    ids += [row * 8 + column]

ids.sort()
for i in range(1, len(ids)):
    if ids[i] - 2 == ids[i - 1]:
         print(ids[i] -1)
         break
