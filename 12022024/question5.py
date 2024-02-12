# Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count(string):
    upper = 0
    lower = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower


input_string = input("Enter a string: ")
upper, lower = count(input_string)
print("uppercase:", upper)
print("lowercase", lower)