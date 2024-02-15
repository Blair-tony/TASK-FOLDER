# Write a Python program to print the numbers of a specified list after removing even numbers from it
# 	list = [24,34,53,65,78,93,23,42]


a = [24, 34, 53, 65, 78, 93, 23, 42]

filter1 = []

for num in a :
    if num % 2 != 0:
        filter1.append(num)

print( filter1)