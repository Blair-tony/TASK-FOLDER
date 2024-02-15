# Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
# 	lst1=[2, 4, 6, 8, 10, 12, 14]



lst1 = [2, 4, 6, 8, 10, 12, 14]

square_list = [num ** 2 
               for num in lst1 
               if num ** 2 > 50]

print(square_list)
