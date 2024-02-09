#Write python programs , which accept two inputs and perform the following arithmetic operations
#   i)Addition (+)
#   ii)Subtraction (-)
#   iii)Multiplication (*)
#   iv)Division (/)
#   v)Modulus (%)
#   vi)Exponentiation (**)
#   vii)Floor Division (//) 

num1=int(input("enter a first number :"))
num2=int(input("enter a second number :"))
o=int(input("enter the number for operation \n"
            "1 addition\n"
            "2 substraction\n"
            "3 multiplication\n"
            "4 division\n"
            "5 modulus\n"
            "6 Exponent\n"
            "7 Floor Division\n"
            ":"))
if (o==1):
    print(num1+num2)
elif (o==2):
    print(num1-num2)
elif (o==3):
    print(num1*num2)
elif (o==4):
    print(num1/num2)
elif (o==5):
    print(num1%num2)
elif (o==6):
    print(num1**num2)
elif (o==7):
    print(num1//num2)
elif (o<1 or o>7):
    print("invalid value")
