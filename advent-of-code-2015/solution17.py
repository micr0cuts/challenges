from itertools import accumulate
from itertools import combinations
from operator import add

inp = [int(line.strip()) for line in open('input17.txt', encoding='utf8')]

TOY = [20, 15, 10, 5, 5]

def solve(containers, amount=150):
    mask_indexes = [i for i in range(len(containers))]
    combs = []
    for j in range(1, len(mask_indexes)):
        combs += combinations(mask_indexes, r=j)
    solutions = []
    for c in combs:
        acc = 0
        containers_used = []
        for n, container in enumerate(containers):
            if n in c:
                continue
            acc += container
            containers_used.append(container)
        if acc == amount:
            solutions.append(containers_used)

    # part2
    part2 = [len(sol) for sol in solutions]
    min_num = min(part2)
    part2_solution = [1 for sol in part2 if sol == min_num]

    return len(solutions), sum(part2_solution)

assert solve(TOY, 25) == (4, 3), solve(TOY, 25)
print("The solution to part 1 and part 2 is:", solve(inp, 150))
