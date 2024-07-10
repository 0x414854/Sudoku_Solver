"""
This script solves a 9x9 Sudoku puzzle using a backtracking algorithm.
It fills each empty cell with numbers from 1 to 9 that satisfy Sudoku rules.
If no solution exists for the given puzzle, it prints an error message.
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
    grid = [[0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 8, 2],
        [0, 0, 0, 5, 8, 0, 9, 3, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 8],
        [0, 6, 0, 0, 1, 0, 7, 0, 0],
        [9, 0, 7, 8, 3, 0, 0, 0, 0],
        [1, 0, 3, 0, 0, 0, 0, 2, 9],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [7, 0, 0, 9, 0, 0, 0, 6, 0]]
    
    if solve_sudoku(grid):
        print("Here is the result of your Sudoku\n")
        for row in grid:
            print(row)
        print()
    else:
        print("Error : No solution exists ! ")

if __name__ == "__main__":
    main()

