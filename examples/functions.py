"""
    Functions and stuff 
"""


# def my_function():
#     # functions are like hotkeys
#     # faster and easier than pressing everything individually everytime
#     print("Functions start with FUN!")


# my_function()


# def months(years):
#     # calculate how many months old you are, rounded to years
#     months = 12 * years
#     print(f"You are {months} months old.")


# years = int(input("How old are you, in years?"))
# months(years)


def add_numbers(number1, number2):
    # number1 and number2 are parameters
    total = number1 + number2
    return total


# pass in order
total = add_numbers(5, 7)
print(total)

# overrides default order when assigned
total = add_numbers(number2=12, number1=7)
print(total)
