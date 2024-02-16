# Create a function that takes a string and returns a dictionary where keys are letters, 
# and values are the number of times each letter appears in the string 


def count1(string):
    letter={}
    for char in string:
        if char.isalpha():
            char=char.lower()  
            letter[char]=letter.get(char, 0) + 1
    return letter


input_string=input("enter any string")
res=count1(input_string)
print(res)