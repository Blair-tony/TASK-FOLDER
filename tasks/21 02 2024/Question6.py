# Write a Python program to read a random line from a file.

import random

file_path = "C:\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\destination.txt"
with open(file_path, "r") as file:
    lines = file.readlines() # to read lines
    random_line = random.choice(lines) #random module to utilize the random.choice()
    print(random_line.strip()) #Print the selected random line after removing white space
