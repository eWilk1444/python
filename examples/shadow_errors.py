# Global variable
math = 10


def multiply(math):
    # The parameter 'number' shadows the global variable 'number'
    return math * 2


# Calling the function
result = multiply(5)

print("Result:", result)
print("Global number:", math)
