with open('./inputs/day-5.txt') as file:
    lines = [line.strip() for line in file]

def binary_partition(boarding_code, low, high, lower_char, upper_char):
    if not boarding_code:
        return low
    
    mid = (low + high) // 2
    boarding_letter = boarding_code[0]

    if(boarding_letter == lower_char):
        return binary_partition(boarding_code[1:], low, mid, lower_char, upper_char)

    if(boarding_letter == upper_char):
        return binary_partition(boarding_code[1:], mid + 1, high, lower_char, upper_char)

def solve_day_five_part_one():
    total_rows = 127
    total_columns = 7
    highest_id = 0

    for line in lines:
        row = binary_partition(line[0:7], 0, total_rows, 'F', 'B')
        column = binary_partition(line[7:10], 0, total_columns, 'L', 'R')
        seat_id = (row * 8 + column)
        if seat_id > highest_id:
            highest_id = seat_id

    print('Highest seat id:', highest_id)

solve_day_five_part_one()