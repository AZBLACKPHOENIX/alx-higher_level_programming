#!/usr/bin/python3
"""
Define a class
"""

class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width with error checks
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height with error checks
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

