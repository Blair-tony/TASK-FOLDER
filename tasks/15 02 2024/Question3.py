# Write a Python program to count the number of strings where the string length is 2 or more.
# 	Sample List : ['abc', 'xyz', 'aba', '1']
# 	Expected Result : 3

list1 = ["12","1243","3122","a12" ,"1"]

c = 0

for s in list1:
    if len(s) >= 2:
        c += 1

print(c)