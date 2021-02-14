instructions = []

with open('input01.txt', encoding='utf8') as f:
    for line in f:
        unclean_instr = line.strip().split(',')
        for instruction in unclean_instr:
            instructions.append(instruction.strip())

def update_visited(current, xory, sign, n):
    assert xory in ['x', 'y']
    assert sign in ['+', '-']
    passed_blocks = []
    for step in range(1, n+1):
        if xory == 'x':
            newx = current[0] + int(sign + str(step))
            passed_blocks.append((newx, current[1]))
        else:
            newy = current[1] + int(sign + str(step))
            passed_blocks.append((current[0], newy))
    return passed_blocks

def part1(instr):
    x, y = 0, 0
    facing = 'N'
    visited = [(0,0)]
    part2 = 0
    for i in instr:
        turn, n = i[0], int(i[1:])
        if turn == 'L':
            if facing == 'N':
                x -= n
                passed_blocks = update_visited(visited[-1], 'x', '-', n)
                facing = 'W'
            elif facing == 'S':
                x += n
                passed_blocks = update_visited(visited[-1], 'x', '+', n)
                facing = 'E'
            elif facing == 'W':
                y -= n
                passed_blocks = update_visited(visited[-1], 'y', '-', n)
                facing = 'S'
            elif facing == 'E':
                y += n
                passed_blocks = update_visited(visited[-1], 'y', '+', n)
                facing = 'N'
        elif turn == 'R':
            if facing == 'N':
                x += n
                passed_blocks = update_visited(visited[-1], 'x', '+', n)
                facing = 'E'
            elif facing == 'S':
                x -= n
                passed_blocks = update_visited(visited[-1], 'x', '-', n)
                facing = 'W'
            elif facing == 'W':
                y += n
                passed_blocks = update_visited(visited[-1], 'y', '+', n)
                facing = 'N'
            elif facing == 'E':
                y -= n
                passed_blocks = update_visited(visited[-1], 'y', '-', n)
                facing = 'S'

        for b in passed_blocks:
            if part2 == 0:
                if b in visited:
                    part2 = abs(b[0]) + abs(b[1])
            visited.append(b)
                
    return abs(x) + abs(y), part2

assert part1(['R2', 'L3']) == (5, 0)
assert part1(['R2', 'R2', 'R2']) == (2, 0)
assert part1(['R5', 'L5', 'R5', 'R3']) == (12, 0)
assert part1(['R8', 'R4', 'R4', 'R8']) == (8, 4)
print("The solution to part 1 and part2 is", part1(instructions))
