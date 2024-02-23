# Task 2 
# ===== 
# Create a class named Cypher. The purpose of that class is to receive an input string of characters and convert it to 
# another cypher string. Use a constructor to receive the input. You can also read the input from user. But don’t use 
# input() inside the constructor.  
# The class must have a class method to do the string conversion. And an instance method to invoke the classmethod 
# from within it. 
# • Use the below conversion logic: 
# • Iterate over each character in the string, and if the character is a digit increment it by one (0->1, 1
# >2, ... 9 should be replaced with 0) 
# • if the character is an alphabet then shift the character by 2 positions (use chr() and ord() built-ins for 
# this) (a->c, b->d, ... y->a, z->b) If the character is in upper case convert it to lower and vice versa 
# • The returned string must be of same length as the input.  
# No need to implement the reversing algorithm but will be a plus if available. 
# 1) create an object for the Cypher class with the string. 
# 2) call the instance method, which should internally call the classmethod you prepared for the conversion, pass the 
# string data to classmethod and do the conversion. 
# No need to consider special characters for now. 
# # Expected output for the string "ABcD1293Z" is "cdEf2304b"



class Cypher:
    def __init__(self, input_string):
        self.input_string = input_string

    @classmethod
    def convert_string(cls, input_string):
        converted_chars = []
        for char in input_string:
            if char.isdigit():
                converted_chars.append(str((int(char) + 1) % 10))
            elif char.isalpha():
                if char.islower():
                    shifted_char = chr((ord(char) - 97 + 2) % 26 + 97)
                else:
                    shifted_char = chr((ord(char) - 65 + 2) % 26 + 65)
                converted_chars.append(shifted_char.swapcase())
            else:
                converted_chars.append(char)
        return "".join(converted_chars)

    def perform_conversion(self):
        return self.convert_string(self.input_string)


# Test the Cypher class
input_string = input("enter the cypher to convert : ")
cypher_instance = Cypher(input_string)
converted_result = cypher_instance.perform_conversion()
print(f"Converted result for '{input_string}': {converted_result}")
