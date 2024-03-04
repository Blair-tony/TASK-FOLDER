#  Write a Python program that executes an operation on a list and handles an 
# IndexError exception if the index is out of range. 


def perform_operation_on_list(my_list, index):
    try:
        result = my_list[index] ** 2  # Squaring the element at the given index
        print("Result:", result)
    except IndexError:
        print("Index is out of range.")

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list)

    index = int(input("Enter the index to find the square: "))

    perform_operation_on_list(my_list, index)
