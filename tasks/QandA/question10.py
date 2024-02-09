#Find the sum of all even numbers between the range given by user
x=0
e=0
a=int(input("range of even sum needed:"))

while(x<=a):
    if(x%2==0):
        e=e+x
    x+=1
print("evensum=",e)