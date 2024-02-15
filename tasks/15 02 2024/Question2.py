#.Write a Python program to remove duplicates from a list

li1 = [1,2,44,2,4,5,3,4,2,9,6,7,3,99,44,33,99]
l2= []

for item in li1:
    if item not in l2:
        l2.append(item)
        
li1 = l2

print(li1)
