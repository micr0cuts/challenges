#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List
from lib import inputgetter_list

inp: List = inputgetter_list('inputs/01.txt')
tests: List = inputgetter_list('tests/01.txt')
inp = [int(x) for x in inp]
tests = [int(x) for x in tests]

def solve(depth_measurements: List[int], part2: bool = False) -> int:
    stride: int = 3 if part2 else 1
    prev_measurements: int = 0
    increased: int = 0

    for i in range(0, len(depth_measurements)):
        look_at: List = depth_measurements[i:i+stride]
        the_sum: int = sum(look_at)

        if i > 0:
            if the_sum > prev_measurements:
                increased += 1

        prev_measurements = the_sum

    return increased

test_solution: int = solve(tests[:-1])
assert test_solution == tests[-1], test_solution

solution1: int = solve(inp)
print(f"The solution to part1 is: {solution1}")

solution2: int = solve(inp, part2=True)
print(f"The solution to part2 is: {solution2}")
