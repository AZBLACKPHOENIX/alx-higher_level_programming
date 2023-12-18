#!/usr/bin/python3
def safe_print_list_integers(my_list, x):
    count = 0

    for i in range(x):
        try:
            # Attempt to format the element as an integer and print it
            print("{:d}".format(int(my_list[i])), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            # Skip elements that cannot be formatted as integers or handle index errors
            pass

    print()  # Print a newline after all integers have been printed
    return count
