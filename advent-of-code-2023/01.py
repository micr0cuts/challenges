# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
import re

from typing import List

from lib import check_coordinates
from lib import inputgetter_list

inp = inputgetter_list('inputs/01.txt')
tests1 = inputgetter_list('tests/01_1.txt')
tests2 = inputgetter_list('tests/01_2.txt')

def solve(input_list: List[str], part2: bool = False) -> int:
    solutions = []
    DIGITS = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
              'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    DIGITS_FOR_RE = list(DIGITS.values())
    if part2:
        DIGITS_FOR_RE += list(DIGITS.keys())

    for line in input_list:
        matches = []
        reverse_matches = []
        for digit in DIGITS_FOR_RE:
            match = re.search(digit, line)
            reverse_match = re.search(digit[::-1], line[::-1])
            if match:
                matches.append((match.start(), match.end(), match.group()))
            if reverse_match:
                reverse_matches.append(
                    (reverse_match.start(), reverse_match.end(), reverse_match.group()[::-1])
                )
        first = sorted(matches, key=lambda x: x[0])[0][2]
        second = sorted(reverse_matches, key=lambda x: x[0])[0][2]
        first = DIGITS[first] if not first.isdigit() else first
        second = DIGITS[second] if not second.isdigit() else second

        solutions.append(int(first + second))
    return sum(solutions)

assert solve(tests1, part2=False) == 142, solve(tests1, part2=False)
print(f'The solution to part 1 is: {solve(inp, part2=False)}')

assert solve(tests2, part2=True) == 281

print(f'The solution to part 2 is: {solve(inp, part2=True)}')
