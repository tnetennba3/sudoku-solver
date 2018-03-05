import math

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


def convert_to_sets(grid):
    columns = convert_to_columns(grid)
    squares = convert_to_squares(grid)
    rows = [set([value for value in row]) for row in grid]
    return columns, squares, rows


def generate_row_column_square_indices(queue, queue_index):
    row, column = queue[queue_index]
    square = math.floor(row / 3) * 3 + math.floor(column / 3)
    return row, column, square


def add_new_number_to_sets(columns, squares, rows, column, square, row, new_number):
    rows[row].add(new_number)
    columns[column].add(new_number)
    squares[square].add(new_number)


def subtract_old_number_from_sets(columns, squares, rows, column, square, row, old_number):
    rows[row].remove(old_number)
    columns[column].remove(old_number)
    squares[square].remove(old_number)
