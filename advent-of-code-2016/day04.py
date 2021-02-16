import re
from collections import Counter
from string import ascii_lowercase

inp = [line.strip() for line in open('input04.txt', encoding='utf8').readlines()]

TOY = ["aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]"]

def validate_room(room):
    front, checksum = room.split('[')
    checksum = checksum.replace(']', '')
    room_name = ''.join(front.split('-')[:-1])
    c = Counter(room_name)
    sorted_top5 = sorted(c.items(), key=lambda item: (-item[1], item[0]))[:5]
    if checksum == ''.join(i[0] for i in sorted_top5):
        return True
    return False

def get_sector_id(room):
    sector_id = room.split('[')[0].split('-')[-1]
    return int(sector_id)

def part1(rooms):
    ans = 0
    for r in rooms:
        if validate_room(r):
            ans += get_sector_id(r)
    return ans

assert part1(TOY) == 1514
print("The solution to part 1 is:", part1(inp))

char2num = {}
num2char = {}

for num, char in enumerate(ascii_lowercase):
    char2num[char] = num
    num2char[num] = char

def shift_cipher(room, s_id):
    front, _ = room.split('[')
    room_name = ' '.join(front.split('-')[:-1])
    decrypted = []
    for char in room_name:
        if char == ' ':
            decrypted.append(' ')
            continue
        idx = (char2num[char] + s_id) % len(char2num.keys())
        decrypted_letter = num2char[idx]
        decrypted.append(decrypted_letter)
    return "".join(decrypted)

def part2(rooms):
    for r in rooms:
        if validate_room(r):
            sector_id = get_sector_id(r)
            decrypted_name = shift_cipher(r, sector_id)
            # northpole... really?
            if re.search("northpole object storage", decrypted_name):
                return sector_id
print("The solution to part 2 is:", part2(inp))
