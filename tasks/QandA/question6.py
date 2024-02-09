#Python program to print all even/odd numbers in the range given by user

p=int(input("enter the starting number :"))
q=int(input("enter the ending number :"))

for i in range(p,q,2):
     if(i%2!=0):
            print (i)