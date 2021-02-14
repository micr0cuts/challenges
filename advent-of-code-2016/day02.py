instructions = [line.strip() for line in open('input02.txt', encoding='utf8').readlines()]

TOY = ["ULL", "RRDDD", "LURDL", "UUUUD"]

def update_num(num, char):
    if char == 'U':
        if num > 3:
            num -= 3
    elif char == 'D':
        if num < 7:
            num += 3
    elif char == 'L':
        if num not in [1, 4, 7]:
            num -= 1
    elif char == 'R':
        if num not in [3, 6, 9]:
            num += 1
    return num

def part1(instructions):
    combination = []
    button = 5
    for instr in instructions:
        for char in instr:
            button = update_num(button, char)
        combination.append(button)
    return ''.join(map(str, combination))

assert part1(TOY) == "1985", part1(TOY)
print("The solution to part 1 is:", part1(instructions))

KEYPAD = [[0,0,1,0,0], [0,2,3,4,0], [5,6,7,8,9], [0,'A','B','C',0], [0,0,'D',0,0]]

def update_num_part2(button, char):
    x, y = button
    if char == 'U':
        if x > 0:
            x -=1
    elif char == 'D':
        if x != len(KEYPAD)-1:
            x += 1
    elif char == 'L':
        if y > 0:
            y -= 1
    elif char == 'R':
        if y != len(KEYPAD[0])-1:
            y += 1
    if KEYPAD[x][y] == 0:
        return button
    return (x,y)

def part2(instructions):
    combination = []
    button = (2,0)
    for instr in instructions:
        for char in instr:
            button = update_num_part2(button, char)
            x, y = button
        combination.append(KEYPAD[x][y])
    return ''.join(map(str, combination))

assert part2(TOY) == "5DB3", part2(TOY)
print("The solution to part 2 is:", part2(instructions))
