instructions = [line.strip() for line in open('input02.txt', encoding='utf8').readlines()]

KEYPAD = '123456789'
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
    return "".join(map(str,combination))

assert part1(TOY) == "1985", part1(TOY)
print("The solution to part 1 is:", part1(instructions))
