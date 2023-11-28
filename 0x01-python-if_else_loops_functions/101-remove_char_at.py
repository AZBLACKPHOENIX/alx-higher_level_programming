#!/usr/bin/python3
def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        return input_str  # Return the original string if index is out of range

    # Use slicing to create a new string without the character at position n
    result_str = input_str[:n] + input_str[n+1:]
    return result_str
