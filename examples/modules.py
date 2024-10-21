"""
    Modules and stuff
"""
import math as m  # creating alias

# Get two numbers from the user
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# Use math.pow() to calculate the result
result = m.pow(base, exponent)

# Print the result
print(f"{base} raised to the power of {exponent} is {result}")
