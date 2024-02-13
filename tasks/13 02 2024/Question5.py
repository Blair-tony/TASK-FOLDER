#Write a Python program to check whether a given string is a number or not using Lambda. 


num=lambda x:x.isdigit()

test=input("enter any string")
print(num(test))