#!/usr/bin/python3
"""module for N Queens"""

import sys


def is_safe(board, row, col, N):
    """Check if there's a queen in the same column"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, N):
    """
    a recursive helper function that tries to place queens
    on the board row by row. It backtracks when it reaches a
    dead-end or finds a solution, printing the solutions as it finds them.
    """
    if row == N:
        for i in range(N):
            print("".join(str(cell) for cell in board[i]))
        print()
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N)
            board[row][col] = 0

def solve_nqueens(N):
    """
    responsible for parsing the command-line argument,
    validating it, and initiating the recursive backtracking
    algorithm to find solutions.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0, N)
