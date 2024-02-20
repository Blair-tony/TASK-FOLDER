# Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])

flat1 = [1, [2, 3], [4, 5, 6]]
flat2 = []

for sublist in flat1:
    if isinstance(sublist, list):  # Check if sublist is a list
        for num in sublist:
            flat2.append(num) #if sublist containes numbers only then it append to flat2
    else:
        flat2.append(sublist) # if it is a list again then it append to sublist and runs in the loop again

print(flat2)
