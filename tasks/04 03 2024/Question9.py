# Write a Python function that takes a list of integers as input and returns a 
# new list with only the numbers that are perfect squares.



def perfect_square(num):
    return int(num ** 0.5) ** 2 == num  #check if a number is a perfect square
 
def check_list(num_list):
    # Function to check for perfect squares in the list
    perfect_squares = []
    for num in num_list:
        if perfect_square(num):
            perfect_squares.append(num)
    return perfect_squares
 
if __name__ == "__main__":
    # Example list of numbers
    numbers = [4, 16, 17, 11, 36, 82, 
           81, 49, 110, 120, 100]
 
    squares_list = check_list(numbers)
    print("Perfect squares are:", squares_list)