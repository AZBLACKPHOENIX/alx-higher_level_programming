#!/usr/bin/python3
"""define class"""
class MyInt(int):
    """A class representing MyInt that inherits from int."""
    """method"""
    def __eq__(self, other):
        """Override the equality operator (==)."""
        return super().__ne__(other)
    """method"""
    def __ne__(self, other):
        """Override the inequality operator (!=)."""
        return super().__eq__(other)
