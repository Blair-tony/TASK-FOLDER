# Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("blair tony", 18, "c")


print("Name:", student1.name)
print("Age:", student1.age)
print("Grade:", student1.grade)
