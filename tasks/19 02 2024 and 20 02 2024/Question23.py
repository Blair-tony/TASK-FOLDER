# Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.(gcd(48, 
# 60)=12)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function
num1 = int(input("enter any number 1 : "))
num2 = int(input("enter any number 2 : "))

gcd_result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd_result}.")
