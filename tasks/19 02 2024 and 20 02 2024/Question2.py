# Write a program to check the validity of a password. Primary conditions for password validation: - minimum 8 charecters -

# The alphabet must be between [a-z] -
# At least one alphabet should be of Upper Case [A-Z] - 
# At least 1 number or digit between [0-9]. -
# At least 1 character from [ _ or @ or $ ]

def valid_password(password):
    if len(password) < 8:
        return False #Checks length of password

    lower_case = False
    upper_case= False
    digit = False
    special_char= False #here if length is less than 8 then all parameter fails

    for char in password:
        if char.islower():
            lower_case = True
        elif char.isupper():
            upper_case = True
        elif char.isdigit():
            digit = True
        elif char in ['_', '@', '$']:
            special_char = True #if the length is greater than or equal to 8 then it checks all other parameters

    if lower_case and upper_case and digit and special_char:
        return True
    else:
        return False #if it satisfies all the condition by checking using and operator it returns true 


password = input("Enter password: ")
if valid_password(password):
    print("Valid password!")
else:
    print("Invalid password Please try again !")