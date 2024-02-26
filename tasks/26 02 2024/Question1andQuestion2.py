


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def update_salary(self, hours, rate=200):
        self.salary = hours * rate

    def __str__(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

    def __add__(self, other):
        if not isinstance(other, Employee):
            raise TypeError("Unsupported operand types for +: 'Employee' and 'str'")
        return self.salary+other.salary


class PartTime(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.rate = 150

    def update_salary(self, hours):
        super().update_salary(hours, self.rate)
        
class Track:
    employees = []

    def __init__(self, Employee):
        self.employees.append(Employee)

    @classmethod
    def average_expense(cls):
        total_expense = sum(Employee.salary for Employee in cls.employees)
        return total_expense / len(cls.employees)


e1 = Employee(name=input("enter employee 1 name:"))
e1.update_salary(hours=int(input("enter hours:")))
e2 = Employee(name=input("enter employee 2 name:"))
e2.update_salary(hours=int(input("enter hours:")))

p1 = PartTime(name=input("enter partime 1 person name:"))
p1.update_salary(hours=int(input("enter hours:")))
p2 = PartTime(name=input("enter partime 2 person name:"))
p2.update_salary(hours=int(input("enter hours:")))
p3 = PartTime(name=input("enter partime 3 person name:"))
p3.update_salary(hours=int(input("enter hours:")))


print(e1)
print(e2) 
print(p1)
print(p2)
print(p3)


#TASK 1 -  the total salary expense

employees = [e1, e2, p1, p2, p3]
total_expense = sum(employee.salary for employee in employees)
print(f"\nTotal Salary: ${total_expense}")



# TASK 2 -  Average expense per employee.
t1 = Track(e1)
t2 = Track(e2)
t3 = Track(p1)
t4 = Track(p2)
t5 = Track(p3)


average_expense = Track.average_expense()
print("$Average expense:", average_expense)