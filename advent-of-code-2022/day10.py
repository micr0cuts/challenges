from typing import List

from lib import inputgetter_list

inp = inputgetter_list('inputs/10.txt')
tests = inputgetter_list('tests/10.txt')

def report_signal_strength(X: int, c: int) -> int:
    if c % 40 == 20:
        return c*X
    return 0

def draw_or_not(X: int, draw_index: int) -> str:
    # this time cycle represents an index
    # and starts at 0
    idx = (draw_index - 1) % 40
    if X in (idx - 1, idx, idx + 1):
        return 'X'
    return '.'

def solve(commands: List[str]) -> int:
    signal_strength = 0
    X = 1
    cycle = 1
    solution2 = []
    for comm in commands:
        solution2.append(draw_or_not(X, cycle))
        signal_strength += report_signal_strength(X, cycle)
        if comm == 'noop':
            cycle += 1
            continue
        _, value = comm.split()
        cycle += 1
        solution2.append(draw_or_not(X, cycle))
        signal_strength += report_signal_strength(X, cycle)
        cycle += 1
        X += int(value)

    for i in range(0, len(solution2), 40):
        print(solution2[i:i+40])
    return signal_strength

test_solution = solve(tests)
assert test_solution == 13140
print()
solution = solve(inp)
print(f'The solution to part 1 is: {solution}')
