# Write a program that opens a file, reads its contents, and writes the contents to a new file. 
# Use a try-except-finally block to ensure that the file is closed even if an exception occurs during the file operations.

try:
    # Open the source file for reading
    with open('data.txt', 'r') as source_file:
        # Read the contents of the source file
        contents = source_file.read()

    # Open the destination file for writing
    with open('output.txt', 'w') as destination_file:
        # Write the contents to the destination file
        destination_file.write(contents)

except FileNotFoundError:
    print("Error: One of the files does not exist.")

except Exception as e:
    print("Error:", e)

finally:
    # Ensure that files are closed even if an exception occurs
    if 'source_file' in locals() and not source_file.closed:
        source_file.close()

    if 'destination_file' in locals() and not destination_file.closed:
        destination_file.close()
