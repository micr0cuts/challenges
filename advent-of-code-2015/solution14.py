reindeers = []
speeds = []
durs = []
rest = []
distances = []

with open('input14.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip().split()
        reindeers.append(line[0])
        speeds.append(int(line[3]))
        durs.append(int(line[6]))
        rest.append(int(line[-2]))

print(reindeers, speeds, durs, rest)

def solve(r, s, d, rest):
    t = 0
    dist = 0
    broken = False
    while True:
        if broken:
            break
        for i in range(d):
            t += 1
            dist += s
            if t >= 2503:
                broken = True
                break
        for i in range(rest):
            t += 1
            if t >= 2503:
                broken = True
                break
    return dist

for r, s, d, rest in zip(reindeers, speeds, durs, rest):
    distances.append(solve(r, s, d, rest))
print("The solution to part 1 is:", max(distances))
