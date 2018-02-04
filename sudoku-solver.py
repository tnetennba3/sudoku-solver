import math
import time
import collections


def remove_zeros(list_of_values):
    return [x for x in list_of_values if x != 0]


def check_nine_unique(list_of_values, list_type):
    without_zeros = remove_zeros(list_of_values)
    if len(set(without_zeros)) != len(without_zeros):
        raise Exception("Error with " + list_type + ": " + str(list_of_values))


def convert_to_columns(grid):
    return [set([line[i] for line in grid]) for i in range(9)]


def convert_to_squares(grid):
    squares = []
    for x in range(3):
        for y in range(3):
            x_values = range(3 * x, 3 * x + 3)
            y_values = range(3 * y, 3 * y + 3)
            square = set([grid[i][j] for i in x_values for j in y_values])
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


def solve_sudoku(grid):

    columns = convert_to_columns(grid)
    squares = convert_to_squares(grid)

    queue = collections.deque([(x, y) for x in range(9) for y in range(9) if grid[x][y] == 0])

    while len(queue) > 0:
        cell = queue.popleft()
        row, column = cell
        square_index = math.floor(row / 3) * 3 + math.floor(column / 3)
        possibilities = set(range(1, 10)) - set(grid[row]) - columns[column] - squares[square_index]
        if len(possibilities) == 1:
            new_number = possibilities.pop()
            columns[column].add(new_number)
            squares[square_index].add(new_number)
            grid[row][column] = new_number
        else:
            queue.append(cell)

    return grid


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
    solve_sudoku(sudoku_puzzle)


start_time = time.time()

for i in range(1024):
    main()

print("Sudoku completed 1024 times in:", round((time.time() - start_time), 6), "s")
