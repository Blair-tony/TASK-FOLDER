# Write a Python program that prompts the user to enter an integer and 
# handles the ValueError exception if the user enters a non-integer value.

while True:
    try:
        user_input = input("Please enter an integer: ")
        integer_value = int(user_input)
        print("You entered:", integer_value)
        break  # Break out of the loop if integer conversion succeeds
    except ValueError:
        print("Invalid input. Please enter an integer.")

