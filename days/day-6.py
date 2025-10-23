from itertools import groupby

with open('./inputs/day-6.txt') as file:
    lines = [line.strip() for line in file]

groups = [list(g) for k, g in groupby(lines, key=bool) if k]

def get_group_count_day_one(group):
    unique_questions = set()

    for person in group:
        for question in person:
            unique_questions.add(question)

    return len(unique_questions)

def get_group_count_day_two(group):
    common_questions = set(group[0])

    for person in group[1:]:
        common_questions = common_questions.intersection(set(person))

    return len(common_questions)

def solve_day_six_part_one():
    result = 0

    for group in groups:
        count = get_group_count_day_one(group)

        result = result + count

    print('Total count:', result)

def solve_day_six_part_two():
    result = 0

    for group in groups:
        count = get_group_count_day_two(group)

        result = result + count

    print('Total count:', result)

solve_day_six_part_one()
solve_day_six_part_two()