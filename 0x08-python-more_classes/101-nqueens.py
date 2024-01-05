#!/usr/bin/python3
""" import systems"""
import sys
""" create class """

class NQueens:
    """ initialize class """
    def __init__(self, N):
        if not N.isdigit():
            print("N must be a number")
            sys.exit(1)

        self.N = int(N)
        if self.N < 4:
            print("N must be at least 4")
            sys.exit(1)

        self.board = [[0 for _ in range(self.N)] for _ in range(self.N)]
        self.solutions = []

    def is_safe(self, row, col):
        """Check if it's safe to place a queen at self.board[row][col]"""
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_nqueens(self, col):
        """Recursive function to solve N queens problem"""
        if col == self.N:
            self.solutions.append([row[:] for row in self.board])
            return

        for i in range(self.N):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.solve_nqueens(col + 1)
                self.board[i][col] = 0

    def print_solutions(self):
        """Print the solutions in the specified format"""
        for solution in self.solutions:
            print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n_queens_solver = NQueens(sys.argv[1])
    n_queens_solver.solve_nqueens(0)
    n_queens_solver.print_solutions()

