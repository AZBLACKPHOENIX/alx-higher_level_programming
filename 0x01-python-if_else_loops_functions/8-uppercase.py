#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is lowercase using ASCII values
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase character to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end='')
        else:
            # Print non-lowercase characters as they are
            print("{}".format(char), end='')
