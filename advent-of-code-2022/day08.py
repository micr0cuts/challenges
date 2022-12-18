from lib import Matrix
from lib import inputgetter_int_matrix

inp: Matrix = inputgetter_int_matrix('inputs/08.txt')
tests: Matrix = inputgetter_int_matrix('tests/08.txt')

def is_tree_at_edge(x: int, y: int, forest: Matrix) -> bool:
    return x in (0, len(forest) - 1) or y in (0, len(forest[x]) - 1)

def is_tree_visible(x: int, y: int, forest: Matrix, forest_t: Matrix) -> bool:
    height = forest[x][y]

    left = forest[x][:y + 1]
    if max(left) == height and left.count(height) == 1:
        return True

    right = forest[x][y:]
    if max(right) == height and right.count(height) == 1:
        return True

    up = forest_t[y][:x + 1]
    if max(up) == height and up.count(height) == 1:
        return True

    down = forest_t[y][x:]
    if max(down) == height and down.count(height) == 1:
        return True

    return False

def solve(trees: Matrix) -> int:
    visible_trees = set()
    transpose = [list(i) for i in zip(*trees)]

    for x, row in enumerate(trees):
        for y, _ in enumerate(row):
            if is_tree_at_edge(x, y, trees):
                visible_trees.add((x, y))
                continue
            if is_tree_visible(x, y, trees, transpose):
                visible_trees.add((x, y))

    return len(visible_trees)

def calculate_score(x: int, y: int, forest: Matrix, forest_t: Matrix) -> int:
    if is_tree_at_edge(x, y, forest):
        return 0

    score = 1
    height = forest[x][y]
    left = forest[x][:y][::-1]
    right = forest[x][y:]
    up = forest_t[y][:x][::-1]
    down = forest_t[y][x:]
    for direction in (left, right[1:], up, down[1:]):
        for num_trees_visible, tree in enumerate(direction, 1):
            if tree >= height or num_trees_visible == len(direction):
                score *= num_trees_visible
                break

    return score

def solve2(trees: Matrix) -> int:
    max_viewing_score = 0
    transpose = [list(i) for i in zip(*trees)]

    for x, row in enumerate(trees):
        for y, _ in enumerate(row):
            score = calculate_score(x, y, trees, transpose)
            max_viewing_score = max(max_viewing_score, score)

    return max_viewing_score


test_solution = solve(tests)
assert test_solution == 21, test_solution

solution = solve(inp)
print(f'The solution to part 1 is: {solution}')

test_solution2 = solve2(tests)
assert test_solution2 == 8

solution2 = solve2(inp)
print(f'The solution to part 2 is: {solution2}')
 