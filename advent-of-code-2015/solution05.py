import re
from collections import Counter

inp = [line.strip() for line in open('input05.txt', encoding='utf8').readlines()]

nice = 0
better_nice = 0
vowels = {'a', 'e', 'i', 'o', 'u'}

def check_niceness(string):
    c = Counter(line)
    num_vowels = sum([c[v] for v in vowels])
    if num_vowels < 3:
        return False
    for bad in ['ab', 'cd', 'pq', 'xy']:
        if bad in line:
            return False
    prev_char = ''
    for char in line:
        if char == prev_char:
            return True
        prev_char = char
    return False

pattern1 = r'(\w\w).*?(\1)'
pattern2 = r'(\w)(\w)(\1)'

def check_better_niceness(string):
    if re.search(pattern1, string):
        if re.search(pattern2, string):
            return True

for line in inp:
    if check_niceness(line):
        nice += 1
    if check_better_niceness(line):
        better_nice += 1

print("Solution for part1:", nice)
print("Solution for part2:", better_nice)
