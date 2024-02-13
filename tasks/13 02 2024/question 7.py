#Write a Python program to find palindromes in a given list of strings using Lambda. 

a=lambda s: s==s[::-1]

string = ["dad", "mom", "racecar", "noon", "world", "civic"]

J = list(filter(a, string))

print("Palindromes in the list:", J)