#!/usr/bin/env python3

inp = []
with open('input09.txt', encoding='utf8') as f:
    for line in f:
        inp.append(line.strip())

TESTS = {
    'ADVENT': 6,
    'A(1x5)BC': 7,
    '(3x3)XYZ': 9,
    'A(2x2)BCD(2x2)EFG': 11,
    '(6x1)(1x3)A': 6,
    'X(8x2)(3x3)ABCY': 18
    }

def parse_marker(marker):
    width, reps = marker.split('x')
    return int(width), int(reps)

def solve_decompression(inp_to_repeat, repeats):
    decompression = []
    for _ in range(repeats):
        for char in inp_to_repeat:
            decompression.append(char)
    return decompression

def solve(compressed_input):
    decompressed = []
    inside_marker = False
    marker_content = []
    decompression = []
    width, reps = 0, 0
    for idx, char in enumerate(compressed_input):
        if width > 0:
            # use this as a skip mechanism
            width -= 1
            continue
        elif inside_marker:
            if char != ')':
                marker_content.append(char)
            else:
                width, reps = parse_marker(''.join(marker_content))
                start = idx + 1
                end = start + width
                # idea for part 2: recurse here
                # while interim_decompressed still contains a match for r'\(\d+x\d+\)'
                interim_decompressed = solve_decompression(compressed_input[start:end], reps)
                decompressed.extend(interim_decompressed)
                marker_content = []
                inside_marker = False

        else:
            if char == '(':
                inside_marker = True
                continue
            decompressed.append(char)

    return decompressed, len(decompressed)

for test_string, test_answer in TESTS.items():
    #print("Testing: ", test_string, test_answer)
    #print(solve(test_string))
    assert solve(test_string)[1] == test_answer, solve(test_string)

_, solution1 = solve(''.join(inp))
print(f"The solution to part1 is: {solution1}")
