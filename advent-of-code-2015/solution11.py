import string
import re

'''
This riddle has caused me a lot of confusion. I struggled a lot with getting the logic for next_password right
and my final code is pretty much copypasted from solutions found on Reddit and Github. 
I also noticed many comments saying that this was easier to solve by "reasoning" (i.e. doing it manually) than programming it,
which to a certain degree I agree with.
Many solutions I found online were pretty ugly and made assumptions that shouldn't be made in production code.
So I was striving to get the solution right without making too many assumptions.
Notwithstanding this problem isn't really realistic in the first place...
'''

inp = 'hxbxwxba'
a = list(string.ascii_lowercase)
ALPHA2NUM = {}
for i, char in enumerate(a, 1):
    ALPHA2NUM[char] = i

NUM2ALPHA = {v:k for k, v in ALPHA2NUM.items()}

PAIR = re.compile(r'(\w)\1')
INCREASING_STRAIGHTS = []
for i in range(len(a)-2):
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

def increment_letter(char):
    charnum = ALPHA2NUM[char]
    if charnum == 26:
        return 'a'
    else:
        return NUM2ALPHA[charnum+1]

def next_password(password):
    new_pass = password[:-1] + increment_letter(password[-1])

    for i in range(len(password)-1, -1, -1):
        if new_pass[i] == 'a':
            new_pass = new_pass[:i-1] + increment_letter(new_pass[i-1]) + new_pass[i:]
        else:
            break
    return new_pass

toy_passwords = ['hijklmmn', 'abbceffg', 'abbcegjk']
for p in toy_passwords:
    assert not validate_password(p)

password = inp
while not validate_password(password):
    password = next_password(password)

print("The solution to part 1 is:", password)
password = next_password(password)

while not validate_password(password):
    password = next_password(password)

print("The solution to part 2 is:", password)

