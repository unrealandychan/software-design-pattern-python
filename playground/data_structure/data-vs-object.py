from abc import ABC


# Data vs Object
# Data Structure Programming
# In data structure programming, we create classes to store data and functions to manipulate the data.
# Example
class Circle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Square:
    def __init__(self, side):
        self.side = side


class Geometry:
    def __init__(self):
        self.pi = 3.14

    def area(self, shape):
        if shape is Circle:
            return self.pi * shape.radius ** 2
        elif shape is Rectangle:
            return shape.width * shape.height
        elif shape is Square:
            return shape.side ** 2

    def perimeter(self, shape):
        if shape is Circle:
            return 2 * self.pi * shape.radius
        elif shape is Rectangle:
            return 2 * (shape.width + shape.height)
        elif shape is Square:
            return self.side * 4


# Multi paradigm Programming
class Shape(ABC):
    def area(self):
        pass

    def perimeter(self):
        pass


class CircleNew(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class RectangleNew(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class SquareNew(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4

#
