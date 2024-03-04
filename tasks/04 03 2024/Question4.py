# Merge Multiple Text Files into One 


inputs = ['data.txt', 'output.txt', 'sample.txt']  # file names

output = 'merged_file.txt' # Output file



with open(output, 'w') as outfile: # Open the output file in write mode
   
    for file_name in inputs: # Iterate through each input file
   
        with open(file_name, 'r') as infile:     # Open each input file in read mode
           
            outfile.write(infile.read()) # Read the content of each input file and write it to the output file
            outfile.write('\n')  # Add a new line between the contents of different files

print("Files merged successfully!")
