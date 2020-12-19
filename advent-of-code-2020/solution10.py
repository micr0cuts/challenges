from collections import defaultdict

inp = sorted([int(i.strip()) for i in open('input10toy.txt', encoding='utf8').readlines()])

differences = []

# accounting for the jump from 0 jolts to the first adapter
differences.append(inp[0])

for i in range(1, len(inp)):
    diff = inp[i] - inp[i-1]
    assert diff in [1, 2, 3]
    differences.append(inp[i] - inp[i-1])
# accounting for the "always three higher than the highest one"
differences.append(3)
ones = differences.count(1)
threes = differences.count(3)
print(ones * threes)

# part 2

inp.insert(0, 0)
inp.append(inp[-1]+3)

# current state to possible transitions
d = defaultdict(list)
for i in inp:
    for j in inp:
        if j > i and j-i <= 3:
            d[i].append(j)
print(d)


# my borked attempt
# state to where could I possibly have come from
# tvartom = defaultdict(list)
# for k, v in d.items():
#     for i in v:
#         tvartom[i].append(k)
# print(tvartom)

# total = 0
# prev_k = 0
# prev_values = defaultdict(int)
# for k, v in sorted(d.items()):
#     prev_values[k] = total
#     if len(v) > 1:
#         total += prev_values[prev_k] +1 + len(v)
#         print(k, i, prev_values[prev_k], total)
#     prev_k = k
# print(total)
# gave up here

# Python translation of Marin's Java code
mymap = defaultdict(int)
sl = sorted(list(d.keys()))
mymap[0] = 1
for i in sl:
    for j in sl:
        if j > i:
            if j - i <= 3:
                mymap[j] += mymap[i]

print(mymap[max(mymap.keys())])
