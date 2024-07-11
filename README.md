![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# Sudoku Solver

## **Description**
**This Python project solves Sudoku puzzles using a backtracking algorithm**.
<br>It includes two scripts : one for **solving a single Sudoku puzzle** and another for **solving multiple Sudoku puzzles read from a file**.
<br>The scripts ensure each puzzle adheres to Sudoku rules by filling empty cells with valid numbers. Additionally, the multiple Sudoku solver script measures and reports the time taken to solve each puzzle.


## **Features**
- **Single Sudoku Solver** : Solves a predefined 9x9 Sudoku grid.
- **Multiple Sudoku Solver** : Solves multiple 9x9 Sudoku grids read from a file.
- **Backtracking Algorithm** : Efficiently solves puzzles by trying and validating numbers recursively.
- **Timing Functionality** : Measures and displays the time taken to solve each puzzle and the average time for multiple puzzles.

## **Prerequisites**
- **Python 3.x** installed on your machine

## **Installation Instructions**
Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the scripts.

1. Clone this repository to your machine.
   
   ```bash
   git clone https://github.com/0x414854/Sudoku_Solver.git

2. Navigate to the repository directory.

   ```bash
    cd Sudoku_Solver

## **Usage Examples**
***`Single Sudoku Solver`***

1. Run the '*sudoku_solver.py*' script!
   
   ```bash
   python3 sudoku_solver.py

2. The script will **solve the predefined Sudoku puzzle** and **print the solved grid**.

***`Multiple Sudoku Solver`***

1. Run the '*sudoku_multiple_grid.py*' script!
   
   ```bash
   python3 sudoku_multiple_grid.py

2. The script will **read 50 Sudoku puzzles from '*sudoku_grid.txt*'**, **solve each one**, and **print the solved grids along with the time taken for each puzzle and the average solve time**.

## Tree Directory

Sudoku_Solver/
<br>├── sudoku_solver.py
<br>├── sudoku_multiple_grid.py
<br>├── sudoku_grid.txt
<br>└── README.md

## **License**
This project is licensed under the **MIT License**.

## **Author**
[**0x414854**](https://github.com/0x414854)
