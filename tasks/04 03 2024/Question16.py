#  Count the total number of uppercase characters in a file in Python



def count_uppercase_characters(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
        return uppercase_count
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return -1

# Example usage:
file_name = 'merged_file.txt'
uppercase_count = count_uppercase_characters(file_name)
if uppercase_count != -1:
    print(f"Total uppercase characters in {file_name}: {uppercase_count}")