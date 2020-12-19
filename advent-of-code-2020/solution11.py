
inp = [line.strip() for line in open('input11.txt', encoding='utf8').readlines()]

toy_solution = ['#.#L.L#.##',
            '#LLL#LL.L#',
            'L.#.L..#..',
            '#L##.##.L#',
            '#.#L.LL.LL',
            '#.#L#L#.##',
            '..L.L.....',
            '#L#L##L#L#',
            '#.LLLLLL.L',
            '#.#L#L#.##']

def get_adjacent_occupation(matrix, x, y):
    num_adjacents_occupied = 0
    for row in [-1, 0, 1]:
        for col in [-1, 0, 1]:
            if row or col:
                #n is for neighbour's
                n_x = x+row
                n_y = y+col
                if n_x >= 0 and n_y >= 0 and n_x < len(matrix) and n_y < len(matrix[0]):
                    if matrix[n_x][n_y] == '#':
                        num_adjacents_occupied += 1
    return num_adjacents_occupied

matrix = inp
prev_matrix = []
while matrix != prev_matrix:
    new_matrix = []
    prev_matrix = matrix
    for x, row in enumerate(matrix):
        new_row = ''
        for y, col in enumerate(row):
            num_adj_occ = get_adjacent_occupation(matrix, x, y)
            if matrix[x][y] == 'L' and not num_adj_occ:
                new_row = new_row + '#'
            elif matrix[x][y] == '#' and num_adj_occ >= 4:
                new_row = new_row + 'L'
            else:
                new_row = new_row + matrix[x][y]
        new_matrix.append(new_row)
    matrix = new_matrix

occupied_seats = 0
for row in matrix:
        occupied_seats += row.count('#')
print(occupied_seats)

# part 2

def get_occupied_in_line_of_sight(matrix, x, y):
    num = 0
    # search left
    width = len(matrix[x])
    depth = len(matrix)
    for i in range(y-1, -1, -1):
        if matrix[x][i] == '#':
            num += 1
            break
        elif matrix[x][i] == 'L':
            break
    # search right
    for i in range(y+1, width, 1):
        if matrix[x][i] == '#':
            num += 1
            break
        if matrix[x][i] == 'L':
            break
    # search up
    for i in range(x-1, -1, -1):
        if matrix[i][y] == '#':
            num += 1
            break
        elif matrix[i][y] == 'L':
            break
    # search down
    for i in range(x+1, depth, 1):
        if matrix[i][y] == '#':
            num += 1
            break
        elif matrix[i][y] == 'L':
            break
    # search left up:
    j = x
    for i in range(y-1, -1, -1):
        j = j-1
        if j >= 0:
            if matrix[j][i] == '#':
                num +=1
                break
            elif matrix[j][i] == 'L':
                break
    # search left down:
    j = x
    for i in range(y-1, -1, -1):
        j = j+1
        if j < depth:
            if matrix[j][i] == '#':
                num +=1
                break
            elif matrix[j][i] == 'L':
                break
    # search right up:
    j = x
    for i in range(y+1, width, 1):
        j = j-1
        if j >= 0:
            if matrix[j][i] == '#':
                num +=1
                break
            elif matrix[j][i] == 'L':
                break
    # search right down:
    j = x
    for i in range(y+1, width, 1):
        j = j + 1
        if j < depth:
            if matrix[j][i] == '#':
                num +=1
                break
            elif matrix[j][i] == 'L':
                break

    return num

matrix = inp
prev_matrix = []
while matrix != prev_matrix:
    new_matrix = []
    prev_matrix = matrix
    for x, row in enumerate(matrix):
        new_row = ''
        for y, col in enumerate(row):
            num_adj_occ = get_occupied_in_line_of_sight(matrix, x, y)
            if matrix[x][y] == 'L' and not num_adj_occ:
                new_row = new_row + '#'
            elif matrix[x][y] == '#' and num_adj_occ >= 5:
                new_row = new_row + 'L'
            else:
                new_row = new_row + matrix[x][y]
        new_matrix.append(new_row)
    matrix = new_matrix


occupied_seats = 0
for row in matrix:
        occupied_seats += row.count('#')
print(occupied_seats)

