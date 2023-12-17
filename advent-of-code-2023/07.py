# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
from collections import Counter
from collections import defaultdict
from typing import List

from lib import inputgetter_list

tests = inputgetter_list('tests/07.txt')
inp = inputgetter_list('inputs/07.txt')
helper = inputgetter_list('tests/07_helper.txt') # helper input from Reddit

def score_hand_part1(h: Counter) -> int:
    sorted_values = sorted(h.values())
    # five of a kind
    if sorted_values == [5]:
        return 6
    # four of a kind
    if sorted_values == [1, 4]:
        return 5
    # full house
    if sorted_values == [2, 3]:
        return 4
    # three of a kind
    if sorted_values == [1, 1, 3]:
        return 3
    # two pair
    if sorted_values == [1, 2, 2]:
        return 2
    # one pair
    if sorted_values == [1, 1, 1, 2]:
        return 1
    # high card
    if sorted_values == [1, 1, 1, 1, 1]:
        return 0
    raise Exception('Value of hand not determinable')

def score_hand_part2(h: Counter) -> int:
    sorted_values = sorted(h.values())
    j_count = h[1]
    # five of a kind
    if sorted_values == [5]:
        return 6
    # four of a kind
    if sorted_values == [1, 4]:
        if j_count in (1, 4):
            return 6
        return 5
    # full house
    if sorted_values == [2, 3]:
        if j_count in (2, 3):
            return 6
        return 4
    # three of a kind
    if sorted_values == [1, 1, 3]:
        if j_count in (1, 3):
            return 5
        return 3
    # two pair
    if sorted_values == [1, 2, 2]:
        if j_count == 1:
            return 4
        if j_count == 2:
            return 5
        return 2
    # one pair
    if sorted_values == [1, 1, 1, 2]:
        if j_count in (1, 2):
            return 3
        return 1
    # high card
    if sorted_values == [1, 1, 1, 1, 1]:
        if j_count == 1:
            return 1
        return 0
    raise ValueError

def solve(input_list: List[str], part2: bool = False) -> int:
    card_to_int = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
               'Q': 12, 'K': 13, 'A': 14}
    if part2:
        card_to_int['J'] = 1
    hands = defaultdict(list)
    for line in input_list:
        hand, bid_str = line.split()
        converted_hand = [card_to_int[x] for x in hand]
        if part2:
            hand_counter = Counter(converted_hand)
            score = score_hand_part2(hand_counter)
        else:
            hand_counter = Counter(converted_hand)
            score = score_hand_part1(hand_counter)
        hands[score].append((converted_hand, int(bid_str)))
    answer = 0
    multiplier = 1
    for i in sorted(hands):
        for _, bid in sorted(hands[i]):
            answer += multiplier * bid
            multiplier += 1
    return answer

assert solve(tests, part2=False) == 6440
assert solve(helper, part2=False) == 6592
print(f'The solution to part 1 is: {solve(inp, part2=False)}')

assert solve(tests, part2=True) == 5905
assert solve(helper, part2=True) == 6839
print(f'The solution to part 2 is: {solve(inp, part2=True)}')
