# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
from collections import defaultdict
from typing import Any
from typing import List

from lib import inputgetter_list

tests = inputgetter_list('tests/04.txt')
inp = inputgetter_list('inputs/04.txt')

def get_card_dict(input_list) -> dict[int, defaultdict[str, Any]]:
    cards: dict[int, defaultdict[str, Any]] = {}
    for card in input_list:
        card_number, numbers = card.split(':')
        card_number = int(card_number.split()[1])
        winning_numbers, my_numbers = numbers.split('|')
        winning_numbers = winning_numbers.split()
        my_numbers = my_numbers.split()
        cards[card_number] = defaultdict(list)
        cards[card_number]['winning'] = winning_numbers
        cards[card_number]['mine'] = my_numbers
    return cards

def solve(input_list, part2: bool = False) -> int:
    answer = 0
    cards = get_card_dict(input_list)
    for card in cards.values():
        n_wins = sum(1 for n in card['mine'] if n in card['winning'])
        if n_wins:
            answer += 2**(n_wins-1)
        card['n_wins'] = n_wins
    if not part2:
        return answer

    new_cards = sorted(cards.keys())
    num_cards = len(cards)
    while new_cards:
        new_cards_ = [i for k in new_cards for i in range(k+1, k + cards[k]['n_wins']+1)]
        num_cards += len(new_cards_)
        new_cards = new_cards_
    return num_cards

assert solve(tests) == 13
print(f'The solution to part 1 is: {solve(inp)}')

assert solve(tests, part2=True) == 30
print(f'The solution to part 2 is: {solve(inp, part2=True)}')
