from collections import Counter

left = []
right = []
with open('inputs/01.txt', encoding='utf8') as f:
    for line in f:
        first, second = line.strip().split()
        left.append(int(first))
        right.append(int(second))


def solve(left, right, part2=False):
    solution = 0
    if not part2:
        left.sort()
        right.sort()
        for first, second in zip(left, right):
            solution += abs(first - second)
        return solution

    #### part 2
    counter = Counter(right)

    for i in left:
        solution += i*counter[i]

    return solution

print(f'The solution to part 1 is: {solve(left, right, part2=False)}')
print(f'The solutiont o part 2 is: {solve(left, right, part2=True)}')
