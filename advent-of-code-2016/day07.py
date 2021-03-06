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

def get_outer_inner(s):
    inside = False
    inner, outer = [], []
    subs = ''
    for n, char in enumerate(s):
        if char == '[':
            outer.append(subs)
            subs = ''
            inside = True
        elif char == ']':
            inner.append(subs)
            subs = ''
            inside = False
        else:
            subs = subs + char
            if n == len(s) - 1:
                outer.append(subs)
    return outer, inner

def part1(ips):
    tls_supported_ips = []
    for ip in ips:
        ans = False
        outer, inner = get_outer_inner(ip)
        #### this magically works
        if any(matches_abba(o) for o in outer):
            if not any(matches_abba(i.strip('[').strip(']')) for i in inner):
                ans = True
        #### end
        #### but this doesn't work??
        # for i in inner:
        #     if matches_abba(i.strip('[').strip(']')):
        #         break
        #     for o in outer:
        #         if matches_abba(o):
        #             ans = True
        #             break
        #### end
        tls_supported_ips.append(ans)

    return tls_supported_ips

assert part1(TOY) == [True, False, False, True], part1(TOY)
print("The solution to part 1 is:", sum(part1(inp)))

TOY2 = ["aba[bab]xyz",
        "xyx[xyx]xyx",
        "aaa[kek]eke",
        "zazbz[bzb]cdb"]

def matches_aba(s):
    m = []
    if len(s) < 3:
        return []
    for i in range(0, len(s)-2):
        if s[i] == s[i+2]:
            m.append(s[i:i+3])
    return m

def part2(ips):
    ssl_supported_ips = []
    for ip in ips:
        ans = False
        outer, inner = get_outer_inner(ip)
        o_matches = []
        for o in outer:
            m = matches_aba(o)
            if m:
                o_matches += m
        for i in inner:
            for om in o_matches:
                if om[1] + om[0] + om[1] in i:
                    ans = True
        ssl_supported_ips.append(ans)
    return ssl_supported_ips

assert part2(TOY2) == [True, False, True, True], part2(TOY2)
print("The solution to part 2 is:", sum(part2(inp)))
