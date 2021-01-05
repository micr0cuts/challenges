from collections import defaultdict
from itertools import permutations

rules = defaultdict(int)
names = set()
with open('input13.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip().split()
        sign = '-' if line[2] == 'lose' else '+'
        rules[(line[0], line[-1].strip('.'))] = int(sign + line[3])
        names.add(line[0])

def calculate_happiness(person, nb1, nb2, r):
    happiness = 0
    if not "me" in [person, nb1]:
        happiness += r[(person, nb1)]
    if not "me" in [person, nb2]:
        happiness += r[(person, nb2)]
    return happiness

def solve(n, r):
    # one improvement could be to get rid of permutations that will produce
    # the same happiness score
    perms = permutations(n, len(n))
    scores = set()
    for p in perms:
        score = 0
        for i, person in enumerate(p):
            if i == len(p)-1:
                h = calculate_happiness(person, p[i-1], p[0], r)
            else:
                h = calculate_happiness(person, p[i-1], p[i+1], r)
            score += h
        scores.add(score)
    return max(scores)
print("The solution to part 1 is:", solve(names, rules))
names.add("me")
print("The solution to part 2 is:", solve(names, rules))
