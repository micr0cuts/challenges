
inp = [line.strip().split() for line in open('input08.txt', encoding='utf8').readlines()]

accumulator = 0

pos = 0
visited = set()

while True:
    comm, val = inp[pos][0], inp[pos][1]
    print(pos, comm, val, visited)
    if comm == 'acc':
        accumulator += int(val)
        pos += 1
    if comm == 'jmp':
        pos += int(val)
    if comm == 'nop':
        pos += 1
    if pos in visited:
        break
    visited.add(pos)

print(accumulator)

# part 2


tried_to_switch = set()
success = False
while not success:
    accumulator = 0
    pos = 0
    visited = set()
    switched = False
    while True:
        if pos > len(inp):
            # by switching you might 'jump' out of range
            break
        elif pos == len(inp):
            print("SUCCESS!!!")
            print(accumulator)
            success = True
            break
        comm, val = inp[pos][0], inp[pos][1]
        if comm == 'acc':
            accumulator += int(val)
            pos += 1
        elif comm == 'jmp' and (pos in tried_to_switch or switched):
            pos += int(val)
        elif comm == 'jmp' and not switched:
            # do nop instead
            switched = True
            tried_to_switch.add(pos)
            pos += 1
        elif comm == 'nop' and (pos in tried_to_switch or switched):
            pos += 1
        elif comm == 'nop' and not switched:
            # do jmp instead
            switched = True
            tried_to_switch.add(pos)
            pos += int(val)
        if pos in visited:
            break
        visited.add(pos)
