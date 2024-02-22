# Write a program to create a child class Teacher that will inherit the properties from the parent class Staff. 

#     attributes need for staff : role,department, salary 

#     attributes need for teacher: name,age 

#     method in  staff : def print_details() 

 

#     output expected - 

#         Name:  Raj 

#         Age:  28 

#         Role: Teacher 

#         Department: Science 



class Staff:
    def __init__(self, role, dep, salary):
        self.role = role
        self.department = dep
        self.salary = salary

    def details(self):
        print("Role:", self.role)
        print("Department:", self.department)


class Teacher(Staff):
    def __init__(self, name, age, role, dep, salary):
        super().__init__(role, dep, salary)
        self.name = name
        self.age = age

    def details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().details()


teacher = Teacher("Raj", 28, "Teacher", "Science", "50000")
teacher.details()
