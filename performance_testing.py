import time
from sudoku_solver import solve_easy_sudoku
from sudoku_generator import generate_sudoku


start_time = time.time()
for _ in range(8192):
    solve_easy_sudoku()
print("Average sudoku completion time over 8192 runs:", round((time.time() - start_time) * 1000 /8192, 6), "ms")


start_time = time.time()
for _ in range(2048):
    generate_sudoku()
print("Average sudoku generation time over 2048 runs:", round((time.time() - start_time) * 1000 / 2048, 6), "ms")
