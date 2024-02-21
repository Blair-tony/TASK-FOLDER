# Write a Python program that takes a text file as input and returns the number of words of a given text file

path = input("Enter the path of the text file: ")

with open(path, "r") as file: # open file
    text = file.read() # read the full file
    word_count = len(text.replace(',', ' ').split()) # replace comma with space and split with space

print("Number of words:", word_count)