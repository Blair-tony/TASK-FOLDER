# Write a Python program that takes a list of integers as input and returns a 
# new list with only the numbers that are prime.  


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:   # Checks if a given number is prime.
            return False
    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)] # Filters prime numbers from the list of integers.

# Example usage:
input_list = [111,22,23,47,55,88,66,59,43,67,73,77,78]
prime_numbers = filter_primes(input_list)
print("Prime numbers are:", prime_numbers)
