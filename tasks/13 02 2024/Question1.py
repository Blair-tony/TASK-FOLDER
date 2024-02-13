# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and prints the result. 

add = lambda x:x+15
a=int(input("enter any number"))
print(add(a))

x=int(input("enter any first number"))
y=int(input("enter any second number"))
multiply = lambda x,y:print(x*y)
multiply(x,y)