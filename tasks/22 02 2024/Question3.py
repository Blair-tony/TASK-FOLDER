# Write a Python class, Square, and define two methods that return the square area and perimeter

class Square:

    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length


square1 = Square(int(input("enter the length")))
print("Area:", square1.area(), "Perimeter:", square1.perimeter())