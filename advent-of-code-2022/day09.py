# pylint: disable=invalid-name,missing-function-docstring,missing-module-docstring
from typing import List

from lib import inputgetter_list

inp = inputgetter_list('inputs/09.txt')
tests = inputgetter_list('tests/09.txt')
tests2 = inputgetter_list('tests/09_2.txt')

def move_H(d: str, H_: List[int]) -> List[int]:
    if d == 'L':
        H_[1] -= 1
    if d == 'R':
        H_[1] += 1
    if d == 'U':
        H_[0] -= 1
    if d == 'D':
        H_[0] += 1
    return H_

def move_T(H_: List[int], T_: List[int]) -> List[int]:
    diff_x = H_[0] - T_[0]
    diff_y = H_[1] - T_[1]
    touching_x = diff_x in (-1, 0, 1)
    touching_y = diff_y in (-1, 0, 1)
    if not (touching_x and touching_y):
        # T needs to move
        move_x = 1 if diff_x > 0 else -1
        move_y = 1 if diff_y > 0 else -1
        if diff_x and diff_y:
            # move diagonally
            T_[0] += move_x
            T_[1] += move_y
        elif diff_x:
            # move vertically
            T_[0] += move_x
        elif diff_y:
            # move horizontally
            T_[1] += move_y
    return T_

def solve(commands: List[str], num_knots: int = 2) -> int:
    knots = [[0, 0] for _ in range(num_knots)]
    visited = set()
    visited.add((0, 0))

    for comm in commands:
        direction, n = comm.split()
        for _ in range(int(n)):
            knots[0] = move_H(direction, knots[0])
            for i, _ in enumerate(knots[1:], 1):
                knots[i] = move_T(knots[i-1], knots[i])
            visited.add((knots[-1][0], knots[-1][1]))

    return len(visited)

test_solution = solve(tests)
assert test_solution == 13

solution = solve(inp)
print(f'The solution to part 1 is: {solution}')

test_solution2 = solve(tests, num_knots=10)
assert test_solution2 == 1

test_solution3 = solve(tests2, num_knots=10)
assert test_solution3 == 36

solution2 = solve(inp, num_knots=10)
print(f'The solution to part 2 is: {solution2}')
