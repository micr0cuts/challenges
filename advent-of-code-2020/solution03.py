mymap = []

num_rows = sum(1 for line in open('input3.txt', encoding='utf8'))
num_cols = 1 + 3*(num_rows-1)

with open('input3.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        reps = (num_cols//len(line))+1
        row = line*reps
        mymap.append(row)

trees_hit = 0

col = 0
for row in mymap:
    if row[col] == '.':
        col += 3
    elif row[col] == '#':
        col += 3
        trees_hit += 1
    else:
        raise Exception('This should not happen.')

print(trees_hit)