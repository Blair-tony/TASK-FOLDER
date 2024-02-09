#Find the factorial of a number taken as input using for loop

def fact():
    num=int(input("enter any number:"))
    r=1
    for i in range(1,num+1):
        r=r*i
    print(r)
fact()