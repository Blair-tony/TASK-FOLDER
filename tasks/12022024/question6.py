# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
            else:
                return True

num=int(input("enter a number"))
print(test_prime(num))  