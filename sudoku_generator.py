import time
import random
from helpers import convert_to_sets, generate_row_column_square_indices, add_new_number_to_sets,\
    subtract_old_number_from_sets, print_grid


def generate_sudoku():

    grid = [[0 for _ in range(9)] for _ in range(9)]

    columns, squares, rows = convert_to_sets(grid)

    queue = [(x, y) for x in range(9) for y in range(9)]
    queue_index = 0
    attempted_numbers = [set() for _ in range(81)]

    while queue_index < 81:

        row, column, square = generate_row_column_square_indices(queue, queue_index)
        possibilities = set(range(1, 10)) - rows[row] - columns[column] - squares[square]

        while not possibilities:
            attempted_numbers[queue_index] = set()
            queue_index -= 1
            row, column, square = generate_row_column_square_indices(queue, queue_index)
            old_number = grid[row][column]
            grid[row][column] = 0
            attempted_numbers[queue_index].add(old_number)
            subtract_old_number_from_sets(columns, squares, rows, column, square, row, old_number)
            possibilities = set(range(1, 10)) - rows[row] - columns[column] - squares[square] - attempted_numbers[
                queue_index]

        if possibilities:
            queue_index += 1
            new_number = random.choice(list(possibilities))
            add_new_number_to_sets(columns, squares, rows, column, square, row, new_number)
            grid[row][column] = new_number

    return grid


def main():

    start_time = time.time()
    completed_sudoku = generate_sudoku()
    print_grid(completed_sudoku)
    print("Sudoku generated in", round((time.time() - start_time) * 1000, 6), "ms")
