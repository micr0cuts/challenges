import re
from collections import defaultdict

# dict like d[container] = {containee: amount, containee2: amount2}
containers = defaultdict(dict)
# decided not to use regex after all
#pattern = r'(?P<container>\w+\s\w+\s)(bags?)\s(contain)\s\d\s\w+\s\w+\s(bags?)'
with open('input07.txt', encoding='utf8') as f:
    for line in f:
        container = " ".join(line.strip().split()[:2])
        containee_string = ' '.join(line.strip().split()[4:])
        for c in containee_string.split(','):
            c_split = c.split()
            if c_split[0] == 'no':
                amount = 0
            else:
                amount = int(c_split[0])
            containers[container][' '.join(c_split[1:3]).rstrip('.')] = amount

def what_type_can_hold_this(type_of_bag, registry):
    results = [type_of_bag]
    for container, containees in registry.items():
        for k in containees.keys():
            if k == type_of_bag:
                results += what_type_can_hold_this(container, registry)
    return results

result = set()
for container, containees in containers.items():
    for k, v in containees.items():
        if k == 'shiny gold' and v != 0:
            for t in [i for i in what_type_can_hold_this(container, containers)]:
                result.add(t)

print(len(result))

# part 2
def recurse(type_of_bag, registry):
    num = 1
    for c, a in registry[type_of_bag].items():
        if a != 0:
            num += a*recurse(c, registry)
    return num


number_of_bags_needed = 0
for containee, amount in containers['shiny gold'].items():
    if amount != 0:
        number_of_bags_needed += amount*recurse(containee, containers) 
print(number_of_bags_needed)
