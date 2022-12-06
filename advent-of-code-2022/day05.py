from typing import List
from typing import Tuple

def get_n_stacks(file: str) -> int:
    with open(file, encoding='utf8') as f:
        n_stacks = len(f.readlines()[0])//4
    return n_stacks

def parse_stacks(file: str) -> Tuple[List[List[str]], int]:
    n_stacks = get_n_stacks(file)
    stacks: List[List[str]] = [[] for _ in range(n_stacks)]
    with open(file, encoding='utf8') as f:
        for ignore, line in enumerate(f, 1):
            if line.strip().split()[0] == '1':
                ignore_n = ignore
            for i in range(1, len(stacks)*4, 4):
                item = line[i]
                if item not in ('[', ']', ' '):
                    stacks[i//4].append(item)
        reversed_stacks = [s[::-1] for s in stacks]
        return reversed_stacks, ignore_n

def solve(file: str, part2: bool = False) -> str:
    with open(file, encoding='utf8') as f:
        stack_list, ignore_n = parse_stacks(file)
        for i, line in enumerate(f):
            if i <= ignore_n:
                # ignore crates
                continue
            line = line.split()
            # -1 for proper indexing
            amount, origin, destination = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
            if not part2:
                for _ in range(amount):
                    stack_list[destination].append(stack_list[origin].pop())
            else:
                new_stack = []
                for _ in range(amount):
                    new_stack.append(stack_list[origin].pop())
                for crate in new_stack[::-1]:
                    stack_list[destination].append(crate)
    return ''.join(stack[-1] for stack in stack_list)

test_solution = solve('tests/05.txt', part2=False)
assert test_solution == 'CMZ'
solution1 = solve('inputs/05.txt', part2=False)
print(f'The solution to part 1 is: {solution1}')

test_solution2 = solve('tests/05.txt', part2=True)
assert test_solution2 == 'MCD'
solution2 = solve('inputs/05.txt', part2=True)
print(f'The solution to part 2 is: {solution2}')
