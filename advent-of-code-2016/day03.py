inp = []
with open('input03.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip().split()
        inp.append([int(i) for i in line])

def part1(triangles):
    counter = 0
    for x, y, z in triangles:
        if x + y > z:
            if x + z > y:
                if y + z > x:
                    counter += 1
    return counter

print("The solution to part 1 is:", part1(inp))

def part2(triangles):
    counter = 0
    for row in range(0, len(triangles), 3):
        for col in range(len(triangles[0])):
            if triangles[row][col] + triangles[row+1][col] > triangles[row+2][col]:
                if triangles[row][col] + triangles[row+2][col] > triangles[row+1][col]:
                    if triangles[row+1][col] + triangles[row+2][col] > triangles[row][col]:
                        counter += 1
    return counter

print("The solution to part 2 is:", part2(inp))
