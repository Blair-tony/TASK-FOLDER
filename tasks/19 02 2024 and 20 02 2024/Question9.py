#  Write a Python program to count the occurrences of an element in a list.

list=([num for num in range(1, 101) if num % 2 != 0]) # prints list of odd number from 1 to 101
print(list)
Search = int(input("enter the number to search: ")) #enter number to search in the list

def Occurance(list, number):
    count = 0 #count is set to zero 
    for i in list:
        if(i == number):
            count+=1 #if the number is found while traversing the list the count is incremented and updated
    return count

result = Occurance(list, Search)
if(result > 0):
    print("Count is : ", result)
else:
    print("Element not fount in the list")