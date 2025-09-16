with open('day-1-input.txt') as file:
    numbers = [int(line.strip()) for line in file]

target_sum = 2020

def solve_first_day_part_one():
    for index_1 in range(len(numbers)):
        for index_2 in range(index_1 + 1, len(numbers)):
            number_1 = numbers[index_1]
            number_2 = numbers[index_2]

            if number_1 + number_2 == target_sum:
                print("result first day part one:", number_1 * number_2)
                break

def solve_first_day_part_two():
    for index_1 in range(len(numbers)):
        for index_2 in range(index_1 + 1, len(numbers)):
            for index_3 in range(index_2 + 1, len(numbers)):
                number_1 = numbers[index_1]
                number_2 = numbers[index_2]
                number_3 = numbers[index_3]

                if number_1 + number_2 + number_3 == target_sum:
                    print("result first day part two:", number_1 * number_2 * number_3)
                    break

solve_first_day_part_one()
solve_first_day_part_two()