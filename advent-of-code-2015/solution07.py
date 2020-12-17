import re
inp = [line.strip() for line in open('input07.txt', encoding='utf8')]

queue = []
registry = {}
start = ''
for line in inp:
    if line.endswith('a'):
        start = line
    else:
        queue.append(line)
queue.insert(0, start)

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
        elif not registry.get(instr[0]):
            # not sure about this one, what should happen for cases like "lx -> a"
            return False
        else:
            registry[k] = registry[instr[0]]
    if len(instr) == 2:
        if not registry.get(obj):
            return False
        if operator == 'NOT':
            registry[k] = ~registry[obj]
            return True
        raise Exception
    if len(instr) == 3:
        if not all([subject, operator, obj]) or not registry.get(subject):
            return False
        if registry.get(obj):
            if operator == 'AND':
                registry[k] = registry[subject] & registry[obj]
            elif operator == 'OR':
                registry[k] = registry[subject] | registry[obj]
        elif instr[-1].isnumeric(): 
            if operator == 'LSHIFT':
                registry[k] = registry[subject] << int(instr[-1])
            elif operator == 'RSHIFT':
                registry[k] = registry[subject] >> int(instr[-1])

        return True
    else:
        raise Exception

while not registry.get('a'):
    print("queue", queue[0])
    if not evaluate_instruction(queue[0], registry):
        queue.append(queue[0])
    queue.pop(0)
    print(registry)

print("Solution to part 1 is: ", registry['a'])

