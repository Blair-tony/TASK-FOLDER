#Write a Python function to find the maximum of three numbers.

def maxfun():
    a=int(input("enter a first number"))
    b=int(input("enter a second number"))
    c=int(input("enter a third number"))
    if (a>b and a>c):
        print("first number is the largest")
    elif (b>c and b>a):
        print("second number is the largest")
    elif (c>a and c>b):
        print("third number is the largest")
        
        
maxfun()
