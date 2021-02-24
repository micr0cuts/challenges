from collections import defaultdict

aunts = defaultdict(defaultdict)

TARGET = {"children": 3,
          "cats": 7,
          "samoyeds": 2,
          "pomeranians": 3,
          "akitas": 0,
          "vizslas": 0,
          "goldfish": 5,
          "trees": 3,
          "cars": 2,
          "perfumes": 1}

with open('input16.txt', encoding='utf8') as f:
    for n, line in enumerate(f, 1):
        line = line.strip().split(':', 1)
        for attribute in line[1].strip().split(','):
            k, v = attribute.strip().split(':')
            aunts[n][k] = int(v.strip())


def part1(a):
    for aunt in a:
        if all(a[aunt][att] == TARGET[att] for att in a[aunt].keys()):
            return aunt

print("The solution to part 1 is:", part1(aunts))

def validate_attribute(attribute, value):
    if attribute == 'cats' or attribute == 'trees':
        if value <= TARGET[attribute]:
            return False
    elif attribute == 'pomeranians' or attribute == 'goldfish':
        if value >= TARGET[attribute]:
            return False
    else:
        if value != TARGET[attribute]:
            return False
    return True

def part2(a):
    for aunt in a:
        if all(validate_attribute(att, v) for att, v in a[aunt].items()):
            return aunt

print("The solution to part 2 is:", part2(aunts))
