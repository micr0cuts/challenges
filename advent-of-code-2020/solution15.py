from collections import defaultdict

inp = [13, 0, 10, 12, 1, 5, 8]
toy_inp = [0, 3, 6]


def part1(inp, r=2020):
    ledger = defaultdict(list)
    for turn, number in enumerate(inp, 1):
        ledger[number].append(turn)
    for turn in range(len(inp) + 1, r+1):
        if number not in ledger.keys() or len(ledger[number]) == 1:
            ledger[0].append(turn)
            number = 0
        else:
            ans = ledger[number][-1] - ledger[number][-2]
            ledger[ans].append(turn)
            number = ans
    return number

assert part1(toy_inp) == 436, part1(toy_inp)

print("Solution to part 1 is:", part1(inp))

print("Solution to part 2 is:", part1(inp, r=30000000))
