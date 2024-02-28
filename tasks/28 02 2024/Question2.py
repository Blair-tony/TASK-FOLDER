# Create a program that opens a file and reads its contents. Use a try-except block to handle the FileNotFoundError 
# exception and display a custom error message if the file does not exist.

file_name = input("Enter the name of the file to read: ")

try:
    with open(file_name, 'r') as file:
        contents = file.read()
    print("Contents of the file", file_name, ":\n", contents)
except FileNotFoundError:
    print("Error: The file", file_name, "does not exist.")
