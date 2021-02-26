from day2 import calculate_paper_and_ribbon_needed

total_paper = 0
total_ribbon = 0

inp = [line.strip() for line in open('input02.txt', encoding='utf8')]

for i in inp:
    l, w, h = [int(x) for x in i.split('x')]
    results = calculate_paper_and_ribbon_needed(l, w, h)
    total_paper += results[0]
    total_ribbon += results[1]

print("Solution for part1:", total_paper)
print("Solution for part2:", total_ribbon)
