import math
import time
import collections
from helpers import check_grid_valid, convert_to_sets, add_new_number_to_sets, print_grid
from example_sudokus import easy_sudoku


def solve_sudoku(grid):

    columns, squares, rows = convert_to_sets(grid)
    queue = collections.deque([(x, y) for x in range(9) for y in range(9) if grid[x][y] == 0])
    iteration = 0

    while len(queue) > 0:

        cell = queue.popleft()
        row, column = cell
        square = math.floor(row / 3) * 3 + math.floor(column / 3)
        possibilities = set(range(1, 10)) - rows[row] - columns[column] - squares[square]

        if len(possibilities) == 1:

            new_number = possibilities.pop()
            add_new_number_to_sets(columns, squares, rows, column, square, row, new_number)
            grid[row][column] = new_number

        else:
            queue.append(cell)

        iteration += 1

        if iteration == 1000:
            raise Exception("This sudoku puzzle seems unsolveable. Are you sure you inputted the numbers in correctly?")

    return grid


def solve_easy_sudoku():

    check_grid_valid(easy_sudoku)
    return solve_sudoku(easy_sudoku)


def main():

    start_time = time.time()
    solved_sudoku = solve_easy_sudoku()
    print_grid(solved_sudoku)
    print("Sudoku completed in", round((time.time() - start_time) * 1000, 6), "ms")
