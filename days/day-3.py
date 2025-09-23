with open('./inputs/day-3.txt') as file:
    lines = [line.strip() for line in file]

def solve_day_three_part_one():
    r = 3
    d = 1
    x, y = 0, 0
    count = 0

    while(True):
        if lines[y][x % len(lines[0])] == '#':
            count += 1
        x += r
        y += d

        if y >= len(lines):
            break
    
    print(count)

solve_day_three_part_one()