import re
from collections import defaultdict

inp = [line.strip() for line in open('input16.txt', encoding='utf8').readlines()]

allowed_pattern = re.compile(r'(\d+)-(\d+)')

def part1(inp):
    allowed = set()
    for line in inp[:20]:
        for allowed_range in re.findall(allowed_pattern, line):
            for i in range(int(allowed_range[0]), int(allowed_range[1])+1):
                allowed.add(i)

    error_rate = 0
    for line in inp[25:]:
        line = [int(num) for num in line.split(',')]
        for i in line:
            if i not in allowed:
                error_rate += i
    return error_rate

print("The solution to part 1 is:", part1(inp))

def part2(inp):
    allowed = defaultdict(set)
    for line in inp[:20]:
        key = line.split(':')[0]
        for allowed_range in re.findall(allowed_pattern, line):
            for i in range(int(allowed_range[0]), int(allowed_range[1])+1):
                allowed[key].add(i)
    all_allowed = set()
    for lst in allowed.values():
        for v in lst:
            all_allowed.add(v)

    my_ticket = [int(num) for num in inp[22].split(',')]
    locked_pos = [None for i in range(len(allowed.keys()))]
    missing_keys = list(allowed.keys())

    while not all(locked_pos):
        open_fields = {k for k in missing_keys}
        impossible_pos = [set() for i in range(len(allowed.keys()))]

        for line in inp[25:]:
            hypothesised_fieldnames = [list() for i in range(len(allowed.keys()))]
            line = [int(num) for num in line.split(',')]

            #discard invalid tickets
            if not set(line).issubset(all_allowed):
                continue

            for i, num in enumerate(line):
                for k, v in allowed.items():
                    if num in v:
                        hypothesised_fieldnames[i].append(k)
            # process of elimination
            # find field names that can never be associated with a specific field
            for i, pos in enumerate(hypothesised_fieldnames):
                impossible_pos[i] = impossible_pos[i].union((open_fields - set(pos)))
        # find field that at this stage has only one possible key to be associated with
        for num, impossibles in enumerate(impossible_pos):
            print(num, impossibles)
            if len(impossibles) == len(open_fields) - 1:
                found = open_fields - impossibles
                found = found.pop()
                print("Found:", found)
                locked_pos[num] = found
                missing_keys.remove(found)

    assert sum([1 for i in locked_pos if i != None]) == len(allowed.keys())
    answer = 1
    for i, field in enumerate(locked_pos):
        if field.startswith('departure'):
            answer *= my_ticket[i]

    return answer

print("The solution to part 2 is:", part2(inp))
