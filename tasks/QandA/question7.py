#Python program to print the multiplication table of any number (number should be taken as input and user decides the end limit of the table)

x=0
y=int(input("Input multiplication table number :"))
a=int(input("Specify multiplication table end value :"))
while(x<=a):
    z=x*y
    print(x,"*",y,"=",z)
    x+=1