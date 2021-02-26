TOY = [".#.#.#",
       "...##.",
       "#....#",
       "..#...",
       "#.#..#",
       "####.."]

inp = [list(line.strip()) for line in open('input18.txt', encoding='utf8')]

def print_matrix(mat):
    for row in mat:
        print("".join(row))

def update_light(x, y, m):
    active_neighbours = 0
    for row_diff in [-1, 0, 1]:
        for col_diff in [-1, 0, 1]:
            if row_diff == 0 and col_diff == 0:
                continue
            new_x = x+row_diff
            new_y = y+col_diff
            if new_x >= 0 and new_x < len(m):
                if new_y >=0 and new_y < len(m[0]):
                    if m[new_x][new_y] == "#":
                        active_neighbours += 1

    if m[x][y] == '#' and active_neighbours in [2, 3]:
        return '#'
    elif m[x][y] == '#':
        return '.'
    elif m[x][y] == '.' and active_neighbours == 3:
        return '#'
    elif m[x][y] == '.':
        return '.'
    else:
        print(m,x,y)
        raise Exception("This shouldn't happen.")

def fix_corners(m):
    m[0][0] = '#'
    m[0][len(m[0])-1] = '#'
    m[len(m)-1][0] = '#'
    m[len(m)-1][len(m[0])-1] = '#'
    return m

def solve(matrix, num_steps=100, print_mat=False, part2=False):
    for i in range(num_steps):
        new_matrix = []
        for _ in range(len(matrix)):
            new_row = []
            for _ in range(len(matrix[0])):
                new_row.append("O")
            new_matrix.append(new_row)

        if part2:
            matrix = fix_corners(matrix)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                new_matrix[row][col] = update_light(row, col, matrix)
        matrix = new_matrix

        if print_mat:
            print_matrix(matrix)
    if part2:
        matrix = fix_corners(matrix)

    return sum([1 for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][y] == "#"])

assert solve([list(x) for x in TOY], 4) == 4, solve([list(x) for x in TOY], 4, print_mat=True)
print("The solution to part 1 is:", solve(inp, 100))
assert solve([list(x) for x in TOY], 5, part2=True) == 17, solve([list(x) for x in TOY], 5, part2=True)
print("The solution to part 2 is:", solve(inp, 100, part2=True))
