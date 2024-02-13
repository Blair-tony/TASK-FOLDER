# Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list: 

# ['Python', 3, 2, 4, 5, 'version'] 

# Maximum values in the said list using lambda:5 



list1 = ['Python', 3, 2, 4, 5, 'version']

f = filter(lambda x: isinstance(x, (int, float)), list1)

value = max(f)

print(value)