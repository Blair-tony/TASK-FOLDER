# Write a Python program to remove all occurrences of a given element from a list

def remove_element(lst, element):
    while element in lst:
        lst.remove(element)

my_list = [1, 2, 3, 4, 2, 5, 2]
print(my_list)
remove = int(input("enter the element to remove : "))

remove_element(my_list, remove)
print("List after removing",remove, ":", my_list)
