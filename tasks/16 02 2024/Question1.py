# Write a Python program to merge two Python dictionaries.

dict1 = {"MODEL":"DIO","MAKE":"HONDA","COLOUR":"BLUE"}
dict2 = {"MODELS":"SWIFT","MAKE":"MS","COLOUR":"BLACK"}

merge=dict1.copy()
merge.update(dict2)

print("Merged String :", merge)
