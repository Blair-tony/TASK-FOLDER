# # write a single program to handle the following arithmetic operations for addition, subtraction, 
# multiplication , division, floor division,modulus and Exponentiation.

num1=int(input("enter a first number"))
num2=int(input("enter a second number"))
o=int(input("enter the number for operation \n"
            "1 addition\n"
            "2 substraction\n"
            "3 division\n"
            "4 multiplication\n"
            "5 floor division\n"
            "6 Modulus\n"
            "7 Exponent\n"
            ":"))


def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    return num1/num2
def mult(num1,num2):
    return num1*num2
def fdiv(num1,num2):
    return num1//num2
def modu(num1,num2):
    return num1%num2
def expo(num1,num2):
    return num1**num2

if (o==1):
    print(add(num1,num2))
elif(o==2):
    print(sub(num1,num2))
elif(o==3):
    print(div(num1,num2))
elif(o==4):
    print(mult(num1,num2))
elif(o==5):
    print(fdiv(num1,num2))
elif(o==6):
    print(modu(num1,num2))
elif(o==7):
    print(expo(num1,num2))