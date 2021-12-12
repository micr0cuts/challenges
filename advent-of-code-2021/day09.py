#pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name
from typing import List
from typing import Tuple

from lib import check_coordinates
from lib import inputgetter_int_matrix
from lib import Matrix

matrix: Matrix = inputgetter_int_matrix('inputs/09.txt')
tests_matrix: Matrix = inputgetter_int_matrix('tests/09.txt')

def is_lowpoint(x, y, m) -> bool:
    p = m[x][y]
    for x_inc in (-1, 0, 1):
        for y_inc in (-1, 0, 1):
            # skip diagonals
            if abs(x_inc-y_inc) == 1:
                if check_coordinates(x+x_inc, y+y_inc, m):
                    if m[x+x_inc][y+y_inc] <= p:
                        return False
    return True

def solve(m) -> int:
    low_points = []
    for x, row in enumerate(m):
        for y, col in enumerate(row):
            if is_lowpoint(x, y, m):
                low_points.append(col)

    return sum(1+p for p in low_points)

tests_solution: int = solve(tests_matrix)
assert tests_solution == 15
solution1: int = solve(matrix)
print(f'The solution to part 1 is: {solution1}')

def find_basin(x, y, m, seen) -> List[Tuple[int, int]]:
    p = m[x][y]
    basin = []
    # pylint: disable=too-many-nested-blocks
    if p != 9 and (x,y) not in seen:
        basin = [(x,y)]
        seen.add((x,y))
        for x_inc in (-1, 0, 1):
            for y_inc in (-1, 0, 1):
                # skip diagonals
                if abs(x_inc-y_inc) == 1:
                    if check_coordinates(x+x_inc, y+y_inc, m):
                        if m[x+x_inc][y+y_inc] > p:
                            basin += find_basin(x+x_inc, y+y_inc, m, seen)
    return basin

def solve2(m) -> int:
    low_points = []
    basins = {}
    for x, row in enumerate(m):
        for y, _ in enumerate(row):
            if is_lowpoint(x, y, m):
                low_points.append((x, y))
    seen = set()
    for x, y in low_points:
        basins[(x,y)] = set(find_basin(x, y, m, seen))
    lens = [len(v) for v in basins.values()]
    ans = 1
    three_largest = sorted(lens, reverse=True)[:3]
    for i in three_largest:
        ans *= i
    return ans

tests_solution2: int = solve2(tests_matrix)
assert tests_solution2 == 1134

solution2: int = solve2(matrix)
print(f'The solution to part 2 is: {solution2}')
