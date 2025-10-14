from itertools import groupby

with open('./inputs/day-6.txt') as file:
    lines = [line.strip() for line in file]

groups = [list(g) for k, g in groupby(lines, key=bool) if k]

def get_group_count(group):
    unique_questions = set()

    for person in group:
        for question in person:
            unique_questions.add(question)

    return len(unique_questions)

def solve_day_six_part_one():
    result = 0

    for group in groups:
        count = get_group_count(group)

        result = result + count

    print('Total count:', result)


solve_day_six_part_one()