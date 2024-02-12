#Write a Python program to reverse a string 

def string(str1):
    w=""
    index=len(str1)
    while index > 0:
        w+=str1[index-1]
        index=index-1
    return w
print(string("blair"))