# Write a Python program to check if a string is an anagram of another string.("listen", "silent")

str1 = input("enter first string : ")
str2 = input("enter second string : ") #inputes string

str1 = str1.replace(' ', '').lower()
str2 = str2.replace(' ', '').lower() # to remove space


if len(str1) != len(str2):
    print(str1," and ",str2," are not anagrams.") #if length of the string are not equal then condition fails
else:
    
    s_str1 = sorted(str1)
    s_str2 = sorted(str2) #sort the string in alphabetic order

   
    if s_str1 == s_str2:
        print(str1," and ",str2," are anagrams.")  # Checks if the sorted strings are equal
    else:
        print(str1," and ",str2," are not anagrams.")