# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
from lib import inputgetter_list

tests = inputgetter_list('tests/11.txt')
inp = inputgetter_list('inputs/11.txt')

def make_int_board(space: list[str]) -> list[list[int]]:
    new_board = []
    for row in space:
        new_row = []
        for char in row:
            new_row.append(1 if char == '#' else 0)
        new_board.append(new_row)
    return new_board

def find_galaxies(space) -> list[tuple[int, int]]:
    coords = []
    for x, row in enumerate(space):
        for y, col in enumerate(row):
            if col == 1:
                coords.append((x, y))
    return coords

def get_empties(spaces: list[list[int]]) -> list[list[int]]:
    empties: list[list[int]] = [[], []]
    for i, row in enumerate(spaces):
        if sum(row) == 0:
            empties[0].append(i)
    transpose = list(map(list, zip(*spaces)))
    for i, col in enumerate(transpose):
        if sum(col) == 0:
            empties[1].append(i)
    return empties

def add_expanded_space(
                       first: tuple[int, int],
                       second: tuple[int, int],
                       empties: list[list[int]],
                       how_many_extra: int = 1
) -> int:
    stride = -1 if first[0] > second[0] else 1
    vertical_range = range(first[0], second[0], stride)
    stride = -1 if first[1] > second[1] else 1
    horizontal_range = range(first[1], second[1], stride)
    empties_hit = sum(how_many_extra for i in empties[0] if i in vertical_range)
    empties_hit += sum(how_many_extra for i in empties[1] if i in horizontal_range)
    return empties_hit

def solve(input_list: list[str], how_many_extra: int = 1) -> int:
    answer = 0
    int_board = make_int_board(input_list)
    empties = get_empties(int_board)
    galaxies_coords = find_galaxies(int_board)
    for i, _ in enumerate((galaxies_coords)):
        for j in range(i+1, len(galaxies_coords)):
            first = galaxies_coords[i]
            second = galaxies_coords[j]
            added_distance = add_expanded_space(first, second, empties, how_many_extra)
            vertical_distance = abs(second[0] - first[0])
            horizontal_distance = abs(second[1] - first[1])
            answer += vertical_distance + horizontal_distance + added_distance
    return answer

assert solve(tests, how_many_extra=1) == 374, solve(tests, how_many_extra=1)
print(f'The solution to part 1 is: {solve(inp, how_many_extra=1)}')

assert solve(tests, how_many_extra=9) == 1030, solve(tests, how_many_extra=9)
assert solve(tests, how_many_extra=99) == 8410, solve(tests, how_many_extra=99)
print(f'The solution to part 2 is: {solve(inp, how_many_extra=999999)}')
