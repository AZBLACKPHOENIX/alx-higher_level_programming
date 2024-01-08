#!/usr/bin/python3
class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize the Square instance."""
        self.integer_validator("size", size)
        super().__init__(size, size)  # Call the parent class constructor with width and height set to size

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
