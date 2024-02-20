#  Write a Python program to reverse a list.


lst = []

n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n): #repeates the number of elements needed to be entered
    element = int(input()) #inputs the elements
    lst.append(element) #appends to the list
lst.reverse()
print(lst) 