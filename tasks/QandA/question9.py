#Find the factorial of a number taken as input using while loop

a=int(input("enter any number:"))
f = 1
while a > 0:
    f *= a
    a -= 1
print("Factorial:", f)