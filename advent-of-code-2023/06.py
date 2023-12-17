# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
from typing import List

tests = []
with open('tests/06.txt', encoding='utf8') as f:
    for line in f:
        tests.append(list(map(int, line.split(':')[1].split())))

inp = []
with open('inputs/06.txt', encoding='utf8') as f:
    for line in f:
        inp.append(list(map(int, line.split(':')[1].split())))

def solve(input_list: List[List[int]], part2: bool = False) -> int:
    answers = 1
    iterator = list(zip(input_list[0], input_list[1]))
    if part2:
        iterator = [(int(''.join(str(i) for i in input_list[0])),
            int(''.join(str(i) for i in input_list[1])))]
    for race_time, record_distance in iterator:
        this_answer = 0
        for hold_time in range(1, race_time):
            this_distance = (race_time - hold_time) * hold_time
            if this_distance > record_distance:
                this_answer += 1
        answers *= this_answer
    return answers

assert solve(tests, part2=False) == 288
print(f'The solution to part 1 is: {solve(inp, part2=False)}')

assert solve(tests, part2=True) == 71503
print(f'The solution to part 2 is: {solve(inp, part2=True)}')
