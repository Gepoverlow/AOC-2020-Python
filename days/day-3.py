import math

with open('./inputs/day-3.txt') as file:
    lines = [line.strip() for line in file]

def solve_day_three_part_one(r, d):
    x, y = 0, 0
    count = 0

    while(True):
        if lines[y][x % len(lines[0])] == '#':
            count += 1
        x += r
        y += d

        if y >= len(lines):
            break
    
    return count

def solve_day_three_part_two():
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    tree_counts = [solve_day_three_part_one(r, d) for r, d in slopes]
    result = math.prod(tree_counts)

    print("result third day part two:", result)


print("result third day part one:", solve_day_three_part_one(3, 1))
solve_day_three_part_two()