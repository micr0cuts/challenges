# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring

from collections import defaultdict
from functools import reduce
from operator import mul
from typing import List

from lib import inputgetter_list

tests = inputgetter_list('tests/02.txt')
inp = inputgetter_list('inputs/02.txt')

def solve(input_list: List[str], part2: bool = False) -> int:
    POSSIBLE = {'red': 12, 'green': 13, 'blue': 14}
    answer = 0
    answer2 = 0
    for game in input_list:
        minimum_cubes_necessary: defaultdict[str, int] = defaultdict(int)
        game, draws = game.split(':')
        game_idx = int(game.split()[-1])
        draws = draws.split(';')
        impossible = False
        for draw in draws:
            draw = draw.strip()
            for x in draw.split(','):
                i, colour = x.split()
                if minimum_cubes_necessary[colour] < int(i):
                    minimum_cubes_necessary[colour] = int(i)
                if int(i) > POSSIBLE[colour]:
                    impossible = True
        if not impossible:
            answer += game_idx
        power = reduce(mul, minimum_cubes_necessary.values())
        answer2 += power
    if part2:
        return answer2

    return answer

assert solve(tests, part2=False) == 8, solve(tests, part2=False)
print(f'The solution to part 1 is: {solve(inp)}')

assert solve(tests, part2=True) == 2286
print(f'The solution to part 1 is: {solve(inp, part2=True)}')
