forest = list();
with open("input.txt") as f:
    for line in f:
        forest.append(line.rstrip("\n"))

rows = len(forest)
columns = len(forest[0])

xcord = 0
trees = 0

for i in range(rows):
    if forest[i][xcord % columns] == "#":
        trees += 1
    xcord += 3;

print(trees)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

trees = 1
for slope in slopes:
    xcord = 0
    trees_slope = 0

    for i in range(0, rows, slope[1]):
        if forest[i][xcord % columns] == "#":
            trees_slope += 1
        xcord += slope[0]
    ##print(trees_slope)

    trees *= trees_slope

print(trees)
