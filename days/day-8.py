with open('./inputs/day-8.txt') as file:
    lines = [line.strip() for line in file]

program = []
for line in lines:
    operation, value = line.split()
    program.append((operation, int(value)))


def execute(instructions):
    accumulator = 0
    pointer = 0
    visited_pointers = set()

    while True:
        if pointer in visited_pointers:
            return accumulator, False
        
        if pointer == len(instructions):
            return accumulator, True
        
        if pointer < 0:
            return accumulator, False

        visited_pointers.add(pointer)
        operation, value = instructions[pointer]

        if operation == "acc":
            accumulator += value
            pointer += 1
        elif operation == "jmp":
            pointer += value
        else:
            pointer += 1


def solve_day_eight_part_one():
    accumulator, _ = execute(program)
    print("Part 1:", accumulator)

solve_day_eight_part_one()