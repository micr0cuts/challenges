from typing import List
from lib import inputgetter_list

inp: List = inputgetter_list('inputs/01.txt')
tests: List = inputgetter_list('tests/01.txt')

def solve(list_of_calories: List, part2: bool = False) -> int:
    calories = []
    interim_sum = 0
    top_n = 3 if part2 else 1

    for num_cal in list_of_calories + ['']:
        if not num_cal:
            calories.append(interim_sum)
            interim_sum = 0
            continue
        interim_sum += int(num_cal)

    return sum(sorted(calories, reverse=True)[:top_n])

test_solution = solve(tests, part2=False)
assert test_solution == 24000
solution1 = solve(inp, part2=False)
print(f"The solution to part 1 is: {solution1}")

test_solution2 = solve(tests, part2=True)
assert test_solution2 == 45000
solution2 = solve(inp, part2=True)
print(f"The solution to part 2 is: {solution2}")
