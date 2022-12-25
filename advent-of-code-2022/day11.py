import re

from typing import Dict

math = {'+': int.__add__,
'-': int.__sub__,
'*': int.__mul__,
'/': int.__floordiv__}

def monkey_getter(file: str) -> Dict:
    monkey_dict = {}
    with open(file, encoding='utf8') as f:
        monkeys = f.read().split('\n\n')
    for m in monkeys:
        # parsing nonsense, curse you Eric!
        num = int(m.split(':')[0].split()[-1])
        items = list(map(int, re.search(r'(?<=Starting items: ).*?(?=\n)', m).group().split(',')))
        # this can be 'old' or an int
        op, n = re.search(r'(?<=new = old ).*?(?=\n)', m).group().split()
        test = int(re.search(r'(?<=divisible by ).*?(?=\n)', m).group())
        iftrue = int(re.search(r'(?<=If true: throw to monkey ).*?(?=\n)', m).group())
        iffalse = int(re.search(r'(?<=If false: throw to monkey ).*', m).group())

        monkey_dict[num] = {
                            'items': items,
                            'op': (math[op], n),
                            'test': test,
                            'iftrue': iftrue,
                            'iffalse': iffalse,
                            'inspected': 0
        }
    return monkey_dict

def solve(infile: str, part2: bool = False) -> int:
    monkey_dict = monkey_getter(infile)
    n_monkeys = len(monkey_dict)
    num_rounds = 10000 if part2 else 20
    for _ in range(num_rounds):
        for i in range(n_monkeys):
            monkey = monkey_dict[i]
            for item in monkey['items']:
                second_argument = int(monkey['op'][1] if monkey['op'][1].isnumeric() else item)
                worry_level = monkey['op'][0](item, second_argument)
                if not part2:
                    worry_level = worry_level//3
                if worry_level % monkey['test'] == 0:
                    monkey_dict[monkey['iftrue']]['items'].append(worry_level)
                else:
                    monkey_dict[monkey['iffalse']]['items'].append(worry_level)
                monkey['inspected'] += 1
            monkey['items'] = []
    inspected = sorted([v['inspected'] for k, v in monkey_dict.items()], reverse=True)

    return inspected[0] * inspected[1]


test_solution = solve('tests/11.txt')
assert test_solution == 10605

solution = solve('inputs/11.txt')
print(f'The solution to part 1 is: {solution}')

test_solution2 = solve('tests/11.txt', part2=True)
assert test_solution2 == 2713310158, test_solution2

solution2 = solve('inputs/11.txt', part2=True)
print(f'The solution to part 2 is: {solution}')
