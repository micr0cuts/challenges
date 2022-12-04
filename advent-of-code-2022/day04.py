from typing import List

from lib import inputgetter_list

inp: List[str] = inputgetter_list('inputs/04.txt')
tests: List[str] = inputgetter_list('tests/04.txt')


def solve(assignments: List[str], part2: bool = False) -> int:
    overlaps = 0
    for a in assignments:
        left, right = a.split(',')
        left_start, left_end = map(int, left.split('-'))
        right_start, right_end = map(int, right.split('-'))
        left = list(range(left_start, left_end + 1))
        right = list(range(right_start, right_end + 1))

        if part2:
            # overlaps += any(x for x in left if x in right)
            overlaps += len(set(left).intersection(right)) > 0
        else:
            # if left_start <= right_start and left_end >= right_end:
            #     overlaps += 1
            # elif right_start <= left_start and right_end >= left_end:
            #     overlaps += 1
            # second solution using sets
            overlaps += set(left).issubset(right) or set(left).issuperset(right)


    return overlaps

test_solution = solve(tests, part2=False)
assert test_solution == 2
solution1 = solve(inp, part2=False)
print(f'The solution for part1 is: {solution1}')

test_solution2 = solve(tests, part2=True)
assert test_solution2 == 4
solution2 = solve(inp, part2=True)
print(f'The solution for part2 is: {solution2}')
