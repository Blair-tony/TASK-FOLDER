# Write a Python program to read a file line by line store it into a variable. 

path = "\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\text file.txt" 
with open(path, "r") as file:
    file_content = file.readlines()
print(file_content)