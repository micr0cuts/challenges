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
    print("in function", equation)
    no_spaces = re.sub(' ', '', equation)
    solution = no_spaces[0]
    for i in range(1, len(no_spaces), 2):
        # this doesn't work for integers over 9... because of len()
        #probably better to rewrite it and use a list of strings instead?
        solution = eval(''.join([str(solution), no_spaces[i], no_spaces[i+1]]))
    return str(solution)

def part1(inp):
    solved_equations = []
    for equation in inp:
        equation = re.sub(' ', '', equation)

        brackets = find_brackets(equation)
        new_equation = equation
        for bracket in brackets:
            sub_equation = new_equation[bracket[0]+1:bracket[1]]
            print(new_equation)
            assert bracket_free(sub_equation), sub_equation
            partial_solution = solve_one_by_one(sub_equation)
            
            new_equation = new_equation[:bracket[0]] + partial_solution + ' '*len(range(bracket[0], bracket[1]+1-len(partial_solution))) + new_equation[bracket[1]+1:]
            assert len(equation) == len(new_equation)

        assert bracket_free(new_equation)
        print("equation", equation)
        print("new_equation", new_equation)
        solved_equations.append(int(solve_one_by_one(new_equation)))
    return sum(solved_equations)

assert part1(toy_cases) == sum(toy_answers)
print("The solution for part 1 is:", part1(inp))
