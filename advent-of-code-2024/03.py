import re

tests = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
tests2 = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

inputs = []
with open('inputs/03.txt', encoding='utf8') as f:
    for line in f:
        inputs.append(line.strip())

def solve(inp, part2=False):
    solution = 0
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    if not part2:
        for line in inp:
            result = re.findall(pattern, line)
            for x, y in result:
                solution += int(x)*int(y)

        return solution

    pattern = r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)'
    do = True
    for line in inp:
        result = re.findall(pattern, line)
        for res in result:
            if res == 'do()':
                do = True
            elif res == "don't()":
                do = False
            elif res.startswith('mul('):
                m = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', res)
                if do:
                    solution += int(m.group(1)) * int(m.group(2))
    return solution

test_solution = solve(tests)
assert test_solution == 161

solution = solve(inputs)
print(f'The solution to part 1 is: {solution}')

test_solution2 = solve(tests2, part2=True)
assert test_solution2 == 48

solution2 = solve(inputs, part2=True)
print(f'The solution to part 2 is: {solution2}')
