#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        # Attempt to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle division by zero
        result = None
        print("Inside result: None")
    finally:
        # Print the result with "Inside result:" if it's not None
        if result is not None:
            print("Inside result: {:d}".format(result) if isinstance(result, int) else result)

    return result

