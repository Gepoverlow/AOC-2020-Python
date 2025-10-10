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
    
def get_seat_id(line, total_rows=127, total_columns=7):
    row = binary_partition(line[:7], 0, total_rows, 'F', 'B')
    column = binary_partition(line[7:], 0, total_columns, 'L', 'R')
    return row * 8 + column

def solve_day_five_part_one():
    highest_id = 0

    for line in lines:
        seat_id = get_seat_id(line)
        if seat_id > highest_id:
            highest_id = seat_id

    print('Highest seat ID:', highest_id)

def solve_day_five_part_two():
    seat_ids = []

    for line in lines:
        seat_ids.append(get_seat_id(line))

    seat_ids.sort()

    my_seat = None
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] != seat_ids[i] + 1:
            my_seat = seat_ids[i] + 1
            break

    print('My seat ID:', my_seat)

solve_day_five_part_one()
solve_day_five_part_two()