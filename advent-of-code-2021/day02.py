#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List
from lib import inputgetter_list

inp: List = inputgetter_list('inputs/02.txt')
tests: List = inputgetter_list('tests/02.txt')

def solve(commands: List[str], part2: bool = False) -> int:
    aim: int = 0
    horizontal: int = 0
    depth:int = 0

    for i in commands:
        cmd, val = i.split()
        val = int(val)
        if cmd == "forward":
            horizontal += val
            if part2:
                depth += aim*val
        elif cmd == "down":
            if part2:
                aim += val
            else:
                depth += val
        elif cmd == "up":
            if part2:
                aim -= val
            else:
                depth -= val

    return horizontal*depth

test_solution: int = solve(tests[:-1])
print(test_solution, tests[-1])
assert test_solution == int(tests[-1])

solution1: int = solve(inp)
print(f"The solution to part1 is: {solution1}")

solution2: int = solve(inp, part2=True)
print(f"The solution to part2 is: {solution2}")
