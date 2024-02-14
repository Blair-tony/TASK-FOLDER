# Write a Python code to remove all characters except a            

# Sample String : 'exercises' 

# Expected Result : 'eee' (Removed all characters except special character : e)

sample_string = input("enter any string")
result = ''.join(char for char in sample_string if char == 'a')
print(result)