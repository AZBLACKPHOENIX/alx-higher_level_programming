#!/usr/bin/python3

def no_c(my_string):
    # Create a new string with characters not equal to 'c' or 'C'
    result = ''.join(char for char in my_string if char.lower() != 'c')

    return result
