"""
    Recursion and stuff lmao
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Example usage:
print(fibonacci(5))  # Output: 5
