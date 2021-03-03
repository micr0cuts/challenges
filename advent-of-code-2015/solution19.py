from collections import defaultdict

replacements, molecule = open('input19.txt', encoding='utf8').read().split('\n\n')
molecule = molecule.strip()

reps = defaultdict(list)
for r in replacements.split('\n'):
    k,v = r.split('=>')
    reps[k.strip()].append(v.strip())

def parse_molecule(m, replaceables):
    parsed_molecule = []
    tmp = ''
    for char in m:
        if char in replaceables:
            if tmp:
                parsed_molecule.append(tmp)
                tmp = ''
            parsed_molecule.append(char)
        else:
            tmp += char
            if tmp in replaceables:
                parsed_molecule.append(tmp)
                tmp = ''
            if tmp[-2:] in replaceables:
                parsed_molecule.append(tmp[:-2])
                parsed_molecule.append(tmp[-2:])
                tmp = ''

    return parsed_molecule

TOY = {'H': ['HO', 'OH'],
       'O': ['HH']}

def solve(replace_dict, m):
    new_molecules = set()
    for pos, i in enumerate(m):
        if i in replace_dict.keys():
            for v in replace_dict[i]:
                new_molecule = [x for x in m]
                new_molecule[pos] = v
                new_molecules.add(''.join(new_molecule))
    return len(new_molecules)

parsed_molecule = parse_molecule(molecule, reps.keys())
assert solve(TOY, list('HOH')) == 4
assert solve(TOY, list('HOHOHO')) == 7, solve(TOY, list('HOHOHO'))
print("The solution to part 1 is:", solve(reps, parsed_molecule))
