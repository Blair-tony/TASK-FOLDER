
#Define a function that accepts roll number and returns whether the student is present or absent. 


def attendence(rollno):
    x = [23,43,22,56]
    if rollno in x:
        print(f"Roll number {rollno} is present")
    else:
        print(f"Roll number {rollno} is absent")
        
rollno = int(input("Enter roll no:"))
attendence(rollno)