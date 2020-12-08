entries = []

with open('input01.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        entries.append(int(line))

# part 1
found = False
for i in entries:
    if found:
        break
    for j in entries:
        if i == j:
            continue
        if i + j == 2020:
            print(i, j, i*j)
            found = True
# part 2
found = False
for i in entries:
    if found:
        break

    for j in entries:
        if i == j:
            continue
        elif found:
            break

        for k in entries:
            if i == k:
                continue

            if i + j + k == 2020:
                print(i, j, k, i*j*k)
                found = True
