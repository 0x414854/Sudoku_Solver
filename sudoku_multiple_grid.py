import time

"""
This script solves multiple Sudoku puzzles using a backtracking algorithm. It reads the puzzles from a file,
solves each one, and prints the solved grid along with the time taken to solve it. Additionally, it calculates
and prints the total and average time taken to solve all puzzles.
"""

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if grid[i][j] == num:
                return False

    return True

def main():
    total_start_time = time.time()

    with open('./sudoku_grid.txt', 'r') as f:
        grids = f.read().strip().split('\n\n')

    total_solve_time = 0

    for i, grid_str in enumerate(grids):
        print('Solving Sudoku #{}...\n'.format(i+1))
        grid = [[int(c) for c in row] for row in grid_str.split('\n')]
        start_time = time.time()
        if solve_sudoku(grid):
            solve_time = time.time() - start_time
            total_solve_time += solve_time
            for row in grid:
                print(' '.join(str(c) for c in row))
            print('\nSolved Sudoku #{} in {:.4f} seconds:'.format(i+1, solve_time))
        else:
            print('Unable to solve Sudoku #{}.'.format(i+1))
        print()

    total_time = time.time() - total_start_time

    print('Solved all 50 sudokus in {:.4f} seconds'.format(total_time))
    print('Average solve time per sudoku: {:.4f} seconds.'.format(total_solve_time / len(grids)))

if __name__ == "__main__":
    main()
