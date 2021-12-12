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
    if y + 1 < len(m[x]):
        if m[x][y+1] <= p:
            return False
    # left
    if y - 1 >= 0:
        if m[x][y-1] <= p:
            return False
    # up
    if x - 1 >= 0: 
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

def find_basin(x, y, m, seen):
    p = m[x][y]
    basin = []

    if p != 9 and (x,y) not in seen:
        basin = [(x,y)]
        seen.add((x,y))
        # down
        if x + 1 < len(m):
            if m[x+1][y] > p:
                basin += find_basin(x+1, y, m, seen)
        # right
        if y + 1 < len(m[x]):
            if m[x][y+1] > p:
                basin += find_basin(x, y+1, m, seen)    
        # left
        if y - 1 >= 0:
            if m[x][y-1] > p:
                basin += find_basin(x, y-1, m, seen)
        # up
        if x - 1 >= 0: 
            if m[x-1][y] > p:
                basin += find_basin(x-1, y, m, seen)
    #print("here", basin)
    return basin

def has_multiple_low_points(basin, m):
    heights = [m[x][y] for x, y in basin]
    lowest = min(heights)
    return heights.count(lowest) != 1

def solve2(m):
    low_points = []
    basins = {}
    for x in range(len(m)):
        for y in range(len(m[x])):
            if is_lowpoint(x, y, m):
                low_points.append((x, y))
    seen = set()
    for x, y in low_points:
        #print("next lowpoint")
        #basins[(x,y)] = len(set(find_basin(x, y, m)))
        basins[(x,y)] = set(find_basin(x, y, m, seen))
    # legal_basins = []
    # for basin, v in basins.items():
    #     if not has_multiple_low_points(v, m):
    #         legal_basins.append(basin)
    # print(len(basins), len(legal_basins))
    # for v in basins.values():
    #     b = [m[x][y] for x, y in v]
    #     print(b)
    #print(basins)
    lens = [len(v) for v in basins.values()]
    ans = 1
    three_largest = sorted(lens, reverse=True)[:3]
    print("3", three_largest)
    for i in three_largest:
        ans *= i
    return ans

# tests_solution2: int = solve2(tests_matrix)
# assert tests_solution2 == 1134

# status 8 Dec 22:35 PT: tests pass but answer is wrong
solution2: int = solve2(matrix)
print(f'The solution to part 2 is: {solution2}')
