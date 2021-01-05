import re

from collections import OrderedDict

file = open('input12.txt', encoding='utf8')
inp = file.read().strip()

pattern = re.compile(r'-?\d+')

all_nums = re.findall(pattern, inp)

solution = sum([int(i) for i in all_nums])

print("The solution to part 1 is:", solution)

# part 2

matches = re.finditer('red', inp)
to_redact = []
for m in matches:
    opened = 0
    closed = 0
    array_opened = 0
    array_closed = 0
    is_array = False
    start = m.start()
    end = m.end()
    for i, char in enumerate(inp[m.end():]):
        if closed - opened == 1:
            end = m.end() + i + 1
            break
        if char == '}':
            closed += 1
        elif char == '{':
            opened += 1
        elif char == ']':
            array_closed += 1
        elif char == '[':
            array_opened += 1
    for j, char in enumerate(inp[m.start()-1::-1]):
        if char == '{':
            opened += 1
            if opened - closed == 0:
                start = m.start() - j - 1
                break
        elif char == '}':
            closed += 1
        elif char == '[':
            array_opened += 1
            if array_opened - array_closed == 0:
                is_array = True
                break
        elif char == ']':
            array_closed += 1
    if not is_array:
        # starting from somewhere at the 10k-th index
        # my algo fails to find balanced brackets sometimes
        # I suspect it happens when the match starts inside an array
        if inp[end-1] != '}':
            continue
        to_redact.append((start, end))
# get rid of duplicates
to_redact = list(OrderedDict.fromkeys(to_redact))
print(to_redact)
# get rid of strings that are substrings of others
substrings = []
for i, (start, end) in enumerate(to_redact[:-1]):
    if start > to_redact[i+1][0]:
        substrings.append((start, end))
    # elif end < to_redact[i+1][1]:
    #     substrings.append((start, end))
print(len(to_redact), len(substrings))
print(substrings)
redact = [i for i in to_redact if i not in substrings]

redacted = list(inp)
for i in redact:
    for j in range(i[0], i[1]):
        redacted[j] = 'X'

all_nums_part2 = re.findall(pattern, ''.join(redacted))

solution_part2 = sum([int(i) for i in all_nums_part2])

print("The solution to part 2 is:", solution_part2)
