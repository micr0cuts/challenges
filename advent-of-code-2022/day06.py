from collections import deque

inp: str = ''
with open('inputs/06.txt', encoding='utf8') as f:
    for line in f:
        inp += line.strip()

TESTS = [('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
         ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
         ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
         ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26)]

def solve(signal: str, n_distinct: int = 4) -> int:
    buffer: deque = deque()
    for i, char in enumerate(signal, 1):
        buffer.append(char)
        if i >= n_distinct + 1:
            buffer.popleft()
        if len(set(buffer)) == n_distinct:
            return i
    raise ValueError('reached end of signal without a solution')

for test, solution, _ in TESTS:
    test_solution = solve(test, n_distinct=4)
    assert test_solution == solution

solution = solve(inp, n_distinct=4)
print(f'The solution to part 1 is: {solution}')

for test, _, solution in TESTS:
    test_solution = solve(test, n_distinct=14)
    assert test_solution == solution

solution2 = solve(inp, n_distinct=14)
print(f'The solution to part 1 is: {solution2}')
