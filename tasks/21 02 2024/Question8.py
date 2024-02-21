# Write a Python program to write a list to a file

file = "C:\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\OP.txt" 
lst = ["auto", "taxi", "bmw", "benz", "maruthi"]  # Sample list

with open(file, "w") as file:  # Open the file
    for item in lst:  # Iterate through the list
        file.write(item + "\n")  # Write each item to the file, followed by a newline character

f=open("C:\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\OP.txt","rt")
print(f.read())