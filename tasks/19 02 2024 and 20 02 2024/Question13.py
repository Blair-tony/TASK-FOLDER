# Write a Python program to check if a string contains only digits.("12345" -->True)

string = input("Enter string: ")

if string.isdigit():
    print("this string has only digits")
else:
    print("this string has characters other than digits")