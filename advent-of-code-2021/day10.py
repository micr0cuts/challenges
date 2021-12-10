
from lib import inputgetter_list

sym2points = {')': 3, ']': 57, '}': 1197, '>': 25137}

close2open = {')': '(', ']': '[', '}': '{', '>': '<'}

open2close = {v: k for k, v in close2open.items()}

sym2points2 = {'(': 1, '[': 2, '{': 3, '<': 4}

inp = inputgetter_list('inputs/10.txt')

tests_inp = inputgetter_list('tests/10.txt')

opening = list(close2open.values())
closing = list(close2open.keys())

answers = 0
corrupted = set()
for i, line in enumerate(inp):
    opened = []
    for char in line.strip():
        if char in opening:
            opened.append(char)
        if char in closing:
            if char != open2close[opened[-1]]:
                #print("Bad line", i, line, char)
                answers += sym2points[char]
                corrupted.add(i)
                break
            else:
                opened.pop()
print(answers)

answers2 = []
for i, line in enumerate(inp):
    line_score = 0
    if i in corrupted:
        continue
    opened = []
    for char in line.strip():
        if char in opening:
            opened.append(char)
        if char in closing:
            if char == open2close[opened[-1]]:
                opened.pop()
    for char in opened[-1::-1]:
        line_score *= 5
        line_score += sym2points2[char]
    answers2.append(line_score)

answers2.sort()
middle = (len(answers2)//2)
print(answers2[middle])

