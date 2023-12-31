#!/usr/bin/python3
"""Create A Class"""
class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return (str(self.print_symbol) * self.width + "\n") * self.height

    def __repr__(self):
        """Representation of the rectangle for recreation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a square with equal width and height"""
        return cls(size, size)

if __name__ == "__main__":
    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)

