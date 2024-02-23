# Task 1 
# ====== 
# 1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise 
# NotImplementedError() exception with a suitable message. 
# 2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC) 
# Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from 
# abc). 
# 3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle. 
# Define constructor for each of them to assign the necessary parameters required for calculating the area. 
# Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it. 
# Create an object for each of the subclasses and call the area method on the objects.







from abc import ABC, abstractmethod #inheriting ABC class from the abc module.
from math import pi, sqrt


class Shape(ABC): # class name shape
    @abstractmethod
    def area(self):
        raise NotImplementedError("Area method not implemented") # NotImplementedError()

# 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
    

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height  # parameters required for calculating the area.


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side # parameters required for calculating the area.


class Pentagon(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 1.72048 * self.side ** 2 # parameters required for calculating the area.


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2 # parameters required for calculating the area.


# Creating objects for each subclass and calling the area method
a=int(input("enter any base of triangle"))
b=int(input("enter any height of triangle"))
triangle = Triangle(a, b)
print("Area of Triangle:", triangle.area())
c=int(input("enter any base of square"))
square = Square(c)
print("Area of Square:", square.area())
d=int(input("enter any base of pentagon"))
pentagon = Pentagon(6)
print("Area of Pentagon:", pentagon.area())
e=int(input("enter radius"))
circle = Circle(3)
print("Area of Circle:", circle.area())
