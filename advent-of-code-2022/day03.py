import string

from typing import List

from lib import inputgetter_list


inp = inputgetter_list('inputs/03.txt')
tests = inputgetter_list('tests/03.txt')

priorities = {}
for i, letter in enumerate(string.ascii_letters, 1):
    priorities[letter] = i

def solve(rucksack: List[str]) -> int:
    score = 0
    for compartment in rucksack:
        middle = len(compartment)//2
        first = compartment[:middle]
        second = compartment[middle:]
        assert len(first) == len(second)
        common = set(first).intersection(set(second))
        assert len(common) == 1
        score += priorities[common.pop()]

    return score

def solve2(rucksack: List[str]) -> int:
    score = 0
    for i in range(0, len(rucksack), 3):
        first = rucksack[i]
        second = rucksack[i+1]
        third = rucksack[i+2]
        common = set(first).intersection(second).intersection(third)
        assert len(common) == 1
        score += priorities[common.pop()]

    return score

test_solution = solve(tests)
assert test_solution == 157
solution1 = solve(inp)
print(f'The solution for part1 is: {solution1}')

test_solution2 = solve2(tests)
assert test_solution2 == 70
solution2 = solve2(inp)
print(f'The solution for part2 is: {solution2}')
