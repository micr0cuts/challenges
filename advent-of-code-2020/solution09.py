import sys

inp = [int(i) for i in open('input09.txt', encoding='utf8').readlines()]

def calculate_sums(inputs):
    return {inputs[i]+inputs[j] for i in range(len(inputs)) for j in range(len(inputs)) if i != j}

for i in range(len(inp)-25):
    valid_sums = calculate_sums(inp[i:i+25])
    if inp[i+25] not in valid_sums:
        invalid_num = inp[i+25]
        print(invalid_num)
        break

# part 2

for i, val in enumerate(inp):
    contiguous_numbers = [val]
    for val2 in inp[i+1:]:
        the_sum = sum(contiguous_numbers) + val2
        if the_sum > invalid_num:
            break
        elif the_sum == invalid_num:
            contiguous_numbers.append(val2)
            print(min(contiguous_numbers) + max(contiguous_numbers))
            sys.exit()
        else:
            contiguous_numbers.append(val2)
