#!/usr/bin/python3
"""Define a class"""


class Square:
    """Instantiate class"""
    def __init__(self, size=0):
        """Set size to 0 and validate the attributes"""
        self.size = size

    @property
    def size(self):
        """Retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size with validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2
