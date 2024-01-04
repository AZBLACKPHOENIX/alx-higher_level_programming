#!/usr/bin/python3
"""Define A Class"""
class Rectangle:
    """initialize atrributes"""
    def __init_(self, width = 0, height = 0):
        self._width = width
        self._height = height
    """Define Property"""
    @property
    def width(self):
        return self._width
    """Set Property"""
    def width(self, value):
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            value = self._width
    """Property for height"""
    @property
    def height(self):
        return self._height
    """Set property"""
    @setter
    def height(self, value):
        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            value = self._height
