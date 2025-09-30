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

    print(count)

solve_day_four_part_one()