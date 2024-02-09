#Find the sum of all odd numbers between the rane given by user using while loop

x=0
e=0
a=int(input("range of odd sum needed:"))

while(x<=a):
    if(x%2!=0):
        e=e+x
    x+=1
print("oddsum=",e)