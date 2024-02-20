# Write a Python program to merge two sorted lists into a single sorted list. 



list1= []

n = int(input("Enter the number of elements in list 1: "))
print("Enter the elements in list 1:")
for i in range(n): #repeates the number of elements needed to be entered
    element = int(input()) #inputs the elements
    list1.append(element) #appends to the list

list2 = []

n = int(input("Enter the number of elements in list 2: "))
print("Enter the elements in list 2:")
for i in range(n): #repeates the number of elements needed to be entered
    element = int(input()) #inputs the elements
    list2.append(element) #appends to the list

res = sorted(list1 + list2)
print ("list 1: " + str(list1))
print ("list 2 : " + str(list2))
print ("combined list : " , str(res))
