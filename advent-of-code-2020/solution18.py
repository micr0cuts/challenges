import re

toy_cases = ["1 + 2 * 3 + 4 * 5 + 6",
             "1 + (2 * 3) + (4 * (5 + 6))",
             "2 * 3 + (4 * 5)",
             "5 + (8 * 3 + 9 + 3 * 4 * 3)",
             "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
             "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
            ]
toy_answers = [71, 51, 26, 437, 12240, 13632]

inp = [line.strip() for line in open('input18.txt', encoding='utf8')]

def bracket_free(equation):
    return not any(c in ['(', ')'] for c in equation)

def find_brackets(equation):
    '''
    given an equation that contains brackets
    return a list of tuples with all bracket pairs
    '''
    bracket_pos = []
    opened = []
    for i, c in enumerate(equation):
        if c == '(':
            opened.append(i)
        elif c == ')':
            b = (opened.pop(), i)
            bracket_pos.append(b)
    return bracket_pos

def solve_one_by_one(equation):
    no_spaces = [i for i in equation if i != '']
    solution = no_spaces[0]
    for i in range(1, len(no_spaces), 2):
        # this doesn't work for integers over 9... because of len()
        #probably better to rewrite it and use a list of strings instead?
        solution = eval(''.join([str(solution), no_spaces[i], no_spaces[i+1]]))
    return str(solution)

def part1(inp):
    solved_equations = []
    for equation in inp:
        if type(equation) == str:
            equation = list(re.sub(' ', '', equation))

        brackets = find_brackets(equation)
        new_equation = equation
        for bracket in brackets:
            sub_equation = new_equation[bracket[0]+1:bracket[1]]
            assert bracket_free(sub_equation), sub_equation
            partial_solution = solve_one_by_one(sub_equation)
            
            new_equation = new_equation[:bracket[0]] + [partial_solution] + [' ' for i in range(bracket[0], bracket[1])] + new_equation[bracket[1]+1:]
            assert len(equation) == len(new_equation)

        assert bracket_free(new_equation), new_equation

        solved_equations.append(int(solve_one_by_one(new_equation)))
    return sum(solved_equations)

assert part1(toy_cases) == sum(toy_answers)
print("The solution for part 1 is:", part1(inp))

# part 2
toy_answers2 =  [231, 51, 46, 1445, 669060, 23340]

def add_brackets(equation):

    plusses = [i for i, c in enumerate(equation) if c == '+']
    for idx in plusses:
        insert = []
        opened = 0
        # search left
        for i, c in enumerate(equation[idx-1::-1]):
            if c == ')':
                opened -= 1
            elif c == '(':
                opened += 1
            if opened == 0:
                insert.append(idx-i+len(insert))
                break
        # search right
        assert len(insert) % 2 == 1
        assert opened == 0
        for i, c in enumerate(equation[idx+1:]):
            if c == '(':
                opened += 1
            elif c == ')':
                opened -= 1
            if opened == 0:
                if equation[i+1] == '+':
                    continue
                insert.append(i+idx+1+len(insert))
                break


    # for i, c in enumerate(equation):
    #     if c.isnumeric() and len(insert) %2 == 1:
    #         insert.append(i+1+len(insert))
    #     elif c == '+' and not opened:
    #         if equation[i-1].isnumeric():
    #             insert.append(i-1+len(insert))
    #     elif c == '(' and insert:
    #         opened += 1
    #     elif c == ')' and insert:
    #         opened -= 1
    #         if opened == 0 and len(insert) % 2 == 1:
    #             insert.append(i+1+len(insert))
    opening = True
    print(insert)
    for i in insert:
        if opening:
            equation.insert(i, '(')
        else:
            equation.insert(i, ')')
        opening = not opening
    return equation

def part2(inp):
    new_inp = [add_brackets(list(re.sub(' ', '', equation))) for equation in inp]
    print(new_inp)
    return part1(new_inp)


assert part2(toy_cases) == sum(toy_answers2)
print("The solution for part 2 is:", part2(inp))
