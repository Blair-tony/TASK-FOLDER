# Write a function that takes a list of numbers as input and returns the 
# second-largest number. 

def secondlargest(listnumbers):
    if len(listnumbers) < 2:
        return "List should contain at least two numbers"
    
    
    max_number = max(listnumbers) # Find the maximum number
    
    
    listnumbers.remove(max_number)# Removes the maximum number from the list to get the second largest
    
   
    second_largest = max(listnumbers) # Find the second largest number as the largest number is removed
    
    return second_largest

# Function to take a list of numbers as user input
def take_user_input():
    numbers_list = []
    num_numbers = int(input("Enter the number of numbers: "))

    for i in range(num_numbers):
        number = float(input(f"Enter number {i+1}: "))
        numbers_list.append(number)
    
    return numbers_list

# Usage:
numbers_list = take_user_input()
result = secondlargest(numbers_list)
print("Second largest number:", result)
