col_shifts = [1, 3, 5, 7, 1]
row_shifts = [1, 1, 1, 1, 2]
results = []

for col_shift, row_shift in zip(col_shifts, row_shifts):

    mymap = []

    num_rows = sum(1 for line in open('input3emma.txt', encoding='utf8'))
    num_cols = 1 + col_shift*(num_rows-1)

    with open('input3emma.txt', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            reps = (num_cols//len(line))+1
            row = line*reps
            mymap.append(row)

    trees_hit = 0

    col_num = 0
    row_num = 0
    for i, row in enumerate(mymap):
        if i != row_num:
            continue
        try:
            if mymap[row_num][col_num] == '.':
                col_num += col_shift
                row_num += row_shift
            elif mymap[row_num][col_num] == '#':
                col_num += col_shift
                row_num += row_shift
                trees_hit += 1
            else:
                raise Exception('This should not happen.')
        except IndexError:
            print(i, row_num, col_num, num_cols, reps)

    results.append(trees_hit)
print(results)
ans = 1
for i in results:
    ans = ans*i

print(ans)
