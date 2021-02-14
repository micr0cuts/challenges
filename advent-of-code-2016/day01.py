instructions = []

with open('input01.txt', encoding='utf8') as f:
    for line in f:
        unclean_instr = line.strip().split(',')
        for instruction in unclean_instr:
            instructions.append(instruction.strip())

def part1(instr):
    x, y = 0, 0
    facing = 'N'
    for i in instr:
        turn, n = i[0], int(i[1])
        if turn == 'L':
            if facing == 'N':
                x -= n
                facing = 'W'
            elif facing == 'S':
                x += n
                facing = 'E'
            elif facing == 'W':
                y -= n
                facing = 'S'
            elif facing == 'E':
                y += n
                facing = 'N'
        elif turn == 'R':
            if facing == 'N':
                x += n
                facing = 'E'
            elif facing == 'S':
                x -= n
                facing = 'W'
            elif facing == 'W':
                y += n
                facing = 'N'
            elif facing == 'E':
                y -= n
                facing = 'S'
    return abs(x) + abs(y)

assert part1(['R2', 'L3']) == 5
assert part1(['R2', 'R2', 'R2']) == 2
assert part1(['R5', 'L5', 'R5', 'R3']) == 12
print("The solution to part 1 is", part1(instructions))
