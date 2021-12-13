#pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name
from copy import deepcopy
from typing import Set

dots = set()
instructions = []
with open('inputs/13.txt', encoding='utf8') as f:
    for line in f:
        if line != '\n' and not line.startswith('fold'):
            coord = tuple(map(int, line.strip().split(',')))
            dots.add(coord)
        if line.startswith('fold'):
            line = line.strip().split()
            instr = line[-1].split('=')
            instructions.append((instr[0], int(instr[1])))
print(dots)
print(instructions)

def fold(axis, i, data) -> Set:
    new_data = deepcopy(data)
    # eliminate all dots that are on x==i
    for coords in data:
        x, y = coords
        if coords[axis] == i:
            new_data.remove((x, y))
    # every dot where x > i folds up:
    # the new x coordinate now becomes old_x-2*(old_x-i)
        elif coords[axis] > i:
            new_data.remove((x, y))
            new_coord = coords[axis] - 2*(coords[axis] - i)
            if axis:
                new_data.add((x, new_coord))
            else:
                new_data.add((new_coord, y))
    return new_data

def solve(paper, commands, part2=False) -> int:
    iterator = commands if part2 else commands[:1]
    for a, i in iterator:
        axis_idx = 0
        if a == 'y':
            axis_idx = 1
        paper = fold(axis_idx, i, paper)
    if part2:
        max_x = max(paper, key=lambda x:x[0])
        max_y = max(paper, key=lambda y:y[1])
        print(max_x, max_y)
        matrix = []
        for y in range(max_y[1]+1):
            row = []
            for x in range(max_x[0]+1):
                if (x, y) in paper:
                    row.append('#')
                else:
                    row.append(' ')
            matrix.append(row)
        for row in matrix:
            print(''.join(row))
    return len(paper)

solution = solve(dots, instructions)
print(f"The solution to part 1 is: {solution}")
solution2 = solve(dots, instructions, part2=True) #PERCGJPB
