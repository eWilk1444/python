"""
    Calculates factorials of numbers inputted by user
"""


def factorial_calculate(n):
    if n <= 0:
        return n
    else:
        return n * calculate_factorial(n-1)


def get_user_input():
    user_input = int(
        input("\nPlease enter an integer to calculate its factorial. "))


def main():
    number = get_user_input
    total = factorial_calculate(number)
    print(f"\n{number} factorial is {total}.\n")


main()
