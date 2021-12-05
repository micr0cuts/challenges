#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List
from typing import Tuple

from lib import inputgetter_list

inp: List = inputgetter_list('inputs/05.txt')
tests: List = inputgetter_list('tests/05.txt')

def process_data(data: List) -> Tuple[List, List]:
    starts = []
    ends = []

    for entry in data:
        start, end = entry.split('->')
        start_x, start_y = map(int, start.split(','))
        starts.append((start_x, start_y))
        end_x, end_y = map(int, end.split(','))
        ends.append((end_x, end_y))

    return starts, ends

def make_ventmap(m_x: int, m_y: int) -> List:
    ventmap = []
    for _ in range(m_x+1):
        ventmap.append([0 for _ in range(m_y+1)])
    return ventmap

def solve(data, part2: bool = False) -> int:
    # pylint: disable=too-many-locals
    start_coords, end_coords = process_data(data)
    max_x = max(x[0] for x in start_coords + end_coords)
    max_y = max(y[1] for y in start_coords + end_coords)
    ventmap = make_ventmap(max_x, max_y)
    for (s_x, s_y), (e_x, e_y) in zip(start_coords, end_coords):
        if s_x == e_x:
            # horizontal
            stride = 1 if s_y - e_y <= 0 else -1
            for col in range(s_y, e_y+stride, stride):
                ventmap[s_x][col] += 1
        elif s_y == e_y:
            # vertical
            stride = 1 if s_x - e_x <= 0 else -1
            for row in range(s_x, e_x+stride, stride):
                ventmap[row][s_y] += 1
        elif part2:
            # diagonal
            stride_x = 1 if s_x - e_x <= 0 else -1
            stride_y = 1 if s_y - e_y <= 0 else -1
            iterator = zip(range(s_x, e_x+stride_x, stride_x), range(s_y, e_y+stride_y, stride_y))
            for row, col in iterator:
                ventmap[row][col] += 1

    answer = 0
    for row in ventmap:
        for col in row:
            if col >= 2:
                answer += 1
    return answer

tests_solution: int = solve(tests)
assert tests_solution == 5
solution1: int = solve(inp)
print(f"The answer to part 1 is: {solution1}")
tests_solution2: int = solve(tests, part2=True)
print(tests_solution2)
assert tests_solution2 == 12
solution2: int = solve(inp, part2=True)
print(f"The answer to part 2 is: {solution2}")
