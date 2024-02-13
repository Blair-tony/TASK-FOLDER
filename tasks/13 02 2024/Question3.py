#Write a Python program to find if a given string starts with a given character using Lambda.

h=lambda x: True if x.startswith("y") else False #startswith() method returns True if the string begins with the specified value; otherwise, it returns False
word=input("enter any word")
print(h(word))