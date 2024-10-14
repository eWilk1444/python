"""
    Exceptions
"""


def error_checker():
    try:
        result = 10 / 5
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Division successful!")
    finally:
        print("Execution completed.")


def main():
    error_checker()


main()
