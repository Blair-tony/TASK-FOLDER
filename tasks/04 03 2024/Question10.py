def sum_divisible_by_3_or_5(numbers):
    """
    Returns the sum of numbers divisible by 3 or 5 from the input list.
    """
    # Initialize sum
    total_sum = 0

    # Iterate through the numbers in the list
    for num in numbers:
        # Check if the number is divisible by 3 or 5
        if num % 3 == 0 or num % 5 == 0:
            # Add the number to the total sum
            total_sum += num

    return total_sum

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
result = sum_divisible_by_3_or_5(numbers_list)
print("Sum of numbers divisible by 3 or 5:", result)
