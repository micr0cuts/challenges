#pylint: disable=missing-module-docstring,missing-function-docstring

matrix = []
tests_matrix = []

with open('inputs/09.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        matrix.append([int(char) for char in line])

with open('tests/09.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        tests_matrix.append([int(char) for char in line])

def is_lowpoint(x, y, m):
    p = m[x][y]
    # down
    if x + 1 < len(m):
        if m[x+1][y] <= p:
            return False
    # right
    if y+1 < len(m[x]):
        if m[x][y+1] <= p:
            return False
    # left
    if y-1 >= 0:
        if m[x][y-1] <= p:
            return False
    # up
    if x-1 >= 0: 
        if m[x-1][y] <= p:
            return False
    return True

def solve(m):
    low_points = []
    for x in range(len(m)):
        for y in range(len(m[x])):
            if is_lowpoint(x, y, m):
                low_points.append(m[x][y])

    return sum(1+p for p in low_points)

tests_solution: int = solve(tests_matrix)
assert tests_solution == 15
solution1: int = solve(matrix)
print(f'The solution to part 1 is: {solution1}')

def find_basin(x, y, m):
    p = m[x][y]
    basin = []

    if p != 9:
        basin = [(x,y)]
        if x + 1 < len(m):
            if m[x+1][y] == p + 1:
                basin += find_basin(x+1, y, m)
        # right
        if y+1 < len(m[x]):
            if m[x][y+1] == p + 1:
                basin += find_basin(x, y+1, m)    
        # left
        if y-1 >= 0:
            if m[x][y-1] == p + 1:
                basin += find_basin(x, y-1, m)
        # up
        if x-1 >= 0: 
            if m[x-1][y] == p + 1:
                basin += find_basin(x-1, y, m)
    #print("here", basin)
    return basin

def solve2(m):
    low_points = []
    basins = {}
    for x in range(len(m)):
        for y in range(len(m[x])):
            if is_lowpoint(x, y, m):
                low_points.append((x, y))
    for x, y in low_points:
        #print("next lowpoint")
        basins[(x,y)] = len(set(find_basin(x, y, m)))
    #print(basins)
    ans = 1
    three_largest = sorted(basins.values(), reverse=True)[:3]
    print("3", three_largest)
    for i in three_largest:
        ans *= i
    return ans

tests_solution2: int = solve2(tests_matrix)
assert tests_solution2 == 1134

# status 8 Dec 22:35 PT: tests pass but answer is wrong
solution2: int = solve2(matrix)
print(f'The solution to part 2 is: {solution2}')
