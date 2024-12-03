tests = []
with open('tests/02.txt', encoding='utf8') as f:
    for line in f:
        line = list(map(int, line.strip().split()))
        tests.append(line)

inp = []
with open('inputs/02.txt', encoding='utf8') as f:
    for line in f:
        line = list(map(int, line.strip().split()))
        inp.append(line)

def is_safe_with_one_removed(report: list[int]) -> bool:
    reports_with_one_skip = []
    for i in range(len(report)):
        new_report = []
        for j in range(len(report)):
            if i == j:
                continue
            new_report.append(report[j])
        reports_with_one_skip.append(new_report)

    for new_report in reports_with_one_skip:
        broken = False
        if sorted(new_report) == new_report:
            for i, j in zip(new_report, new_report[1:]):
                if j - i not in (1, 2, 3):
                    broken = True
                    break
            if not broken:
                return True
        elif sorted(new_report, reverse=True) == new_report:
            for i, j in zip(new_report, new_report[1:]):
                if i - j not in (1, 2, 3):
                    broken = True
                    break
            if not broken:
                return True
    return False

def solve(inp: list[list[int]], part2: bool = False) -> int:
    solution = 0
    for line in inp:
        broken = 0
        if sorted(line) == line:
            for i, j in zip(line, line[1:]):
                if j - i not in (1, 2, 3):
                    broken += 1
            if not broken:
                solution += 1
                continue

        elif sorted(line, reverse=True) == line:
            for i, j in zip(line, line[1:]):
                if i - j not in (1, 2, 3):
                    broken += 1
            if not broken:
                solution += 1
                continue
        if part2:
            is_fixable = is_safe_with_one_removed(line)
            solution += is_fixable
    return solution

assert solve(tests) == 2, solve(tests)
print(f'The solution to part 1 is: {solve(inp)}')
assert solve(tests, part2=True) == 4, solve(tests, part2=True)
print(f'The solutiont o part 2 is: {solve(inp, part2=True)}')
