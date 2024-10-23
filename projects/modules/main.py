"""
    demostrate the use of the calculator package
"""

# import modules
from math_operations import calculator


def main():
    """uses calculator.py to add or subtract numbers
    """
    result = calculator.add(5, 3)
    print("Addition result:", result)

    result = calculator.subtract(10, 4)
    print("Subtraction result:", result)
