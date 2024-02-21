# Write a Python program to assess if a file is closed or not


path = input("enter the path : ")  

file = open(path, "r")  # Open the file

if file.closed is False : # checks if closed
    print("  file is not closed  ")
else:
    print("  file is closed  ")


file.close()  # Close the file


if file.closed is False :  # checks if again closed
    print("  file is not closed  ")
else:
    print("  file is closed  ")