#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List

inp = []
tests = []

with open('inputs/07.txt', encoding='utf8') as f:
    for line in f:
        inp = list(map(int, line.split(',')))

with open('tests/07.txt', encoding='utf8') as f:
    for line in f:
        tests = list(map(int, line.split(',')))

def solve(data: List) -> int:
    answers = {}
    answers2 = {}
    for pos_to_align_to in range(0, max(data)):
        cost_to_align = 0
        cost_to_align2 = 0
        for crab_position in data:
            cost_to_align += abs(pos_to_align_to - crab_position)
            cost_to_align2 += sum(range(0, abs(pos_to_align_to - crab_position) + 1))
        answers[pos_to_align_to] = cost_to_align
        answers2[pos_to_align_to] = cost_to_align2

    return min(answers.values()), min(answers2.values())

tests_solution, tests_solution2 = solve(tests)
assert tests_solution == 37
solution1, solution2 = solve(inp)
assert tests_solution2 == 168

print(f"The answer to part 1 is: {solution1}")
print(f"The answer to part2 is: {solution2}")
