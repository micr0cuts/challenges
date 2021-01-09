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
            # what if n were a list of [i,j,k] for example?
            if scores.get(prop):
                scores[prop] += n*value
            else:
                scores[prop] = n*value
    # this did not speed it up
    #fail_early = [True for v in scores.values() if v == None or v <= 0]
    #if any(fail_early):
    #    return 0

    for k,v in scores.items():
        if not v:
            v = 0
        s *= max(0, v)
    return s

assert calculate_score(["Butterscotch", "Cinnamon"], [44, 56], toy_kitchen) == 62842880
#all possible permutations of 1 to 4 ingredients in all possible combinations

def calculate_calories(ingredients, ns, kitchen):
    cals = 0
    for n, ing in zip(ns, ingredients):
        cals += n*kitchen[ing]['calories']
    return cals

assert calculate_calories(["Butterscotch", "Cinnamon"], [40, 60], toy_kitchen) == 500

perms = []
for i in range(1,5):
    perms.append(permutations(kitchen.keys(), i))

highest = 0
cal_highest = 0
for order in perms:
    for group in order:
        how_many = len(group)
        if how_many == 1:
            score = calculate_score(group, [100], kitchen)
            # part 2
            if calculate_calories(group, [100], kitchen) == 500:
                if score > cal_highest:
                    cal_highest = score
            if score > highest:
                highest = score
        if how_many == 2:
            for i in range(1, 100):
                score = calculate_score(group, [i, 100-i], kitchen)
                # part 2
                if calculate_calories(group, [i, 100-i], kitchen) == 500:
                    if score > cal_highest:
                        cal_highest = score
            if score > highest:
                highest = score
        if how_many == 3:
            for i in range(1,100):
                for j in range(1,100):
                    k = 100-i-j
                    score = calculate_score(group, [i, j, k], kitchen)
                    # part 2
                    if calculate_calories(group, [i, j, k], kitchen) == 500:
                        if score > cal_highest:
                            cal_highest = score
                    if score > highest:
                        highest = score
        if how_many == 4:
            for i in range(1,100):
                for j in range(1,100):
                    for k in range(1,100):
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

