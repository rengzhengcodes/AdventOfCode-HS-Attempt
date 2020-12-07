import re

groups = [];

with open("input.txt") as f:
    groups = list(f.read().split("\n\n"))

for i in range(len(groups)):
    groups[i] = list(groups[i].split("\n"))

group_count = []

for group in groups:
    answers = ""
    group_sum = 0;
    for person in group:
        person_sum = 0;
        for answer in person:
            if answer not in answers:
                person_sum += 1
                answers += answer
        group_sum += person_sum
    group_count.append(group_sum)

sum = 0

for count in group_count:
    sum += count

print (sum)


group_count = []
sum = 0
for group in groups:
    common = set(group[0])
    for person in group:
        common = common.intersection(set(person))

    group_count.append(len(common))
    sum += len(common)

sum = 0

for count in group_count:
    sum += count

print(sum)
