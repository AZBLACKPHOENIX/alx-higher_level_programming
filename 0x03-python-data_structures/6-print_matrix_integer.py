#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                # Last element in the row, no space after it
                print("{:d}".format(num), end="$\n")
            else:
                # Not the last element, add "$" after it
                print("{:d}".format(num), end=" ")
    print("$")
