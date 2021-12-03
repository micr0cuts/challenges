#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List
from collections import Counter
from collections import defaultdict

from lib import inputgetter_list

inp: List = inputgetter_list('inputs/03.txt')
tests: List = inputgetter_list('tests/03.txt')

assert len({len(x) for x in inp}) == 1

def get_most_least_common(list_of_bits, do_most_common):
    pos2bit = defaultdict(list)
    for bits in list_of_bits:
        for pos, bit in enumerate(bits):
            pos2bit[pos].append(bit)

    pos2_most_common = {}
    pos2_least_common = {}

    for k, v in pos2bit.items():
        most_common_counts = list(Counter(v).most_common(2))
        most_common = Counter(v).most_common(1)[0][0]
        if most_common_counts[0] == most_common_counts[1]:
            most_common = '1' if do_most_common else '0'
        pos2_most_common[k] = most_common
        pos2_least_common[k] = '0' if most_common == '1' else '1'

    return pos2_most_common, pos2_least_common

def solve(list_of_bits):
    gamma_rate = ''
    epsilon_rate = ''

    pos2gamma, pos2epsilon = get_most_least_common(list_of_bits, True)

    for k, v in sorted(pos2gamma.items(), key=lambda x:x[0]):
        gamma_rate += v
        epsilon_rate += pos2epsilon[k]

    return int(epsilon_rate, 2)*int(gamma_rate, 2)

assert solve(tests) == 198
solution1: int = solve(inp)
print(f"The solution to part 1 is: {solution1}")

def solve2(list_of_bits):
    oxygen_rating_candidates = set(list_of_bits)
    co2_scrubber_rating_candidates = set(list_of_bits)
    pos2_most_common, _ = get_most_least_common(list_of_bits, True)
    _, pos2_least_common = get_most_least_common(list_of_bits, False)
    for pos in range(len(list_of_bits[0])):
        if len(oxygen_rating_candidates) == 1:
            break
        for bits in list_of_bits:
            if len(oxygen_rating_candidates) == 1:
                break
            if bits in oxygen_rating_candidates:
                if bits[pos] != pos2_most_common[pos]:
                    oxygen_rating_candidates.remove(bits)

    # shitty duplication but Idk wtf I'm doing
    for pos in range(len(list_of_bits[0])):
        if len(co2_scrubber_rating_candidates) == 1:
            break
        for bits in list_of_bits:
            if len(co2_scrubber_rating_candidates) == 1:
                break
            if bits in co2_scrubber_rating_candidates:
                if bits[pos] != pos2_least_common[pos]:
                    co2_scrubber_rating_candidates.remove(bits)

    assert len(oxygen_rating_candidates) == 1
    assert len(co2_scrubber_rating_candidates) == 1
    oxygen_rating = oxygen_rating_candidates.pop()
    co2_scrubber_rating = co2_scrubber_rating_candidates.pop()

    return int(oxygen_rating, 2)*int(co2_scrubber_rating, 2)

print(solve2(tests))
assert solve2(tests) == 230
solution2: int = solve2(inp)
print(f"The solution to part 2 is: {solution2}")
