# Write a Python program to create a file where all letters of 
# English alphabet are listed by specified number of letters on each line. 

path =input("enter the path : ") # enter the path
letters = int(input("enter the letters per line : "))  # Specify the number of letters per line

with open(path, "w") as file:  # Open the file
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define the English alphabet
    for i in range(0, len(alphabet), letters):  # Iterate over the alphabet
        file.write(alphabet[i:i+letters] + '\n')
        
        
f=open(path,"rt")
print(f.read())# to read the text