import math

data = list()
passports = list()
with open("input.txt") as f:
    data = str(f.read()).split("\n\n")
    for line in data:
        passport_dictionary = dict()
        line = line.replace("\n"," ")
        attributes = line.split(" ")
        for attribute in attributes:
            key, value = attribute.split(":")
            passport_dictionary[key] = value
        passports.append(passport_dictionary)
        

attributes = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

answer = 0
answer1 = 0

def valid_year(year, mini, maxi):
    y = int(year)
    if len(year) == 4 and mini <= y <= maxi:
        return True
    
for passport in passports:
    valid = True
    for attribute in attributes:
        if not attribute in passport.keys():
            valid = False
    if valid:
        answer += 1
        ## valid years test
        if not valid_year(passport["byr"], 1920, 2002):
            valid = False
        elif not valid_year(passport["iyr"], 2010, 2020):
            valid = False
        elif not valid_year(passport["eyr"], 2020, 2030):
            valid = False

        if passport["hgt"].endswith("cm"):
            hgt = int(passport["hgt"][0:-2])
            if not (150 <= hgt <= 193):
                valid = False
        elif passport["hgt"].endswith("in"):
            hgt = int(passport["hgt"][0:-2])
            if not (59 <= hgt <= 76):
                valid = False
        else:
            valid = False

        if passport["hcl"].startswith("#") and len(passport["hcl"]) == 7:
            try:
                int(passport["hcl"][1::], 16)
            except ValueError:
                valid = False
        else:
            valid = False

        if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            valid = False

        try:
            pid = int(passport["pid"])
            if len(passport["pid"]) != 9:
                valid = False
        except ValueError:
            valid = False
    
    if valid:
        answer1 += 1

print(answer)
print(answer1)

