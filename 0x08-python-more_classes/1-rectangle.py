#!/usr/bin/python3
class Rectangle:
    def __init_(self, width = 0, height = 0):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    def width(self, value):
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            value = self._width

    @property
    def height(self):
        return self._height
    @setter
    def height(self, value):
        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            value = self._height
