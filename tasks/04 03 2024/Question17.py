#  Python program to delay printing of line from a file using sleep function


import time

def print_delay(filename, delay):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
                time.sleep(delay)
    except FileNotFoundError:
        print("File not found")


filename = input("Enter the name of the file: ")
delay = float(input("Enter the delay between lines (in seconds): "))
print_delay(filename, delay)
