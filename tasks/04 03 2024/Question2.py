# Count the Number of Lines, Words, and Characters in a Text File


filename = 'sample.txt'  # file name


file = open(filename, 'r')  # Open the file


linecount = 0
wordcount = 0
charactercount = 0 # Initialize counters


for line in file: # Read the file line by line
   
    linecount += 1 # Count lines
    
   
    charactercount += len(line) # Count characters
    
    
    words = line.split() # Split the line into words
    wordcount += len(words) # count words


file.close()


print("No of lines:", linecount)
print("No of words:", wordcount)
print("No of characters:", charactercount)
