import math
import time


def remove_zeros(list_of_values):
    return [x for x in list_of_values if x != 0]


def check_nine_unique(list_of_values, list_type):
    without_zeros = remove_zeros(list_of_values)
    if len(set(without_zeros)) != len(without_zeros):
        raise Exception("Error with " + list_type + ": " + str(list_of_values))


def convert_to_columns(grid):
    return [[line[i] for line in grid] for i in range(9)]


def convert_to_squares(grid):
    squares = []
    for x in range(3):
        for y in range(3):
            x_values = range(3 * x, 3 * x + 3)
            y_values = range(3 * y, 3 * y + 3)
            square = [grid[i][j] for i in x_values for j in y_values]
            squares.append(square)
    return squares


def check_grid_valid(grid):
    # checks grid format is valid
    for row in grid:
        if len(row) != 9:
            raise Exception("Line length incorrect " + str(row))
    if len(grid) != 9:
        raise Exception("Number of lines incorrect")

    # check grid only contains values 0 - 9
    for row in grid:
        for value in row:
            if value not in range(10):
                raise Exception("Invalid value, sudoku must only contain numbers 0-9")

    # check lines are valid
    for row in grid:
        check_nine_unique(row, "row")

    # check columns are valid
    for column in convert_to_columns(grid):
        check_nine_unique(column, "column")

    # check squares are valid
    for square in convert_to_squares(grid):
        check_nine_unique(square, "square")


def solve_sudoku(grid, grid_of_possibilities):

    columns = convert_to_columns(grid)
    squares = convert_to_squares(grid)

    for row in range(9):
        for column in range(9):
            if len(grid_of_possibilities[row][column]) > 1:
                square_index = math.floor(row / 3) * 3 + math.floor(column / 3)
                grid_of_possibilities[row][column] = list(
                    set(grid_of_possibilities[row][column]) -
                    set(grid[row]) - set(columns[column]) - set(squares[square_index])
                )

            if len(grid_of_possibilities[row][column]) == 1:
                grid[row][column] = grid_of_possibilities[row][column][0]

    return grid, grid_of_possibilities


def check_if_complete(grid):
    return 0 not in [value for row in grid for value in row]


def print_grid(grid):
    s = ''
    for row in grid:
        for value in row:
            if value == 0:
                s += ' '
            else:
                s += str(value)
            s += ' '
        s += '\n'
    print(s)


def main():
    sudoku_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    check_grid_valid(sudoku_puzzle)

    start_time = time.time()

    grid_of_possibilities = [[range(1, 10) if value == 0 else [value] for value in row] for row in sudoku_puzzle]

    for iter in range(100):
        sudoku_puzzle, grid_of_possibilities = solve_sudoku(sudoku_puzzle, grid_of_possibilities)
        if check_if_complete(sudoku_puzzle):
            break
    else:
        raise Exception("This sudoku puzzle seems unsolvable. Are you sure you inputted the numbers in correctly?")

    print("sudoku completed in", round(time.time() - start_time, 6), "s")
    print_grid(sudoku_puzzle)

main()
