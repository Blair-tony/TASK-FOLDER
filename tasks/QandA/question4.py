#Python program to check the number taken as an input is even or odd,print invalide input if user enters anything other than integers

p=int(input("enter any number"))
if (p%2==0):
    print("the number is even")
elif (p%2!=0):
    print("the number is odd")
else:
    print("invalid input")