#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List
from typing import Tuple

from copy import deepcopy

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

data = deepcopy(inp)
print(type(data), data[0])
for _ in range(256):
    new_data = do_one_iteration(data)
    data = new_data

print(len(data))

