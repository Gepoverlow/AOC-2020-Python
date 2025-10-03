import re

with open('./inputs/day-4.txt') as file:
    lines = file.read().splitlines()

    passports = []
    current_group = []

    for line in lines:
        if line.strip() == "":
            if current_group:
                passports.append(current_group)
                current_group = []
        else:
            current_group.extend(line.split())
    
    if current_group:
        passports.append(current_group)

def solve_day_four_part_one():
    count = 0
    for passport in passports:
        fields = [field.split(":")[0] for field in passport]
        if len(fields) == 8:
            count = count + 1
        elif (len(fields) == 7 and "cid" not in fields):
            count = count + 1

    print("result fourth day part one:", count)

def valid_field(key, value):
    if key == "byr":
        return value.isdigit() and 1920 <= int(value) <= 2002
    if key == "iyr":
        return value.isdigit() and 2010 <= int(value) <= 2020
    if key == "eyr":
        return value.isdigit() and 2020 <= int(value) <= 2030
    if key == "hgt":
        if value.endswith("cm"):
            return value[:-2].isdigit() and 150 <= int(value[:-2]) <= 193
        if value.endswith("in"):
            return value[:-2].isdigit() and 59 <= int(value[:-2]) <= 76
        return False
    if key == "hcl":
        return re.fullmatch(r"#[0-9a-f]{6}", value) is not None
    if key == "ecl":
        return value in {"amb","blu","brn","gry","grn","hzl","oth"}
    if key == "pid":
        return re.fullmatch(r"\d{9}", value) is not None
    if key == "cid":
        return True
    return False

def solve_day_four_part_two():
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    count = 0

    for passport in passports:
        fields = dict(field.split(":") for field in passport)
        if not required.issubset(fields.keys()):
            continue
        if all(valid_field(k, v) for k, v in fields.items()):
            count += 1

    print("result fourth day part two:", count)

solve_day_four_part_one()
solve_day_four_part_two()