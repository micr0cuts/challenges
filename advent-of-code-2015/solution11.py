import string
import re

inp = 'hxbxwxba'
a = list(string.ascii_lowercase)
ALPHA2NUM = {}
for i, char in enumerate(a, 1):
    ALPHA2NUM[char] = i

NUM2ALPHA = {v:k for k, v in ALPHA2NUM.items()}

PAIR = re.compile(r'(\w)\1')
INCREASING_STRAIGHTS = []
for i in range(len(a)-3):
    INCREASING_STRAIGHTS.append(''.join(a[i:i+3]))

def validate_password(password):
    forbidden = ['i', 'o', 'l']
    for char in forbidden:
        if char in password:
            return False

    o = re.findall(PAIR, password)
    if len(set(o)) < 2:
        return False

    for s in INCREASING_STRAIGHTS:
        if s in password:
            return True

    return False

def increment_password(old_pass):
    new_pass = old_pass
    for i, char in enumerate(old_pass[::-1]):
        charnum = ALPHA2NUM[char]
        if charnum == 26:
            new_pass = new_pass[:-i] + 'a'
            if validate_password(new_pass):
                return new_pass
            continue
        else:
            increased = NUM2ALPHA[charnum + 1]
            new_pass = new_pass[:-i] + increased
            if validate_password(new_pass):
                return new_pass

print("The solution to part 1 is:", increment_password(inp))
