import re

raw_rules = []

with open("input.txt") as f:
	raw_rules = list(f.read().rstrip("\n").split("\n"));

rules_dict = {}

for raw in raw_rules:
	out, contained = raw.split(" contain ")
	out = out.rstrip("s").replace(" bag", "")
	contained = list(contained.rstrip(".").split(", "))
	for i in range(len(contained)):
		num, bag = contained[i].split(" ", 1)
		if "no" in num:
			num = 0
			bag = "END"
		else:
			num = int(num)
		bag = bag.rstrip("s").replace(" bag", "")
		contained[i] = [num, bag]
	rules_dict[out] = contained

shiny_gold_in = 0

def bag_inside(bagsearch, outer, ruleset):
	insides = ruleset[outer]
	bags = []

	for i in range(len(insides)):
		bags.append(insides[i][1])

	if bagsearch in bags:
		return True
	for bag in bags:
		if "END" in bags:
			return False
		elif (bag_inside(bagsearch, bag, ruleset)):
			return True
	return False

for bag in rules_dict.keys():
	if bag_inside("shiny gold", bag, rules_dict):
		shiny_gold_in += 1

print(shiny_gold_in)

def bags_required(outer, ruleset):
	bags = 0

	if outer == "END":
		return bags

	inside = ruleset[outer]
	
	for bag in inside:
		num, adj = bag
		bags += num
		bags += num * bags_required(adj, ruleset)
	return bags

print(bags_required("shiny gold", rules_dict))
