from copy import deepcopy

inp = [line.strip().split() for line in open('input08.txt', encoding='utf8')]

TOY = ["rect 3x2".strip().split(),
       "rotate column x=1 by 1".strip().split(),
       "rotate row y=0 by 4".strip().split(),
       "rotate column x=1 by 1".strip().split()]

TOY_SCREEN = []
screen = []

for row in range(3):
    row = []
    for col in range(7):
        row.append(0)
    TOY_SCREEN.append(row)

for row in range(6):
    row = []
    for col in range(50):
        row.append(0)
    screen.append(row)

def format_input(inp):
    out = []
    for line in inp:
        if line[0] == 'rect':
            x, y = line[1].split('x')
            out.append(['rect', int(x), int(y)])
        elif line[0] == 'rotate':
            out.append([line[1], int(line[2].split('=')[1]), int(line[4])])

    return out

def part1(screen, inp):
    for instr, x, y in inp:
        new_screen = deepcopy(screen)
        if instr == 'rect':
            for a in range(x):
                for b in range(y):
                    new_screen[b][a] = 1
        elif instr == 'row':
            l = len(new_screen[x])
            new_row = [-1 for i in range(l)]
            for i in range(l):
                new_row[(i+y)%l] = screen[x][i]
            new_screen[x] = new_row
        elif instr == 'column':
            l = len(new_screen)
            for i in range(l):
                new_screen[(i+y)%l][x] = screen[i][x]
        else:
            raise Exception("This shouldn't happen", print(instr))
        screen = new_screen

    return screen

TOY = format_input(TOY)
inp = format_input(inp)

assert sum([sum(l) for l in part1(TOY_SCREEN, TOY)]) == 6
solution = part1(screen, inp)
print("The solution to part 1 is:", sum([sum(l) for l in solution]))
for line in solution:
    print("".join(map(str, line)).replace("1", "|").replace("0", " "))
