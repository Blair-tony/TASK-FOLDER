#  Write a Python program to check if a given year is a leap year. 

lyear = int(input("Enter a year:"))

def leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True

    return False

if leap(lyear):
    print("It is a leap year")
else:
    print("It is not a leap year")
