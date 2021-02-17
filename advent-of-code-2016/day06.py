from collections import Counter
from operator import itemgetter

TOY = ["eedadn", "drvtee", "eandsr", "raavrd",
       "atevrs", "tsrnev", "sdttsa", "rasrtv",
       "nssdts", "ntnada", "svetve", "tesnvt",
       "vntsnd", "vrdear", "dvrsen", "enarar"]

TOY = [list(i) for i in TOY]

inp = [list(line.strip()) for line in open('input06.txt', encoding='utf8').readlines()]

def solve(messages, part2=False):
    password = ''
    transposed_strings = [[] for i in range(len(messages[0]))]
    for pos in range(len(messages[0])):
        for m in messages:
            transposed_strings[pos].append(m[pos])
    counters = [Counter(transposed_strings[pos]) for pos in range(len(messages[0]))]
    for c in counters:
        password += sorted(c.items(), key=itemgetter(1), reverse=(not part2))[0][0]
    return password

assert solve(TOY) == "easter"
print("The solution to part 1 is:", solve(inp))

assert solve(TOY, part2=True) == "advent"
print("The solution to part 2 is:", solve(inp, part2=True))
