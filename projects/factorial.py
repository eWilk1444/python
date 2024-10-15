"""
    Calculates factorials of numbers inputted by user
"""


def factorial_calculate(n):
    if n <= 0:
        return n
    else:
        return n * factorial_calculate(n-1)


def main():
    number = int(input("\nPlease enter an integer to calculate its factorial. "))
    total = factorial_calculate(number)
    print(f"\nThe factorial of {number} is {total}. ")


main()
