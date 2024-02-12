#Create a function that takes two arguments, a name and an age, and prints a message like 
#"Hello,   [Name]! You are [Age] years old." Call this function with your name and age as arguments.

def my_fun(fname,lage):
    print("Hello,"+fname+"! You are "+str(lage)+" years old")

fname=input("enter name")
lage=int(input("age"))
my_fun(fname,lage)