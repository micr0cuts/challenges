# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
from collections import defaultdict
from collections import OrderedDict

with open('tests/15.txt', encoding='utf8') as f:
    test = f.read().strip()


with open('inputs/15.txt', encoding='utf8') as f:
    inp = f.read().strip()

def get_HASH_value(x: str) -> int:
    current_value = 0
    for char in x:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

def solve(input_string: str) -> int:
    return sum(get_HASH_value(x) for x in input_string.split(','))

def solve2(input_string: str) -> int:
    boxes_dict: defaultdict[int, OrderedDict] = defaultdict(OrderedDict)
    for x in input_string.split(','):
        if '=' in x:
            lens, focal_length = x.split('=')
            box = get_HASH_value(lens)
            boxes_dict[box][lens] = int(focal_length)
        elif '-' in x:
            lens, _ = x.split('-')
            box = get_HASH_value(lens)
            if lens in boxes_dict[box]:
                del boxes_dict[box][lens]

    focusing_power = 0
    for box, lenses in boxes_dict.items():
        for i, lens in enumerate(lenses, start=1):
            focusing_power += (box + 1) * i * lenses[lens]
    return focusing_power

assert solve(test) == 1320, solve(test)
print(f'The solution to part 1 is: {solve(inp)}')

assert solve2(test) == 145, solve2(test)
print(f'The solution to part 2 is: {solve2(inp)}')
