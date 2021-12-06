#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List
from typing import Tuple

from copy import deepcopy
from collections import defaultdict
inp = []
tests = []

with open('inputs/06.txt') as f:
    for line in f:
        inp = list(map(int, line.split(',')))

with open('tests/06.txt') as f:
    for line in f:
        tests = list(map(int, line.split(',')))

print(inp, tests)

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

data = deepcopy(tests)
# for _ in range(80):
#     new_data = do_one_iteration(data)
#     data = new_data

# print(f"part1: {len(data)}")

new_spawns_keys = [i for i in range(256)]
new_spawns_values = [0 for _ in range(256)]

for fish in data:
    num = 256 - fish
    for i in range(num, 0, -7):
        new_spawns_values[i] += 1

#answer = len(data)
for iteration in new_spawns_keys[-1::-1]:
    for future_iter in range(iteration, 0, -7):
        print(iteration, future_iter)
        new_spawns_values[future_iter] += new_spawns_values[iteration]
print(new_spawns_values)
print(f"part2: {new_spawns_values[0] + len(data)}")

# for iteration, num_new_spawns in new_spawns.items():
#     num = 256 - iteration - fish
#     for i in range(num, 0, -7):
#         new_spawns[i] += num_new_spawns

# answer = len(data) + new_spawns[0]

# print(answer)

