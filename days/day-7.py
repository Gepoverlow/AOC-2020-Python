import re

with open('./inputs/day-7.txt') as file:
    lines = [line.strip() for line in file]

def parse_rules():
    bags = {}
    for line in lines:
        outer_color = re.match(r"(.+?) bags contain", line)[1]
        contained = re.findall(r"(\d+?) (.+?) bags?", line)
        bags[outer_color] = contained
    return bags

rules = parse_rules()

def has_shiny_gold(bag_color):
    if bag_color == "shiny gold":
        return True
    return any(has_shiny_gold(inner_color) for _, inner_color in rules[bag_color])


def solve_day_seven_part_one():
    count = sum(1 for color in rules if has_shiny_gold(color))
    print("Part 1:", count - 1)

solve_day_seven_part_one()