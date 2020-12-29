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

def apply_or_mask(a, m):
    masked_a = ''
    for i, char in enumerate(m):
        if char == 'X':
            masked_a = masked_a + 'X'
        else:
            masked_a = masked_a + str((int(a[i]) or int(char)))

    addresses = []
    where_x = [i for i, c in enumerate(masked_a) if c == 'X']
    if 'X' in masked_a:
        for t in product(['0', '1'], repeat=len(where_x)):
            seq = list(masked_a)
            for i, c in zip(where_x, t):
                seq[i] = c
            addresses.append(''.join(seq))
    else:
        addresses = [a]

    return addresses

with open('input14.txt', encoding = 'utf8') as f:
    for line in f:
#for line in toy_input:   
        line = line.strip().split('=')
        if line[0].strip() == 'mask':
            mask = line[1].strip()
            continue
        if line[0].startswith('mem'):
            address = int(re.search(pattern, line[0]).group(0))
            address_bin = format(address, '#038b')

            addresses = apply_or_mask(address_bin[2:], mask)
            value = int(line[1].strip())

            for add in addresses:
                memory[add] = value

print("Solution to part 2 is:", sum(i for i in memory.values()))
