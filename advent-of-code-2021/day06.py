#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List

from collections import defaultdict

inp = []
tests = []

with open('inputs/06.txt', encoding='utf8') as f:
    for line in f:
        inp = list(map(int, line.split(',')))

with open('tests/06.txt', encoding='utf8') as f:
    for line in f:
        tests = list(map(int, line.split(',')))

### original solution for part 1
def do_one_iteration(data):
    new_data = []
    extension = []
    for fish in data:
        #print(fish)
        if fish == 0:
            extension.append(8)
            new_data.append(6)
        else:
            new_data.append(fish-1)
    new_data.extend(extension)
    return new_data

# data = deepcopy(inp)
school = inp
for _ in range(80):
    school = do_one_iteration(school)

print(f"The solution to part1 using brute force is: {len(school)}")
###

# After banging my head against walls and reading on reddit about it

def solve(data: List, days: int) -> int:
    all_fish = defaultdict(int)
    for fish in data:
        all_fish[fish] += 1

    for _ in range(days):
        new_all_fish = defaultdict(int)
        new_all_fish[8] += all_fish[0]
        new_all_fish[6] += all_fish[7] + all_fish[0]
        new_all_fish[0] = all_fish[1]
        new_all_fish[1] = all_fish[2]
        new_all_fish[2] = all_fish[3]
        new_all_fish[3] = all_fish[4]
        new_all_fish[4] = all_fish[5]
        new_all_fish[5] = all_fish[6]
        new_all_fish[7] = all_fish[8]
        all_fish = new_all_fish

    return sum(all_fish.values())

test_solution: int = solve(tests, 80)
assert test_solution == 5934
solution1: int = solve(inp, 80)
print(f"The solution to part 1 is: {solution1}")
test_solution2: int = solve(tests, 256)
assert test_solution2 == 26984457539
solution2: int = solve(inp, 256)
print(f"The solution to part 2 is: {solution2}")
