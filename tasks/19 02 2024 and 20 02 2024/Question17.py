#  Write a Python program to find the sum of all even numbers in a list.

lst = []

n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n): #repeates the number of elements needed to be entered
    element = int(input()) #inputs the elements
    lst.append(element) #appends to the list

even = 0

for num in lst:
    if num % 2 == 0:
        even += num
print("Sum of even numbers in the list:", even)
