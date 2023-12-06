#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys alphabetically
    sorted_keys = sorted(a_dictionary.keys())

    # Print each key-value pair in the sorted order
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))

