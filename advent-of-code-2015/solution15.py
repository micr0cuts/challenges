from itertools import permutations

kitchen = {}

with open('input15.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip().split(':')
        kitchen[line[0]] = {}
        for prop in line[1:]:
            prop = prop.split(',')
            for p in prop:
                p = p.split()
                kitchen[line[0]][p[0]] = int(p[1])

toy_kitchen = {"Butterscotch": {"capacity": -1, "durability": -2, "flavor": 6, "texture": 3, "calories": 8},
"Cinnamon": {"capacity": 2, "durability": 3, "flavor": -2, "texture": -1, "calories": 3}}

def calculate_score(ingredients, ns, kitchen):
    props = [k for k in kitchen[list(kitchen.keys())[0]] if k != 'calories']
    s = 1
    scores = dict().fromkeys(props)

    for n, ing in zip(ns, ingredients):
        if n == 0:
            continue
        for prop in props:
            value = kitchen[ing][prop]
            if value == 0:
                continue
            if scores.get(prop):
                scores[prop] += n*value
            else:
                scores[prop] = n*value
    # fail early
    if None in scores.values() or min(scores.values()) <= 0:
        return 0

    for k,v in scores.items():
        if not v:
            v = 0
        s *= max(0, v)
    return s

assert calculate_score(["Butterscotch", "Cinnamon"], [44, 56], toy_kitchen) == 62842880

def calculate_calories(ingredients, ns, kitchen):
    cals = 0
    for n, ing in zip(ns, ingredients):
        cals += n*kitchen[ing]['calories']
    return cals

assert calculate_calories(["Butterscotch", "Cinnamon"], [40, 60], toy_kitchen) == 500

#all possible permutations of 1 to 4 ingredients in all possible combinations
perms = []
for i in range(1,5):
    perms.append(permutations(kitchen.keys(), i))

highest = 0
cal_highest = 0
for order in perms:
    for group in order:
        for i in range(0,101):
            for j in range(0,101-i):
                for k in range(0,101-i-j):
                    l = 100-i-j-k
                    score = calculate_score(group, [i, j, k, l], kitchen)
                    # part 2
                    if calculate_calories(group, [i, j, k, l], kitchen) == 500:
                        if score > cal_highest:
                            cal_highest = score
                    if score > highest:
                        highest = score

print("The solution to part 1 is:", highest)
print("The solution to part 2 is:", cal_highest)
