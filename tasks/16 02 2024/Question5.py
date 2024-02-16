# Write a Python program to multiply all the items in a dictionary.

from functools import reduce

dict1={"aa": 2, "bb": 10, "cc": 4, "dd": 20}

res=reduce(lambda x, y: x * y, dict1.values())

print("The product of all items:", res)
