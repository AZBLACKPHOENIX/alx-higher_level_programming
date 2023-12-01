#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    def calculate_args_sum():
        args_sum = sum(int(arg) for arg in argv[1:])
        print(args_sum)

    calculate_args_sum()
