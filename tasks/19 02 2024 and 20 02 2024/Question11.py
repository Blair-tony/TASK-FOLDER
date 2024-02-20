#  Write a Python program to find the intersection of two lists.


lst1= []

n = int(input("Enter the number of elements in list 1: "))
print("Enter the elements in list 1:")
for i in range(n): #repeates the number of elements needed to be entered
    element = int(input()) #inputs the elements
    lst1.append(element) #appends to the list

lst2 = []

n = int(input("Enter the number of elements in list 2: "))
print("Enter the elements in list 2:")
for i in range(n): #repeates the number of elements needed to be entered
    element = int(input()) #inputs the elements
    lst2.append(element) #appends to the list

intersection = [value for value in lst1 if value in lst2]
print("Intersection of the list 1 and list 2 is :", intersection)