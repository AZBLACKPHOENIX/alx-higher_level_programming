#!/usr/bin/python3

def print_hidden_4_names():
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    print_hidden_4_names()

