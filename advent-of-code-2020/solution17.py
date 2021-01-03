from collections import defaultdict

input_plane = []

with open('input17.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        new_line = []
        for char in line:
            if char == '.':
                new_line.append(0)
            else:
                new_line.append(1)
        input_plane.append(new_line)

def update_range(r):
    r.append(max(r)+1)
    r.append(min(r)-1)
    return sorted(r)

print(input_plane)
toy_input = [[0,1,0],[0,0,1],[1,1,1]]

matrix = defaultdict(int)
#for x, row in enumerate(input_plane):
print("Testing against toy input!!")
for x, row in enumerate(toy_input):
    for y, col in enumerate(row):
        #matrix[(x, y, 0)] = input_plane[x][y]
        matrix[(x, y, 0)] = toy_input[x][y]

r_x = [0,1,2]
r_y = [0,1,2]
r_z = [0]
print("Start:", matrix)
for cycle in range(6):
    print(cycle)
    r_x = update_range(r_x)
    r_y = update_range(r_y)
    r_z = update_range(r_z)
    new_matrix = defaultdict(int)
    for x in r_x:
        for y in r_y:
            for z in r_z:
                active_neighbours = 0
                for x2 in [-1, 0, 1]:
                    for y2 in [-1, 0, 1]:
                        for z2 in [-1, 0, 1]:
                            #print(x, y, z, x2, y2, z2)
                            if matrix[(x+x2,y+y2,z+z2)] == 1:
                                active_neighbours += 1
                if matrix[(x, y, z)] == 1:
                    if active_neighbours in [2, 3]:
                        new_matrix[(x, y, z)] = 1
                    else:
                        new_matrix[(x, y, z)] = 0
                elif matrix[(x, y, z)] == 0:
                    if active_neighbours == 3:
                        new_matrix[(x, y, z)] = 1
                    else:
                        new_matrix[(x, y, z)] = 0
    matrix = new_matrix
    print(new_matrix)

print(min([k[2] for k in matrix.keys()]))
print(max([k[2] for k in matrix.keys()]))


print("The solution to part 1 is:", sum(matrix.values()))
