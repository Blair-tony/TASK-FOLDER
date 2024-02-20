# Write a Python program to count the number of occurrences of each element in a tuple.

def occurrence(data):
    count = {}

    for element in data:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1

    return count

my_tuple = (1, 2, 3, 4, 2, 3, 4, 5, 2)
occurrences = occurrence(my_tuple)
print("Number of occurrences of each element:")
for element, count in occurrences.items():
    print(f"{element}: {count}")
