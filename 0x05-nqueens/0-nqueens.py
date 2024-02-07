#!/usr/bin/python3
"""module for N Queens"""

import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    size = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if size < 4:
    print("N must be at least 4")
    sys.exit(1)

chessboard = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    chessboard.append(row)
queens_positions = []


def mark_available_spots(queens, board):
    """This function checks and marks available spots on a chessboard."""
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            for x, y in queens:
                if i == x or j == y or abs(i - x) == abs(j - y):
                    board[i][j] = 1


def place_queens(size, queens, board, solutions):
    """This function places queens on a chessboard of given size"""
    if len(queens) == size:
        sorted_queens = sorted(queens, key=lambda x: x[0])
        if sorted_queens not in solutions:
            solutions.append(queens)
        return solutions
    mark_available_spots(queens, board)
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if not square:
                board_copy = [r[:] for r in board]
                place_queens(size, queens + [[i, j]], board_copy, solutions)
    return solutions


queens_positions = place_queens(size, queens_positions, chessboard, [])
for queen in queens_positions:
    print(queen)
