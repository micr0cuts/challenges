import re

inp = [line.strip() for line in open('input07.txt', encoding='utf8')]

TOY = ["abba[mnop]qrst",
       "abcd[bddb]xyyx",
       "aaaa[qwer]tyui",
       "ioxxoj[asdfgh]zxcvbn"]

def matches_abba(s):
    if len(s) < 4:
        return False
    for i in range(0, len(s)-3):
        if s[i] == s[i+3]:
            if s[i+1] == s[i+2]:
                return s[i] != s[i+1]
    return False

def part1(ips):
    tls_supported_ips = []
    for ip in ips:
        ans = False
        in_brackets = re.findall('\\[.*?\\]', ip)
        for i in in_brackets:
            if matches_abba(i.strip('[').strip(']')):
                break
            outside_brackets = re.findall('(^[a-zA-Z]*)', ip)
            outside_brackets += re.findall('(?<=\\])([a-zA-Z]*)', ip)
            for o in outside_brackets:
                if matches_abba(o):
                    ans = True
                    break
        tls_supported_ips.append(ans)
    return tls_supported_ips

assert part1(TOY) == [True, False, False, True], part1(TOY)
print("The solution to part 1 is:", sum(part1(inp)))
