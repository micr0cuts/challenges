#pylint: disable=missing-module-docstring,missing-function-docstring
from typing import List
from typing import Set
from typing import Tuple
from lib import inputgetter_list

inp: List = inputgetter_list('inputs/04.txt')
tests: List = inputgetter_list('tests/04.txt')

def get_boards(data: List) -> Tuple[List, List]:
    boards = []
    board = []
    hits = []
    hit_board = []
    for line in data[2:]:
        if line:
            line = [int(x) for x in line.split()]
            board.append(line)
            hit_board.append([0 for _ in line])
        elif not line:
            boards.append(board)
            hits.append(hit_board)
            board = []
            hit_board = []
    boards.append(board)
    hits.append(hit_board)

    return boards, hits

def check_for_bingo(hits: List, skip_these: Set) -> bool:
    '''
    First search horizontally, then vertically
    horizontal search is equivalent to:
    return any(all(row) for board_i, board in enumerate(hits) \
        if board_i not in skip_these for row in board)
    vertical search is equivalent to:
    return any(all(col) for board_i, board in enumerate(hits) \
        if board_i not in skip_these for col in zip(*board))
    '''
    for board_i, hit_board in enumerate(hits):
        if board_i not in skip_these:
            for row in hit_board:
                if all(row):
                    return True

    for board_i, hit_board in enumerate(hits):
        if board_i not in skip_these:
            for col in [*zip(*hit_board)]:
                if all(col):
                    return True
    return False

def get_unmarked_numbers(board: List, drawn: Set) -> Set:
    return set(num for row in board for num in row) - set(drawn)

def solve(data: List) -> List:
    # pylint: disable=too-many-locals
    drawings = [int(i) for i in data[0].split(',')]
    boards, hits = get_boards(data)
    drawn = []
    winner_boards = set()
    final_scores = []
    # pylint: disable=invalid-name
    for d in drawings:
        drawn.append(d)
        for board_i, board in enumerate(boards):
            if board_i in winner_boards:
                continue
            for row_i, row in enumerate(board):
                for col_i, col in enumerate(row):
                    if col == d:
                        hits[board_i][row_i][col_i] = 1
                    found_bingo = check_for_bingo(hits, winner_boards)
                    if found_bingo:
                        winner_boards.add(board_i)
                        unmarked_numbers = get_unmarked_numbers(boards[board_i], drawn)
                        bingo = sum(unmarked_numbers) * d
                        final_scores.append(bingo)
                        continue

    return final_scores

test_bingos: List = solve(tests)
assert test_bingos[0] == 4512

bingos: List = solve(inp)
print(f"The solution to part 1 is: {bingos[0]}")
print(f"The solution to part 2 is: {bingos[-1]}")
