from collections import defaultdict
from random import shuffle

TOY = {
       "London": {"Dublin": 464, "Belfast": 518},
       "Dublin": {"Belfast": 141, "London": 464},
       "Belfast": {"London": 518, "Dublin": 141}
       }

distances = defaultdict(dict)
with open('input09.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip().split()
        city1, city2, dist = line[0], line[2], line[4]
        distances[city1][city2] = int(dist)
        distances[city2][city1] = int(dist)

def brute_force_Travelling_Salesman(distance_dict):

    starts = list(distance_dict.keys())
    shortest = 10*sum([v for city in distance_dict for k, v in distance_dict[city].items()])
    for trial in range(10):
        while starts:
            dist_travelled = 0
            must_visit = distance_dict.keys()
            visited = set()
            too_long = False
            while visited != must_visit:
                for city1 in distance_dict:
                    if too_long:
                        break
                    if not visited:
                        city1 = starts.pop()
                    visited.add(city1)
                    keys = list(distance_dict[city1].keys())
                    # shuffling because we need different behaviour for each trial
                    shuffle(keys)
                    for city2 in keys:
                        if too_long:
                            break
                        if city1 == city2:
                            continue
                        # this code does not account for dead ends
                        # we could get into a dead end, turn around, and find the shortest path
                        # but the code treats dead ends as invalid
                        if city2 not in visited:
                            visited.add(city2)
                            dist_travelled += distance_dict[city1][city2]
                            if dist_travelled > shortest:
                                too_long = True
                            if visited == must_visit:
                                if dist_travelled < shortest:
                                    shortest = dist_travelled

    return shortest

assert brute_force_Travelling_Salesman(TOY) == 605, brute_force_Travelling_Salesman(TOY)
print("The solution to part 1 is:", brute_force_Travelling_Salesman(distances))
