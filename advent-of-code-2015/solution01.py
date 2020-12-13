floor = 0

inp = ''
for line in open('input01.txt', encoding='utf8'):
    line = line.strip()
    inp = inp + line

part2_done = False

for i, char in enumerate(inp, 1):
    assert char in ['(', ')']
    if char == ')':
        floor -= 1
    else:
        floor += 1
    if floor == -1 and not part2_done:
        print("Solution for part2:", i)
        part2_done = True

print("Solution for part 1:", floor)
