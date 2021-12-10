#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List
from collections import defaultdict

signal_patterns = []
output_values = []
tests_signal_patterns = []
tests_output_values = []

with open('inputs/08.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip().split('|')
        signal_patterns.append(line[0].split())
        output_values.append(line[1].split())

with open('tests/08.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip().split('|')
        tests_signal_patterns.append(line[0].split())
        tests_output_values.append(line[1].split())

unique_numbers_to_length = {1: 2,
                            4: 4,
                            7: 3,
                            8: 7}

unique_length_to_numbers = {v: k for k, v in unique_numbers_to_length.items()}

c = defaultdict(int)
for values in output_values:
    for value in values:
        c[value] += 1

print(sum(v for k, v in c.items() if len(k) in unique_numbers_to_length.values()))

answers = []
#for v1, v2 in zip(tests_signal_patterns, tests_output_values):
for v1, v2 in zip(signal_patterns, output_values):
    values = v1
    values.extend(v2)
    candidates532 = set()
    candidates960 = set()
    eight = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    for value in values:
        # 1, 4, 7, and 8 have unique lengths (see above)
        # if len(value) == 5 -> (5, 2, 3)
        # elif len(value) == 6 -> (9, 6, 0)
        # furthermore use clues somehow: for candidates of (9,6,0): 
        # one of them should not have one of 1's letters, that must be 6 then!
        # same for candidates of (5,2,3): only 3 contains the same letters as 1.
        # the extra bit in a 7 could be used to exclude that bit as a differentiating factor for the missing mappings
        # the two extra bits of 4 (those who aren't part of 1) are also found in 5, but only one of them in 2 and 3
        v = set()
        for char in value:
            v.add(char)
        if len(value) == 2:
            one = v
        elif len(value) == 4:
            four = v
        elif len(value) == 3:
            seven = v
        elif len(value) == 5:
            candidates532.add(value)
        elif len(value) == 6:
            candidates960.add(value)

    four_unique = four - one
    seven_unique = seven - one
    three = set()
    for c in candidates532:
        if set(c).issuperset(one):
            for x in c:
                three.add(x)
            break
    candidates52 = candidates532
    for c in candidates532:
        if set(c) == three:
            candidates52 = candidates52 - {c}
    five = set()
    for c in candidates52:
        if set(c).issuperset(four_unique):
            for x in c:
                five.add(x)
            break
    candidates2 = candidates52
    for c in candidates52:
        if set(c) == five:
            candidates2 = candidates2 - {c}
    two = set()
    for c in candidates2:
        for x in c:
            two.add(x)
    six = set()
    for c in candidates960:
        if not set(c).issuperset(one):
            for x in c:
                six.add(x)
            break
    candidates90 = candidates960
    for c in candidates960:
        if set(c) == six:
            candidates90 = candidates90 - {c}
    nine = set()
    for c in candidates90:
        if set(c).issuperset(four_unique):
            for x in c:
                nine.add(x)
            break
    zero = set()
    candidates0 = candidates90
    for c in candidates90:
        if set(c) == nine:
            candidates0 = candidates0 - {c}
    for c in candidates0:
        for x in c:
            zero.add(x)
    solutions = [zero, one, two, three, four, five, six, seven, eight, nine]
    assert(all(solutions))
    print(solutions)
    answer = []
    for value in v2:
        print(value)
        for i, s in enumerate(solutions):
            if set(value) == s:
                answer.append(i)
                break
            print(answer)
    answers.append(int(''.join([str(x) for x in answer])))
print(answers)
#assert sum(answers) == 61229
print(sum(answers))