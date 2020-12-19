
instr = [line.strip() for line in open('input12toy.txt', encoding='utf8').readlines()]

# W/E axis
col = 0
# N/S axis
row = 0

direction_to_degree = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
degree_to_direction = {v: k for k, v in direction_to_degree.items()}
print(degree_to_direction)
facing = 'E'
for i in instr:
    comm, val = i[0], int(i[1:])
    if comm == 'N':
        row -= val
    elif comm == 'S':
        row += val
    elif comm == 'W':
        col -= val
    elif comm == 'E':
        col += val
    elif comm == 'F':
        if facing == 'N':
            row -= val
        elif facing == 'S':
            row += val
        elif facing == 'W':
            col -= val
        elif facing == 'E':
            col += val
        else:
            raise Exception("this shouldn't happen")
    elif comm == 'L' or comm == 'R':
        #sign = ''
        if comm == 'L':
            sign = '-'
        elif comm == 'R':
            sign = '+'
        else:
            raise Exception("this shouldn't happen")
        turn = int(sign + str(val//90))
        new_direction = (direction_to_degree[facing] + turn) % len(direction_to_degree)
        facing = degree_to_direction[new_direction]
    else:
        raise Exception("this shouldn't happen")
print("Solution to part 1 is:", abs(col) + abs(row))

# part 2
ship_col = 0
ship_row = 0
wp_col = 10
wp_row = -1

def distance_from_waypoint(ship_col, ship_row, wp_col, wp_row):
    col = abs(abs(ship_col) - abs(wp_col))
    row = abs(abs(ship_row) - abs(wp_row))
    return (col, row)

for i in instr:
    comm, val = i[0], int(i[1:])
    if comm == 'N':
        wp_row -= val
    elif comm == 'S':
        wp_row += val
    elif comm == 'W':
        wp_col -= val
    elif comm == 'E':
        wp_col += val
    elif comm == 'F':
        #gradient_col, gradient_row = distance_from_waypoint(ship_col, ship_row, wp_col, wp_row)
        # this is how I understand the examples given with the toy instructions
        # but not how I would understand the instruction "moving towards the waypoint"
        ship_row += val*wp_row
        ship_col += val*wp_col
    elif comm == 'L' or comm == 'R':
        #this part makes absolutely no sense to me so far
    else:
        raise Exception("this shouldn't happen")

