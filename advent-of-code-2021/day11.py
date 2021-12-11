#pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name
from typing import List
from lib import check_coordinates
from lib import inputgetter_int_matrix

Matrix = List[List[int]]

matrix: Matrix = inputgetter_int_matrix('inputs/11.txt')
tests_matrix: Matrix = inputgetter_int_matrix('tests/11.txt')

def increase_by_one(m) -> Matrix:
    for x, row in enumerate(m):
        for y, _ in enumerate(row):
            m[x][y] += 1
    return m

def flash_increase(x, y, m) -> Matrix:
    for x_inc in (-1, 0, 1):
        for y_inc in (-1, 0, 1):
            if check_coordinates(x+x_inc, y+y_inc, m):
                m[x+x_inc][y+y_inc] += 1
    return m

def caused_more_flashes(m, flashes_in_step):
    # This is equivalent to
    # while any(m[x][y] > 9 for x in range(len(m)) for y in range(len(m[0])) if (x,y) not in flashes_in_step):
    # which is arguably a too long line
    for x, row in enumerate(m):
        for y, col in enumerate(row):
            if (x,y) not in flashes_in_step:
                if col > 9:
                    return True
    return False

def solve(m) -> None:
    flashes = 0
    for i in range(1, 1000):
        m = increase_by_one(m)
        flashes_in_step = []
        while caused_more_flashes(m, flashes_in_step):
            for x, row in enumerate(m):
                for y, col in enumerate(row):
                    if col > 9 and (x,y) not in flashes_in_step:
                        m = flash_increase(x, y, m)
                        flashes_in_step.append((x,y))
        flashes += len(flashes_in_step)
        if len(flashes_in_step) == len(m)*len(m[0]):
            print(f"The solution to part 2 is: {i}")
            break
        if i == 100:
            print(f"The solution to part 1 is: {flashes}")
        for x, y in flashes_in_step:
            m[x][y] = 0

solve(tests_matrix)
solve(matrix)
