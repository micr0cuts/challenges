instructions = []

# try this again but where each row is a value in a dictionary 
# to prevent looping over the full matrix for every line further down

matrix = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    matrix.append(row)

comms = {'off': 0, 'on': 1}
with open('input06.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip().split()
        assert len(line) in [4, 5]
        if len(line) == 4:
            comm = line[0]
            start = line[1].split(',')
            end = line[3].split(',')
        elif len(line) == 5:
            comm = line[1]
            start = line[2].split(',')
            end = line[4].split(',')

        for i, row in enumerate(matrix):
            if i >= int(start[0]) and i <= int(end[0]):
                new_row = []
                for j, col in enumerate(row):
                    if j >= int(start[1]) and j <= int(end[1]):
                        if comm == 'toggle':
                            # commented out parts are part 1
                            # col = int(not col)
                            col += 2
                        #else:
                            #col = comms[comm]
                        elif comm == 'on':
                            col += 1
                        elif comm == 'off':
                            if col > 0:
                                col -= 1
                    new_row.append(col)
                matrix[i] = new_row

count = 0
for row in matrix:
    for col in row:
        # if col == 1:
        #     count += 1
        count += col
print("Solution to part 1:", count)
