import re
from itertools import product

memory = {}
mask = {}

pattern = re.compile(r'\d+')

def read_mask(string):
    m = {}
    for i, char in enumerate(string[::-1]):
        if char in ['0', '1']:
            m[i] = int(char)
    return m

def apply_mask(v, m):
    v = list(v[::-1])
    for pos, replacement in m.items():
        v[pos] = str(replacement)
    return ''.join(v[::-1])

with open('input14.txt', encoding = 'utf8') as f:
    for line in f:
        line = line.strip().split('=')
        if line[0].strip() == 'mask':
            mask = read_mask(line[1].strip())
            continue
        if line[0].startswith('mem'):
            address = int(re.search(pattern, line[0]).group(0))
            value = format(int(line[1].strip()), '#038b')
        else:
            raise Exception("This shouldn't happen", line)
        memory[address] = apply_mask(value, mask)

print("Solution to part 1 is:", sum([int(i, 2) for i in memory.values()]))

# part 2

toy_input = ['mask = 000000000000000000000000000000X1001X',
'mem[42] = 100',
'mask = 00000000000000000000000000000000X0XX',
'mem[26] = 1']

memory = {}

def get_addresses(m):
    seq = list(m)
    masks = []
    where_x = [i for i, c in enumerate(m) if c == 'X']
    # return list of all possible addresses where every X turns into 0 and 1 (all possible combinations)
    if 'X' in m:
        for t in product(['0', '1'], repeat=len(where_x)):
            for i, c in zip(where_x, t):
                seq[i] = c
            masks.append(''.join(seq))
        return masks
    return [m]

def apply_or_mask(a, m):
    a = list(a[:1:-1])
    address = ''
    for i, char in enumerate(m[::-1]):
        address = address + str((int(a[i]) or int(char)))
    return address[::-1]

#with open('input14.txt', encoding = 'utf8') as f:
    #for line in f:
for line in toy_input:   
    line = line.strip().split('=')
    if line[0].strip() == 'mask':
        mask = line[1].strip()
        continue
    if line[0].startswith('mem'):
        address = int(re.search(pattern, line[0]).group(0))
        address_bin = format(address, '#038b')

        masks = get_addresses(mask)
        value = int(line[1].strip())

        for m in masks:
            add = apply_or_mask(address_bin, m)
            memory[add] = value
    print(memory)
print("Solution to part 2 is:", sum(i for i in memory.values()))
