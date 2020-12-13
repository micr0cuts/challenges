from collections import defaultdict

inp = [line.strip() for line in open('input03.txt', encoding='utf8').readlines()]

instructions = ''

for i in inp:
    instructions = instructions + i

visited = defaultdict(int)
x = 0
y = 0

for char in instructions:
    assert char in ['^', 'v', '<', '>']
    coord = str(x) + '_' + str(y)
    visited[coord] += 1
    if char == '^':
        x -= 1
    elif char == 'v':
        x += 1
    elif char == '<':
        y -= 1
    elif char == '>':
        y += 1

print("Solution to part 1:", sum([1 for k, v in visited.items() if v > 0]))

# part 2

visited2 = defaultdict(int)
coords = {'Santa':[0,0], 'Robo': [0,0]}

for i, char in enumerate(instructions):
    actor = 'Robo'
    if i % 2 == 0:
        actor = 'Santa'
    house = str(coords[actor][0]) + '_' + str(coords[actor][1])
    visited2[house] += 1
    if char == '^':
        coords[actor][0] -= 1
    elif char == 'v':
        coords[actor][0] += 1
    elif char == '<':
        coords[actor][1] -= 1
    elif char == '>':
        coords[actor][1] += 1

print("Solution to part 1:", sum([1 for k, v in visited2.items() if v > 0]))
