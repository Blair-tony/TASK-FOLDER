# Search for a String in a Text File 



file_name = input("Enter the text file: ")  #  file name
search = input("Enter the string : ")  # string to search

# Open the file
file = open(file_name, 'r')

found = False  # if the string is found
line_number = 0  # To track of line numbers

# Read the file line by line
for line in file:
    line_number += 1  # Increment line number
    
    # Check if the search string is in the line
    if search in line:
        found = True
        print(f"Found '{search}' in {file_name} at line {line_number}:")
        print(line.strip())  # Print the line where the string is found

# Close the file
file.close()

# If string is not found
if not found:
    print(f"'{search}' not found in {file_name}")
