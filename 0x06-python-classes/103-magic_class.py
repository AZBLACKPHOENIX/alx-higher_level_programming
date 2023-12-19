#!/usr/bin/python3
import math
"""define magicClass"""
class MagicClass:
    """Represent a magic class with radius attribute."""
    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius."""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius

