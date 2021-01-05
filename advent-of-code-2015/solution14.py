from collections import defaultdict

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

def solve(s, d, rest, part2=False):
    t = 0
    dist = 0
    times_up = False
    while True:
        if times_up:
            break
        for i in range(d):
            t += 1
            dist += s
            if t >= 2503:
                times_up = True
                break
            if part2:
                yield dist
        for i in range(rest):
            t += 1
            if t >= 2503:
                times_up = True
                break
            if part2:
                yield dist
    yield dist

for s, d, r in zip(speeds, durs, rest):
    distances += solve(s, d, r, part2=False)

print("The solution to part 1 is:", max([i for i in distances]))

points = [0 for r in reindeers]
distances = defaultdict(list)

for r, s, d, rest in zip(reindeers, speeds, durs, rest):
    distances[r] += solve(s, d, rest, part2=True)

for i in range(2503):
    values = [
              distances[reindeers[0]][i],
              distances[reindeers[1]][i],
              distances[reindeers[2]][i],
              distances[reindeers[3]][i],
              distances[reindeers[4]][i],
              distances[reindeers[5]][i],
              distances[reindeers[6]][i],
              distances[reindeers[7]][i],
              distances[reindeers[8]][i]
              ]
    leaders = []
    highest = 0
    for i, val in enumerate(values):
        if val > highest:
            highest = val
            leaders = [i]
        elif val == highest:
            leaders.append(i)
    for l in leaders:
        points[l] += 1

print("The solution to part 2 is:", max(points))
