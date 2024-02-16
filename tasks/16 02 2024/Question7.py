# Write a Python program to Delete a list of keys from a dictionary 




dict1={"a":1,"b":2,"c":3,"d":4,"e":5}

to_delete = input("Enter keys to delete (separated by comma): ").split(',') #in this the entered key is split using comma

deleted = {k:dict1.pop(k,None) for k in to_delete} #pop method is used to delete , none is used if the key not found

print("Dictionary after deleting:",dict1)

for key, value in deleted.items(): #if the value of the key is none error message will be printed along with the key
    if value is None:
        print("keys not found :",key)
