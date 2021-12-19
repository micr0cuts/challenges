#pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name
from typing import Tuple

x_target: range = range(124, 175)
y_target: range = range(-123, -86)
test_x_target: range = range(20, 31)
test_y_target: range = range(-10, -4)

def do_one_step(
                x: int,
                y: int,
                x_vel: int,
                y_vel: int
                ) -> Tuple[int, int, int, int]:
    x_vel_inc = 0
    if x_vel > 0:
        x_vel_inc = -1
    elif x_vel < 0:
        x_vel_inc = 1

    return x + x_vel, y + y_vel, x_vel + x_vel_inc, y_vel-1

def solve(x_t: range, y_t: range) -> Tuple[int, int]:
    part1 = 0
    part2 = 0
    for i_x_vel in range(max(x_t)+1):
        for i_y_vel in range(-abs(min(y_t)), abs(min(y_t))):
            x_vel = i_x_vel
            y_vel = i_y_vel
            x, y = 0, 0
            highest_y = 0
            while x <= max(x_t) and y >= min(y_t):
                x, y, x_vel, y_vel = do_one_step(x, y, x_vel, y_vel)
                highest_y = max(y, highest_y)
                if x in x_t:
                    if y in y_t:
                        part1 = max(highest_y, part1)
                        part2 += 1
                        break
    return part1, part2

tests_solution, tests_solution2 = solve(test_x_target, test_y_target)
assert tests_solution == 45
assert tests_solution2 == 112
solution1, solution2 = solve(x_target, y_target)
print(f"The solution to part 1 is: {solution1}")# 7503
# stuck here, tests pass but 3166 is the wrong answer

print(f"The solution to part 2 is: {solution2}") # 3166 is too low
