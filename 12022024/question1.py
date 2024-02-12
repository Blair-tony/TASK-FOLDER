#Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example. 

def factor(n): #function
    r=1
    for i in range(1,n+1):
        r *=i
    return r


num=int(input("enter any integer"))  #example
print(factor(num))