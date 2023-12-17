# pylint: disable=missing-module-docstring,invalid-name,missing-function-docstring
import re

from typing import List
from typing import Tuple

from lib import check_coordinates
from lib import inputgetter_list

tests = inputgetter_list('tests/03.txt')
inp = inputgetter_list('inputs/03.txt')

InputList = List[str]
Coordinate = Tuple[Tuple[int, int], Tuple[int, int]]
CoordinateWithNumbers = dict[Tuple[int, int], str]

def is_symbol_adjacent(
    m: InputList,
    coords: Coordinate
) -> bool:
    x = coords[0][0]
    for y in range(coords[0][1], coords[1][1]):
        for x_i in (-1, 0, 1):
            this_x = x + x_i
            for y_i in (-1, 0, 1):
                this_y = y + y_i
                if check_coordinates(this_x, this_y, m):
                    maybe_symbol = m[this_x][this_y]
                    if not maybe_symbol.isdigit() and maybe_symbol != '.':
                        return True
    return False

def expand_coords(n_with_coords: CoordinateWithNumbers) -> Tuple[dict, dict]:
    expanded_coords = {}
    expanded_coords_uuids2number = {}
    uuid = 0
    for (start_x, start_y), number in n_with_coords.items():
        for i in range(len(number)):
            expanded_coords[(start_x, start_y + i)] = uuid
            expanded_coords_uuids2number[uuid] = int(number)
        uuid += 1
    return expanded_coords, expanded_coords_uuids2number

def find_asterisk_coords(m: InputList) -> List[Tuple[int, int]]:
    coords = []
    for x, row in enumerate(m):
        for y, col in enumerate(row):
            if col == '*':
                coords.append((x, y))
    return coords

def find_gears(m: InputList,
    ast_coords,
    exp_coords,
    exp_coords_uuids2number
) -> List[int]:
    gears = []
    for (x, y) in ast_coords:
        adjacents = set()
        for x_i in (-1, 0, 1):
            this_x = x + x_i
            for y_i in (-1, 0, 1):
                this_y = y + y_i
                if check_coordinates(this_x, this_y, m):
                    if (this_x, this_y) in exp_coords:
                        adjacents.add(exp_coords[(this_x, this_y)])
        if len(adjacents) == 2:
            adjacents = list(adjacents)
            gears.append(
                exp_coords_uuids2number[adjacents[0]] * exp_coords_uuids2number[adjacents[1]]
            )
    return gears

def find_numbers(m: InputList) -> CoordinateWithNumbers:
    pattern = re.compile('[0-9]+')
    numbers_with_coords = {}
    for x, row in enumerate(m):
        matches = re.finditer(pattern, row)
        for match in matches:
            numbers_with_coords[(x, match.start())] = match.group()
    return numbers_with_coords

def solve(input_list: InputList) -> int:
    answer = 0
    numbers_with_coords = find_numbers(input_list)
    for (start_x, start_y), number in numbers_with_coords.items():
        if is_symbol_adjacent(
            input_list,
            ((start_x, start_y),
            (start_x, start_y+len(number)))
        ):
            answer += int(number)
    return answer

def solve_part2(input_list: InputList) -> int:
    asterisk_coords = find_asterisk_coords(input_list)
    numbers_with_coords = find_numbers(input_list)
    expanded_coords, expanded_coords_uuids2number = expand_coords(numbers_with_coords)
    gears = find_gears(input_list, asterisk_coords, expanded_coords, expanded_coords_uuids2number)
    return sum(gears)

assert solve(tests) == 4361
print(f'The solution to part 1 is: {solve(inp)}')

assert solve_part2(tests) == 467835
print(f'The solution to part 2 is: {solve_part2(inp)}')
