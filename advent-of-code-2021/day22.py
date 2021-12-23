import re
from collections import defaultdict

commands = []
test_commands = []
test_commands2 = []

with open('inputs/22.txt', encoding='utf8') as f:
    for line in f:
        cmd = 0 if line.split()[0] == 'off' else 1
        m = re.match(r'(.*)x=(-?\d+)\.\.(-?\d+)', line)
        x_min = int(m.group(2))
        x_max = int(m.group(3))

        m = re.match(r'(.*)y=(-?\d+)\.\.(-?\d+)', line)
        y_min = int(m.group(2))
        y_max = int(m.group(3))

        m = re.match(r'(.*)z=(-?\d+)\.\.(-?\d+)', line)
        z_min = int(m.group(2))
        z_max = int(m.group(3))
        commands.append([cmd, x_min, x_max, y_min, y_max, z_min, z_max])

with open('tests/22.txt', encoding='utf8') as f:
    for line in f:
        cmd = 0 if line.split()[0] == 'off' else 1
        m = re.match(r'(.*)x=(-?\d+)\.\.(-?\d+)', line)
        x_min = int(m.group(2))
        x_max = int(m.group(3))

        m = re.match(r'(.*)y=(-?\d+)\.\.(-?\d+)', line)
        y_min = int(m.group(2))
        y_max = int(m.group(3))

        m = re.match(r'(.*)z=(-?\d+)\.\.(-?\d+)', line)
        z_min = int(m.group(2))
        z_max = int(m.group(3))
        test_commands.append([cmd, x_min, x_max, y_min, y_max, z_min, z_max])

with open('tests/22_2.txt', encoding='utf8') as f:
    for line in f:
        cmd = 0 if line.split()[0] == 'off' else 1
        m = re.match(r'(.*)x=(-?\d+)\.\.(-?\d+)', line)
        x_min = int(m.group(2))
        x_max = int(m.group(3))

        m = re.match(r'(.*)y=(-?\d+)\.\.(-?\d+)', line)
        y_min = int(m.group(2))
        y_max = int(m.group(3))

        m = re.match(r'(.*)z=(-?\d+)\.\.(-?\d+)', line)
        z_min = int(m.group(2))
        z_max = int(m.group(3))
        test_commands2.append([cmd, x_min, x_max, y_min, y_max, z_min, z_max])

def solve(cmds, part2=False):
    cubes = defaultdict(int)
    for instructions in cmds:
        if all(i >= -50 and i <= 50 for i in instructions[1:]) or part2:
            cmd, x1, x2, y1, y2, z1, z2 = instructions
            assert x1 <= x2
            assert y1 <= y2
            assert z1 <= z2
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    for z in range(z1, z2+1):
                        cubes[(x, y, z)] = cmd

    print(cubes[(21291, -33476, 38147)])
    solution = sum(cubes.values())

    if not part2:
        solution = 0
        for (x, y, z), val in cubes.items():
            if all(i <= 50 and i >= -50 for i in [x, y, z]):
                solution += val

    return solution

test_solution = solve(test_commands, part2=False)
print(test_solution)
assert test_solution == 590784
solution1 = solve(commands, part2=False)
print(f'The solution to part 1 is: {solution1}')

print(test_commands2)
test_solution2 = solve(test_commands2, part2=True)
print(test_solution2)
assert test_solution2 == 2758514936282235
solution2 = solve(commands, part2=True)
print(f'The solution to part 2 is: {solution2}')
