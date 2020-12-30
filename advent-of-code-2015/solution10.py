inp = '1113222113'

# don't do this, it literally takes half an hour to get to iter #50 with this
def part1(inp):
    #print("inp", inp)
    count = 1
    last_char = inp[0]
    new_seq = ''

    if len(inp) > 1:
        for i in range(1, len(inp)):
            if inp[i] == last_char:
                count += 1
            else:
                new_seq = new_seq + str(count) + last_char
                count = 1
            if i == len(inp)-1:
                new_seq = new_seq + str(count) + inp[i]

            last_char = inp[i]
        return new_seq
    return '1' + str(inp)

# do this because it just takes 5 seconds
def part1_faster(inp):
    count = 1
    new_seq = []

    if len(inp) > 1:
        for i in range(1, len(inp)):
            if inp[i] == inp[i-1]:
                count += 1
            else:
                new_seq.append(count)
                new_seq.append(inp[i-1])
                count = 1
            if i == len(inp)-1:
                new_seq.append(count)
                new_seq.append(inp[i])

        return new_seq
    return [1, inp[0]]

toy_inp = [1]
for i in range(5):
    toy_inp = part1_faster(toy_inp)
assert toy_inp == [3, 1, 2, 2, 1, 1]

inp = [int(i) for i in inp]
new_inp = inp
for i in range(50):
    if i == 40:
        print("The solution to part 1 is:", len(new_inp))
    new_inp = part1_faster(new_inp)

print("The solution to part 2 is:", len(new_inp))
