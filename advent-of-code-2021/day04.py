from lib import inputgetter_list
import sys

inp = inputgetter_list('inputs/04.txt')

drawings = [int(i) for i in inp[0].split(',')]

boards = []
board = []
for i, line in enumerate(inp[2:], 3):
    if line:
        line = [int(x) for x in line.split()]
        board.append(line)
    elif not line:
        boards.append(board)
        board = []
boards.append(board)

test_boards = []
test_board = []
tests = inputgetter_list('tests/04.txt')
test_drawings = [int(i) for i in tests[0].split(',')]
for i, line in enumerate(tests[2:], 3):
    if line:
        line = [int(x) for x in line.split()]
        test_board.append(line)
    elif not line:
        test_boards.append(test_board)
        test_board = []
test_boards.append(test_board)

hits = []
for board in boards:
    b = []
    for row in board:
        b.append([0 for _ in row])
    hits.append(b)

test_hits = []
for test_board in test_boards:
    t_b = []
    for test_row in test_board:
        t_b.append([0 for _ in test_row])
    test_hits.append(t_b)

def check_for_bingo_horizontal(hits, boards, skip_these):
    for board_i, hit_board in enumerate(hits):
        if board_i in skip_these:
            continue
        for row_i, row in enumerate(hit_board):
            if all(row):
                return board_i
    return

def check_for_bingo_vertical(hits, boards, skip_these):
    for board_i, hit_board in enumerate(hits):
        if board_i in skip_these:
            continue
        for col_i, col in enumerate([*zip(*hit_board)]):
            if all(col):
                return board_i
    return

def get_unmarked_numbers(board, drawn):
    return set(num for row in board for num in row) - set(drawn)

# test_drawn = []
# for t_d in test_drawings:
#     test_drawn.append(t_d)
#     for board_i, board in enumerate(test_boards):
#         for row_i, row in enumerate(board):
#             for col_i, col in enumerate(row):
#                 if col == t_d:
#                     test_hits[board_i][row_i][col_i] = 1
#                 horizontal_bingo = check_for_bingo_horizontal(test_hits, test_boards)
#                 if horizontal_bingo:
#                     unmarked_numbers = get_unmarked_numbers(board_i, test_boards, test_drawn)
#                     bingo = sum(unmarked_numbers) * t_d
#                     print(t_d, sum(unmarked_numbers))

#                 vertical_bingo = check_for_bingo_vertical(test_hits, test_boards)
#                 if vertical_bingo:
#                     unmarked_numbers = get_unmarked_numbers(board_i, test_boards, test_drawn)
#                     bingo = sum(unmarked_numbers) * t_d
#                     print(t_d, sum(unmarked_numbers))
# assert bingo == 4512

drawn = []
winner_boards = set()
bingos = []
for d in drawings:
    drawn.append(d)
    for board_i, board in enumerate(boards):
        if board_i in winner_boards:
            continue
        for row_i, row in enumerate(board):
            for col_i, col in enumerate(row):
                if col == d:
                    hits[board_i][row_i][col_i] = 1
                horizontal_bingo = check_for_bingo_horizontal(hits, boards, winner_boards)
                if horizontal_bingo:
                    winner_boards.add(board_i)
                    unmarked_numbers = get_unmarked_numbers(boards[board_i], drawn)
                    bingo = sum(unmarked_numbers) * d
                    bingos.append(bingo)
                    #print(board_i, d, sum(unmarked_numbers), bingo)

                vertical_bingo = check_for_bingo_vertical(hits, boards, winner_boards)
                if vertical_bingo:
                    winner_boards.add(board_i)
                    unmarked_numbers = get_unmarked_numbers(boards[board_i], drawn)
                    bingo = sum(unmarked_numbers) * d
                    bingos.append(bingo)
                    #print(board_i, d, sum(unmarked_numbers), bingo)
print(f"The solution to part 1 is: {bingos[0]}")
print(f"The solution to part 2 is: {bingos[-1]}")

