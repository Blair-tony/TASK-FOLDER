# The program takes input from the user and checks if whether the input 
# value is an integer or not, if the input value is not an integer then the 
# program will through a Type exception. 
# Run 1:  
# Enter First Number: 43 
# 43 
# Run 2: 
# Enter First Number: 123.1 
# Invalid Input..Please Input Integer Only.. 
# Enter First Number: 43 
# 43


def get_input():
    while True:
        user_input = input("Enter the Number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid Input..Please Input Integer Only..")

if __name__ == "__main__":
    number = get_input()
    print(number)
