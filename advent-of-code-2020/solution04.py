import re
from collections import defaultdict

inp = []
passport = []

inp = open('input04.txt', encoding='utf8').readlines()

passport_list = [row.strip() for row in inp]
passports = defaultdict(dict)

num_passports = 1
for line in passport_list:
    if line:
        for item in line.split():
            key, value = item.split(':')
            passports[num_passports][key] = value
    else:
        num_passports += 1

# part 1

mandatory_values = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valids = 0
valid_passports = defaultdict(dict)

for p in passports:
    if set(passports[p].keys()) >= mandatory_values:
        valids +=1
        valid_passports[p] = passports[p]

print(valids)

# part 2

def verify_passport(passport_dict): 
    if not (int(passport_dict['byr']) >= 1920 and int(passport_dict['byr']) <= 2002):
        return False
    if not (int(passport_dict['iyr']) >= 2010 and int(passport_dict['iyr']) <= 2020):
        return False
    if not (int(passport_dict['eyr']) >= 2020 and int(passport_dict['eyr']) <= 2030):
        return False
    hgt_match = re.match(r'^\d+(cm|in)$', passport_dict['hgt'])
    if hgt_match:
        pass
        #print(hgt_match.group((0)))
    if not hgt_match:
        #print(passport_dict['hgt'])
        return False
    else:
        match = hgt_match.group(0)
        #print("first", match)
        if match.endswith('cm'):
            if (int(match.split('cm')[0]) < 150 or int(match.split('cm')[0]) > 193):
                #print(int(match.split('cm')[0]))
                return False
        elif match.endswith('in'):
            if (int(match.split('in')[0]) < 59 or int(match.split('in')[0]) > 76):
                return False
    #print("second", match)
    if not re.match(r'#[0-9a-f]{6}', passport_dict['hcl']):
        return False
    if passport_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.match(r'^[0-9]{9}$', passport_dict['pid']):
        return False
    return True


valids = 0
for p in valid_passports.values():
    if verify_passport(p):
        valids += 1
print(valids)
