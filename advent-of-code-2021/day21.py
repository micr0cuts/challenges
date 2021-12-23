positions = {}
scores = {}
test_positions = {}
test_scores = {}
board = list(range(1,11))
with open('inputs/21.txt', encoding='utf8') as f:
    for i, line in enumerate(f, 1):
        line = line.strip().split()
        player = int(line[1])
        positions[player] = int(line[-1])
        scores[player] = 0

with open('tests/21.txt', encoding='utf8') as f:
    for i, line in enumerate(f, 1):
        line = line.strip().split()
        player = int(line[1])
        test_positions[player] = int(line[-1])
        test_scores[player] = 0

print(test_positions, test_scores)

def solve(p, s, b):
    i = 1
    dicerolls = 0
    player = min(s.keys())
    while max(s.values()) < 1000:
        for _ in range(3):
            p[player] += i
            print(player, i, p)
            i += 1
            if i == 101:
                i = 1
                dicerolls += 100
            if p[player] > 10:
                if p[player] % 10 != 0:
                    p[player] = p[player] % 10
                else:
                    p[player] = 10
        s[player] += p[player]
        print('s', s)
        player = 1 if player == 2 else 2
    print(dicerolls, i)
    return min(s.values())*(i-1+dicerolls)

test_solution = solve(test_positions, test_scores, board)
print(test_solution)
assert test_solution == 739785
solution1 = solve(positions, scores, board)
print(f'The solution to part 1 is : {solution1}')
