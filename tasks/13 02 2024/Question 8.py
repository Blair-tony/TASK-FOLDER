
# Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results. 

# Original list: [2, 4, 6, 9, 11] 

# Given number: 2 

# Result: 

# 4 8 12 18 22 



givnum=2
numblist=[2,4,6,9,11]

m=lambda givnum , list1 :[x*givnum for x in list1]

res=m(givnum,numblist)
print(res)