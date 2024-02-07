# N Queens
* Import sys Module: The code imports the sys module, which is necessary for handling command-line arguments and exiting the program with specific statuses.

* is_safe Function: This function checks whether it's safe to place a queen at a given position on the board. It checks if there's no queen in the same column, upper-left diagonal, and upper-right diagonal.

* solve_nqueens_util Function: This function is a recursive helper function that tries to place queens on the board row by row. It backtracks when it reaches a dead-end or finds a solution, printing the solutions as it finds them.

* solve_nqueens Function: This function is responsible for parsing the command-line argument, validating it, and initiating the recursive backtracking algorithm to find solutions.

* Command-Line Argument Validation: The program checks if the user has provided exactly one command-line argument (excluding the script name). If not, it prints a usage message and exits with status 1.

* Parsing and Validating N: The program checks if the provided argument N is a valid integer greater than or equal to 4. If not, it prints an appropriate error message and exits with status 1.

* Initialize the Board: The program initializes an empty chessboard represented as a 2D list with all elements set to 0.

* Invoking the Solution Finder: The program calls the solve_nqueens_util function with the initialized board and starts finding solutions recursively.

* Printing Solutions: As the solutions are found, they are printed out to the console.
