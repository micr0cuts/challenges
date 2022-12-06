from typing import List

from lib import inputgetter_list

inp: List = inputgetter_list('inputs/02.txt')
tests: List = inputgetter_list('tests/02.txt')
inp = [x.split() for x in inp]
tests = [x.split() for x in tests]

determine_score = {
    "A": {"X": 3,
          "Y": 6,
          "Z": 0},
    "B": {"X": 0,
          "Y": 3,
          "Z": 6},
    "C": {"X": 6,
          "Y": 0,
          "Z": 3}
}

selection_score = {"X": 1, "Y": 2, "Z": 3}

win_score = {"X": 0, "Y": 3, "Z": 6}

def determine_win_part2(a: str, b: str) -> str:
    if b == "X":
        if a == "A":
            return "Z"
        if a == "B":
            return "X"
        if a == "C":
            return "Y"
    if b == "Y":
        if a == "A":
            return "X"
        if a == "B":
            return "Y"
        if a == "C":
            return "Z"
    if b == "Z":
        if a == "A":
            return "Y"
        if a == "B":
            return "Z"
        if a == "C":
            return "X"

def solve(inp: List[List[str]]) -> int:
    my_score = 0
    for opponent, my_choice in inp:
        my_score += determine_score[opponent][my_choice]
        my_score += selection_score[my_choice]
    return my_score

def solve2(inp: List[List[str]]) -> int:
    my_score = 0
    for opponent, end_result in inp:
        my_choice = determine_win_part2(opponent, end_result)
        my_score += win_score[end_result]
        my_score += selection_score[my_choice]
    return my_score

test_solution = solve(tests)
assert test_solution == 15
solution1 = solve(inp)
print(f"The solution to part 1 is: {solution1}")

test_solution2 = solve2(tests)
assert test_solution2 == 12
solution2 = solve2(inp)
print(f"The solution to part 2 is: {solution2}")
