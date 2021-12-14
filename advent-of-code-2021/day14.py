#pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name
from collections import Counter
from typing import Dict

rulebook = {}
with open('inputs/14.txt', encoding='utf8') as f:
    for i, line in enumerate(f):
        if i == 0:
            template = line.strip()
        elif i >= 2:
            line = line.strip().split('->')
            rulebook[line[0].strip()] = line[1].strip()

tests_rulebook = {}
with open('tests/14.txt', encoding='utf8') as f:
    for i, line in enumerate(f):
        if i == 0:
            tests_template = line.strip()
        elif i >= 2:
            line = line.strip().split('->')
            tests_rulebook[line[0].strip()] = line[1].strip()

def solve(polymer: str, rules: Dict, part2: bool = False) -> int:
    num_iters = 40 if part2 else 10
    counter = Counter([polymer[i:i+2] for i in range(len(polymer)-1)])
    for _ in range(num_iters):
        new_counter = Counter()
        for pair, val in counter.items():
            mid = rules[pair]
            left, right = pair
            new_counter[left+mid] += val
            new_counter[mid+right] += val
        counter = new_counter
    final_counter = Counter()
    for pair, val in counter.items():
        for char in pair:
            final_counter[char] += val
    final_counter[polymer[0]] += 1
    final_counter[polymer[-1]] += 1
    ans = max(final_counter.values()) - min(final_counter.values())
    return ans//2

tests_solution = solve(tests_template, tests_rulebook)
assert tests_solution == 1588
solution = solve(template, rulebook)
print(f"The solution to part 1 is: {solution}")

tests_solution2 = solve(tests_template, tests_rulebook, part2=True)
assert tests_solution2 == 2188189693529
solution2 = solve(template, rulebook, part2=True)
print(f"The solution to part 2 is: {solution2}")
