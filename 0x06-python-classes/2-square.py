#!/usr/bin/python3
"""Define a class"""


class Square:
    """Instantiate class"""
    def __init__(self, size=0):
        """Set size to 0 and validate the attributes"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

