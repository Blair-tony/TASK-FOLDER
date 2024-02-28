# Write a program that calculates the division of two numbers entered by the user. Use a try-except 
# block to handle the ZeroDivisionError exception and display an appropriate error message if the user tries to divide by zero.



try:
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))

    result = dividend / divisor
    print("Result of division:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numeric values for dividend and divisor.")
