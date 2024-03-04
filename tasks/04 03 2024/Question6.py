# Write a Python function that takes a list of strings as input and returns a 
# new list with the strings sorted in descending order of their lengths. 


def sortbylength(strings):
    sorted_strings = sorted(strings, key=len, reverse=True) # descending order sorting 
    return sorted_strings

stringlist = []
num_strings = int(input("Enter the number of strings: ")) # Takes number of strings needed from user

for i in range(num_strings):
    string = input(f"Enter string {i+1}: ")
    stringlist.append(string) # Takes input of strings from the user

# Sort the strings
sorted_list = sortbylength(stringlist)
print("Sorted strings in descending order of length:", sorted_list)
