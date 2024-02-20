# Write a Python program to remove all whitespace characters from a string.

string = input("enter string : ")

string1 = string.replace(' ', '').lower()

if string == string1:
    print("No white space in string")
else:
    print("after eliminating white space: ",string1)