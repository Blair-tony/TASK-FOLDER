# Python program to for student height record for a school using Class and 
# Objects.

class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_records(self):
        print("Student Height Records:")
        for student in self.students:
            print(f"Name: {student.name}, Height: {student.height} cm")


if __name__ == "__main__":
    try:
        num_students = int(input("Enter the number of students: "))
        school = School()

        for i in range(num_students):
            name = input(f"Enter the name of student {i+1}: ")
            height = float(input(f"Enter the height of student {i+1} (in cm): "))
            student = Student(name, height)
            school.add_student(student)

        school.print_records()
    except ValueError:
        print("Please enter a valid number of students.")
