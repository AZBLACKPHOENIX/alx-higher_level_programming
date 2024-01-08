#!/usr/bin/python3
"""define class"""
class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the Rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
