# Write a Python program to copy the contents of a file to another file

source = "C:\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\text file.txt"
destination = "C:\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\destination.txt"

with open(source, "r") as source_file, open(destination, "w") as destination_file:
    destination_file.write(source_file.read())
    
f=open(destination,"rt")
print(f.read())