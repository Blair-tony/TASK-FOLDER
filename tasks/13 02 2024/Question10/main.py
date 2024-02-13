from rectangle import rectanglearea

from rectangle import rectanglearea

def arearectangle():
    area = rectanglearea(length, breadth)
    return area

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
result = arearectangle()
print(f"Rectangle Area: {result:.2f} square units")

