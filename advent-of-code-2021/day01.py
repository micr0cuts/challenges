from lib import inputgetter_list
from typing import List

inp: List = inputgetter_list('inputs/01.txt')
tests: List = inputgetter_list('tests/01.txt')

def solve(inp: List, part2: bool = False) -> int:
    stride: int = 3 if part2 else 1
    prev_inp: int = 0
    increased: int = 0

    for i in range(0, len(inp)):
        look_at: List = inp[i:i+stride]
        the_sum: int = sum(int(x) for x in look_at)

        if i > 0:
            if the_sum > prev_inp:
                increased += 1

        prev_inp = the_sum

    return increased

test_solution: int = solve(tests[:-1])
assert  test_solution == int(tests[-1]), test_solution

solution1: int = solve(inp)
print(f"The solution to part1 is: {solution1}")

solution2: int = solve(inp, part2=True)
print(f"The solution to part2 is: {solution2}")
