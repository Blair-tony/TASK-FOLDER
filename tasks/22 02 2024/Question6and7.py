# 6) Extend the above solution and add another instance attribute called grade (should be string).

# Assign value to grade from within the constructor. 

# The value should not be taken from user input. 

# Instead use the following conditions and assign values to grade by using the value of score. 

# grade = A+ if score >=90 

# grade = A if score >=80 and <90 

# grade = B+ if score >=70 and <80 

# and so on. 

# if score is below 40 then grade should be "FAILED" 


#  7)Extend the above solution again and add another instance method called 'as_dict'. 

# The method should return a dictionary with the data of the student.

# It should contain 'name', 'score', 'grade', keys and their respective values.


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = 'A+' if score >= 90 else 'A' if score >= 80 else 'B+' if score >= 70 else 'B' if score >= 60 else 'C+' if score >= 50 else 'C' if score >= 40 else 'FAILED'

    def display(self):
        print("Name of the student:", self.name)
        print("Score of the student:", self.score)
        print("Grade of the student:", self.grade)

    def as_dict(self):
        return {'name': self.name, 'score': self.score, 'grade': self.grade}



student1 = Student("Blair", 55)
student2 = Student("Tony", 45)


student1.display()
print()
student2.display()
print() #question 6 outuput

print("Student 1 as dictionary:", student1.as_dict())
print("Student 2 as dictionary:", student2.as_dict()) #question 7 output