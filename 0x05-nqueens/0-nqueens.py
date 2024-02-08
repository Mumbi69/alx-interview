#!/usr/bin/python3
"""N Queens module"""


import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)
n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    exit(1)


def check_if_safe(i, j, board):
    """
    Args:
        i : Argument
        j : Argument
        board : Argument

    """
    for element in board:
        if (
            i == element[0]
            or j == element[1]
            or abs(i - element[0]) == abs(j - element[1])
        ):
            return False
    return True


def backtrack(n, row, q_board, s_board):
    """
    Args:
        n : Argument
        row : Argument
        q_board : Argument
        s_board : Argument

    """
    if row == n:
        s_board.append(q_board.copy())
        return

    for column in range(n):
        if check_if_safe(row, column, q_board):
            q_board.append([row, column])
            backtrack(n, row + 1, q_board, s_board)
            q_board.pop()


solution_board = []
queen_board = []
backtrack(n, 0, queen_board, solution_board)
for row in solution_board:
    print(row)


if __name__ == "__main__":
    main()
