"""
    Return values of functions are demonstrated    
"""


def add_numbers(num1, num2):
    # add two numbers together
    total = num1 + num2
    return total


# must have storage for returned value
result = add_numbers(5, 3)
print(f"The sum is: {result}")

# return the divisor and remainder


def division(num1, num2):
    whole = num1 // num2
    remainder = num1 % num2
    return whole, remainder


whole, remainder = division(12, 7)
print(f"The answer is {whole} with a remainder of {remainder}.")
