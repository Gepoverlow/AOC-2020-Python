with open('./inputs/day-2.txt') as file:
    lines = [line.strip() for line in file]

def solve_day_two_part_one():
    count = 0
    for line in lines:
        letterCount = 0
        policy, letter, password = line.split()

        min, max = policy.split('-')

        for i in range(len(password)):
            if password[i] == letter[0]:
                letterCount = letterCount + 1
        
        if letterCount >= int(min) and letterCount <= int(max):
            count = count + 1
    
    print("result second day part one:", count)
        


solve_day_two_part_one()