#!/usr/bin/python3
def raise_exception():
    # Raise a type exception
    raise TypeError("Type exception")

# Test case
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

