# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
from typing import List

from lib import inputgetter_list

tests = inputgetter_list('tests/09.txt')
inp = inputgetter_list('inputs/09.txt')

def solve(input_list: List[str], part2: bool = False) -> int:
    answer = 0
    for history in input_list:
        x = [list(map(int, history.split()))]
        if part2:
            x = [list(map(int, history.split()))[::-1]]
        while any(i for i in x[-1]):
            new = []
            for j in range(1, len(x[-1])):
                new.append(x[-1][j] - x[-1][j-1])
            x.append(new)
        x[-1].append(0)
        for k in range(len(x)-1, 0, -1):
            new_value = x[k-1][-1] + x[k][-1]
            x[k-1].append(new_value)
        answer += new_value
    print(answer)
    return answer

assert solve(tests, part2=False) == 114
print(f'The solution for part 1 is: {solve(inp, part2=False)}')

assert solve([tests[-1]], part2=True) == 5
print(f'The solution for part 2 is: {solve(inp, part2=True)}')
