rows = [i for i in range(0, 128)]
columns = [i for i in range(0, 8)]

passes = []

with open('input05.txt', encoding='utf8') as f:
    for line in f:
        passes.append(line.strip())

testcases = ['FBFBBFFRLR']

seat_assignments = []
#for p in testcases:
for p in passes:
    possible_rows = rows
    possible_cols = columns
    for letter in p:
        half_rows = len(possible_rows)//2
        half_cols = len(possible_cols)//2
        #print(possible_rows)
        #print(possible_cols)
        if letter == 'F':
            possible_rows = possible_rows[0:half_rows]
        if letter == 'B':
            possible_rows = possible_rows[half_rows:]
        if letter == 'L':
            possible_cols = possible_cols[0:half_cols]
        if letter == 'R':
            possible_cols = possible_cols[half_cols:]
    seat_assignments.append((possible_rows[0], possible_cols[0]))
#print(seat_assignments)

def calculate_seat_id(seat_tuple):
    return seat_tuple[0]*8+seat_tuple[1]

taken_seat_ids = [calculate_seat_id(x) for x in seat_assignments]
print(max(taken_seat_ids))    

# part 2

possible_seat_ids = [i*8+c for i in rows for c in columns]

free_seats = [i for i in possible_seat_ids if i not in taken_seat_ids]
for free_seat in free_seats:
    if free_seat - 1 in free_seats or free_seat + 1 in free_seats:
        continue
    else:
        print(free_seat)
