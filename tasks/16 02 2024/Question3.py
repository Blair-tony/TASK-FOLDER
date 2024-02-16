# Write a Python program to print a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are the square of the keys 

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: ")) # CHANGED THE PROGRAM AS USER INPUTS THE VALUES, NOT USING 1 TO 15 

square= {}

for i in range(start, end+1):
    square[i] = i ** 2

print("the square of number of the given range : ", square)