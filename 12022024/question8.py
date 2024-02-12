# Define a function that accepts 2 values and return its sum, subtraction and multiplication. 
# Using 4 types of functions based on arguments and return type. 

num1=int(input("enter a first number"))
num2=int(input("enter a second number"))
o=int(input("enter the number for operation \n"
            "1 addition\n"
            "2 substraction\n"
            "3 division\n"
            "4 multiplication\n"
            ":"))


def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

def mult(num1,num2):
    return num1*num2

if (o==1):
    print(add(num1,num2))
elif(o==2):
    print(sub(num1,num2))
elif(o==3):
    print(div(num1,num2))
elif(o==4):
    print(mult(num1,num2))