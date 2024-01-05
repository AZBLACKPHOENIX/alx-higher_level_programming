#!/usr/bin/python3
import sys

class NQueens:
    def __init__(self, N):
        if not N.isdigit():
            print("N must be a number")
            sys.exit(1)

        self.N = int(N)
        if self.N < 4:
            print("N must be at least 4")
            sys.exit(1)

        self.board = [-1] * self.N
        self.solutions = []

    def is_safe(self, row, col):
        """Check if it's safe to place a queen at self.board[row][col]"""
        for i in range(col):
            if self.board[i] == row or \
               self.board[i] - i == row - col or \
               self.board[i] + i == row + col:
                return False
        return True

    def solve_nqueens(self, col):
        """Recursive function to solve N queens problem"""
        if col == self.N:
            self.solutions.append(self.board[:])
            return

        for i in range(self.N):
            if self.is_safe(i, col):
                self.board[col] = i
                self.solve_nqueens(col + 1)
                self.board[col] = -1

    def print_solutions(self):
        """Print the solutions in the specified format"""
        for solution in self.solutions:
            print([[row, solution[row]] for row in range(self.N)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n_queens_solver = NQueens(sys.argv[1])
    n_queens_solver.solve_nqueens(0)
    n_queens_solver.print_solutions()

