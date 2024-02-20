#  Write a Python program to find the second largest number in a list.

h=int(input("enter any first number"))
i=int(input("enter any second number"))
j=int(input("enter any thrid number"))

if(h>i and h>j):
    if(i>j):
        print(i,"is the second largest")
    else:
        print(j ,"is the second largest")
if(i>h and i>j):
    if(h>j):
        print(h,"is the second largest")
    else:
        print(j,"is the second largest")
if(j>i and j>h):
    if(i>h):
        print(i,"is the second largest")
    else:
        print(h,"is the second largest")