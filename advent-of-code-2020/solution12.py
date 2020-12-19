
instr = [line.strip() for line in open('input12vasundhara.txt', encoding='utf8').readlines()]

# W/E axis
col = 0
# N/S axis
row = 0

# vals = set()
# for i in instr:
#     comm, val = i[0], int(i[1:])
#     if comm == 'L' or comm == 'R':
#         vals.add(val)
# print(vals)
direction_to_degree = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
degree_to_direction = {v: k for k, v in direction_to_degree.items()}

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
        sign = ''
        if comm == 'L':
            sign == '-'
        elif comm == 'R':
            sign == '+'
        else:
            raise Exception("this shouldn't happen")
        turn = int(sign + str(val//90))
        new_direction = (direction_to_degree[facing] + turn) % len(direction_to_degree)
        facing = degree_to_direction[new_direction]
    else:
        raise Exception("this shouldn't happen")
print(col, row)
print(abs(col) + abs(row))
