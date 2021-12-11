#pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name
from typing import List
from typing import Set
from typing import Tuple

from lib import inputgetter_list

sym2points = {')': 3, ']': 57, '}': 1197, '>': 25137}
sym2points2 = {'(': 1, '[': 2, '{': 3, '<': 4}
close2open = {')': '(', ']': '[', '}': '{', '>': '<'}
open2close = {v: k for k, v in close2open.items()}

inp = inputgetter_list('inputs/10.txt')

tests_inp = inputgetter_list('tests/10.txt')

opening = list(close2open.values())
closing = list(close2open.keys())

def solve(data: List[str]) -> Tuple[int, Set]:
    score = 0
    corrupted = set()
    for i, line in enumerate(data):
        opened = []
        for char in line.strip():
            if char in opening:
                opened.append(char)
            if char in closing:
                if char != open2close[opened[-1]]:
                    score += sym2points[char]
                    corrupted.add(i)
                    break
                opened.pop()
    return score, corrupted

tests_solution, test_corrupted = solve(tests_inp)
assert tests_solution == 26397
solution, corrupt = solve(inp)
print(f"The solution to part 1 is: {solution}")

def solve2(data: List[str], filtered_inputs: Set[str]) -> int:
    scores = []
    for i, line in enumerate(data):
        line_score = 0
        if i in filtered_inputs:
            continue
        opened = []
        for char in line.strip():
            if char in opening:
                opened.append(char)
            if char in closing:
                if char == open2close[opened[-1]]:
                    opened.pop()
        for char in opened[-1::-1]:
            line_score *= 5
            line_score += sym2points2[char]
        scores.append(line_score)

    scores.sort()
    middle = (len(scores)//2)

    return scores[middle]

solution2 = solve2(inp, corrupt)
print(f"The solution to part 1 is: {solution2}")
