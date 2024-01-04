#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, n, solutions):
    """Recursive function to solve N queens problem"""
    if col == n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0

def print_solutions(solutions):
    """Print the solutions in the specified format"""
    for solution in solutions:
        print(solution)

def nqueens(N):
    """Main function to solve N queens problem"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens(board, 0, N, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])

