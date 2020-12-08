

inp = open('input06.txt', encoding='utf8').readlines()

#part 1

groups = []
group = set()
for i, line in enumerate(inp):
    if i == len(inp) - 1:
        groups.append(group)
    if line != '\n':
        for char in line.strip():
            group.add(char)
    else:
        groups.append(group)
        group = set()
print(sum([len(i) for i in groups]))

# part 2

groups = []
group = []
person = set()
for i, line in enumerate(inp):
    if i == len(inp) - 1:
        groups.append(group)
    if line != '\n':
        for char in line.strip():
            person.add(char)
        group.append(person)
        person = set()
    else:
        groups.append(group)
        group = []

total = 0
for g in groups:
    total += len(g[0].intersection(*g[1:]))
print(total)
