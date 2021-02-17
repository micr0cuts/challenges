import hashlib

door_id = "ojvtpuvg"

def part1(d):
    password = ''
    while True:
        x = d + str(n)
        m = hashlib.md5(x.encode('utf8')).hexdigest()
        if m.startswith("00000"):
            password = password + m[5]
            print(password, n, x, m)
            if len(password) == 8:
                return password

assert part1('abc') == "18f47a30"
print("The solution to part 1 is:", part1(door_id))

def part2(d):
    password = ["_" for i in range(8)]
    while True:
        x = d + str(n)
        m = hashlib.md5(x.encode('utf8')).hexdigest()
        if m.startswith("00000"):
            if m[5] in "01234567":
                pos = int(m[5])
                if password[pos] == "_":
                    password[pos] = m[6]
                    print(password, n, m)
                    if "_" not in password:
                        return ''.join(password)

print("The solution to part 2 is:", part2(door_id))
