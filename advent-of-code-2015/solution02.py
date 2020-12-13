inp = [line.strip() for line in open('input02.txt', encoding='utf8')]

total_paper = 0
total_ribbon = 0

def calculate_paper_and_ribbon_needed(l, w, h):
    side1 = l*w
    side2 = w*h
    side3 = h*l
    ribbon = l*w*h + 2*sum(sorted([l, w, h])[:2])
    paper = 2*side1+2*side2+2*side3+min([side1, side2, side3])
    return (paper, ribbon)

for i in inp:
    l, w, h = [int(x) for x in i.split('x')]
    results = calculate_paper_and_ribbon_needed(l, w, h)
    total_paper += results[0]
    total_ribbon += results[1]

print("Solution for part1:", total_paper)
print("Solution for part2:", total_ribbon)
