import re

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

