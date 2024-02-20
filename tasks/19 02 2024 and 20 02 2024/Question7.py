# Write a Python program to implement a binary search on a sorted list. 


def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2 # to get the midpoint of the whole sequence
        midpoint_value = sequence[midpoint]
        if midpoint_value == item: #if the midpoint is the value return true
            return midpoint

        elif item < midpoint_value: #value of item less than midpoint value checks left of the midpoint
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1 #value of item greater than midpoint then begin value is midpoint value+1 to check the right side of the list

    return None

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = int(input("Enter the item to search for: "))


print(binary_search(sequence_a, item_a))