# Write a Python program to calculate the sum of all elements in a list recursively.

def recursive(lst):

    if not lst:
        return 0
    else:
        return lst[0] + recursive(lst[1:])


lst = []

n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n): #repeates the number of elements needed to be entered
    element = int(input()) #inputs the elements
    lst.append(element) #appends to the list


total_sum = recursive(lst)
print("Sum of all elements in the list:", total_sum)
