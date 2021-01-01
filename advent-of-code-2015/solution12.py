import re

file = open('input12.txt', encoding='utf8').read()

pattern = re.compile(r'-?\d+')

all_nums = re.findall(pattern, file)

solution = sum([int(i) for i in all_nums])

print("The solution to part 1 is:", solution)
