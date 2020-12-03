ok = 0;
with open("input.txt") as f:
    for line in f:
        params = line.rstrip("\n").split(" ")
        params[1] = params[1].rstrip(":")
        range_req = params[0].split("-")
        for i in range(len(range_req)):
            range_req[i] = int(range_req[i]) 
        if range_req[0] <= params[2].count(params[1]) <= range_req[1]:
            ok += 1
print(ok)
ok1 = 0
with open("input.txt") as f:
    for line in f:
        params = line.rstrip("\n").split(" ")
        params[1] = params[1].rstrip(":")
        range_req = params[0].split("-")
        for i in range(len(range_req)):
            range_req[i] = int(range_req[i]) - 1 
        if (params[2][range_req[0]] == params[1]) ^ (params[2][range_req[1]] == params[1]):
            ok1 += 1
print(ok1)
