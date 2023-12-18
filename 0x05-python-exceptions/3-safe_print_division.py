#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        # Attempt to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle division by zero
        print("Inside result: None")
    except (ValueError, TypeError):
        # Handle unexpected value or type errors
        print("Inside result: None")
    finally:
        # Print the result with "Inside result:" regardless of success or failure
        print("Inside result: {:d}".format(result) if isinstance(result, int) else result)

    return result
