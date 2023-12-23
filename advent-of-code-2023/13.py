# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
from copy import deepcopy
from typing import Generator
from typing import Iterator

with open('tests/13.txt', encoding='utf8') as f:
    contents = f.read()
tests = [x.split('\n') for x in contents.split('\n\n')]

with open('inputs/13.txt', encoding='utf8') as f:
    contents = f.read()
inp = [x.split('\n') for x in contents.split('\n\n')]

def make_int_list(x: list[str]) -> list[list[int]]:
    int_list: list[list[int]] = []
    for row in x:
        int_list.append([1 if char == '#' else 0 for char in row])
    return int_list

def make_smudges_shift(x: list[list[int]]) -> Generator:
    for i in range(len(x) * len(x[0])):
        shifted = deepcopy(x)
        x_coord = i % len(x)
        y_coord = i // len(x)
        value = x[x_coord][y_coord]
        shifted[x_coord][y_coord] = int(not value)
        yield deepcopy(shifted)

def is_reflection(i: int, x: Iterator[list[int]]) -> bool:
    upper = x[:i+1]
    lower = x[i+1:]
    for one, two in zip(upper[::-1], lower):
        if one != two:
            return False
    return True

def solve(input_list: list[list[str]]) -> tuple[int, dict[int, tuple[int, int]]]:
    reflection_idxs = {}
    score = 0
    for idx, x in enumerate(input_list):
        l = make_int_list(x)
        transpose = list(map(list, zip(*l)))
        # flipped_idx represents whether it's a horizontal or vertical mirroring
        for flipped_idx, iterable in enumerate((l, transpose)):
            for i, (line1, line2) in enumerate(zip(iterable, iterable[1:])):
                if line1 == line2:
                    if is_reflection(i, iterable):
                        score += (i + 1) * (100 if flipped_idx == 0 else 1)
                        reflection_idxs[idx] = (flipped_idx, i)
                        break

    return score, reflection_idxs

def solve2(input_list: list[list[str]], refl_idxs: dict[int, tuple[int, int]]) -> int:
    score = 0
    for idx, x in enumerate(input_list):
        l = make_int_list(x)
        shifted_ls = make_smudges_shift(l)
        is_broken = False
        for smudged in shifted_ls:
            if is_broken:
                is_broken = False
                break
            transpose = list(map(list, zip(*smudged)))
            for flipped_idx, iterable in enumerate((smudged, transpose)):
                if is_broken:
                    break
                for i, (line1, line2) in enumerate(zip(iterable, iterable[1:])):
                    if line1 == line2:
                        if is_reflection(i, iterable):
                            if refl_idxs[idx] != (flipped_idx, i):
                                score += (i + 1) * (100 if flipped_idx == 0 else 1)
                                is_broken = True
                                break
    return score

test_solution, test_r_idxs = solve(tests)
assert test_solution == 405, solve(tests)
solution , r_idxs = solve(inp)
print(f'The solution for part 1 is: {solution}')

assert solve2(tests, test_r_idxs) == 400, solve2(tests, test_r_idxs)
print(f'The solution for part 2 is: {solve2(inp, r_idxs)}')
