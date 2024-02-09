#Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same

h=int(input("enter any first number :"))
i=int(input("enter any second number :"))
j=int(input("enter any third number :"))

if (h>i and h>j):
    print("FIRST NUMBER IS GREATEST")
elif (i>h and i>j):
    print("SECOND NUMBER IS GREATEST")
elif (j>h and j>i):
    print("THIRD NUMBER IS GREATEST")
else:
    print("all the number are same")