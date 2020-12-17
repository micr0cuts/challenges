import re
inp = [line.strip() for line in open('input07.txt', encoding='utf8')]

queue = []
registry = {}
for line in inp:
    queue.append(line)

#print(queue)

def evaluate_instruction(line, registry):
    # returns False if an instruction is not able to solve at this point in time
    line = line.split('->')
    k = line[1].strip()
    instr = line[0].split()
    actions = r'(NOT|OR|LSHIFT|RSHIFT|AND)'
    subject = instr[0] if instr[0] not in actions else None
    print(instr, k, subject)
    x = re.search(actions, line[0])
    operator = x.group(0) if x else None
    obj = instr[-1] if len(instr) > 1 else None
    if len(instr) == 1:
        if instr[0].isnumeric():
            registry[k] = int(instr[0])
            return True
        else:
            # not sure about this one, what should happen for cases like "lx -> a"
            return False
    if len(instr) == 2:
        if not registry.get(obj):
            return False
        if operator == 'NOT':
            registry[k] = ~obj
            return True
        raise Exception
    if len(instr) == 3:
        if not all([subject, operator, obj]) or not registry.get(subject) or not registry.get(obj):
            return False
        elif operator == 'AND':
            registry[k] = registry[subject] & registry[obj]
        elif operator == 'LSHIFT':
            registry[k] = registry[subject] << registry[obj]
        elif operator == 'RSHIFT':
            registry[k] = registry[subject] >> registry[obj]
        elif operator == 'OR':
            registry[k] = registry[subject] | registry[obj]
        return True
    else:
        raise Exception

while not registry.get('a'):
    print("queue", queue[0])
    if not evaluate_instruction(queue[0], registry):
        queue.append(queue[0])
    queue.pop(0)

print("Solution to part 1 is: ", registry['a'])

