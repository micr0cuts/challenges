from collections import Counter

database = []

with open('input02.txt', encoding='utf8') as f:
    for i, line in enumerate(f):
        line = line.strip().split()
        minmax = line[0].split('-')
        minimum = int(minmax[0])
        maximum = int(minmax[1])
        letter = line[1].rstrip(":")
        password = line[2]

        database.append((minimum, maximum, letter, password))

# part 1

valids = 0

for entry in database:
    counter = Counter(entry[3])
    if counter[entry[2]] < entry[0] or counter[entry[2]] > entry[1]:
        continue
    else:
        valids += 1

print(valids)

# part 2

valids = 0

for (idx1, idx2, letter, password) in database:

    if password[idx1 - 1] == letter:
        if not password[idx2 - 1] == letter:
            valids += 1

    elif not password[idx1 - 1] == letter:
        if password[idx2 - 1] == letter:
            valids += 1

print(valids)
