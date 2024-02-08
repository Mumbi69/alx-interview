#!/usr/bin/python3
"""N Queens module"""
from sys import argv


def check_row(board, index, board_len):
    """This function checks if there is a queen in the row """
    for r in range(board_len):
        if board[index][r]:
            return False

    return True


def check_diagonals(board, row, col, board_len, step):
    """This function checks if there is a queen in the diagonals """
    c = col
    for r in range(row, -1, -1):
        if c < 0 or c >= board_len:
            break
        if board[r][c]:
            return False
        c += step

    return True


def check_all(board, row, col, n):
    """This function checks if it's safe to place a queen at a given position """
    if not check_row(board, row, n):
        return False

    return check_diagonals(board, row, col, n, -1) and check_diagonals(board, row, col, n, 1)


def solve_nqueens(n):
    """This function solves the N queens problem """
    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0] * n for _ in range(n)]
    result = []

    i = 0
    c = 0
    r = i

    while i < n:
        while c < n:
            found = False

            while r < n:
                if check_all(board, r, c, n):
                    board[r][c] = 1
                    result.append([c, r])
                    found = True
                    r = 0
                    break
                r += 1

            if not found and result:
                last_i = result.pop()
                c = last_i[0]
                r = last_i[1] + 1
                board[last_i[1]][last_i[0]] = 0
                continue
            c += 1

        if result:
            print(result)
            i = result[0][1]
            last_i = result.pop()
            c = last_i[0]
            r = last_i[1] + 1
            board[last_i[1]][last_i[0]] = 0
        else:
            return


def main():
    """Initializing function """

    argc = len(argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
