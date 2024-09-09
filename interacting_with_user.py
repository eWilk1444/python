"""
    This file is about interpreting and using user input.
"""

# This is the UI
print("Welcome", "\n",
      "Please enter the amount of money you spend on each category annually")

# This section holds the input of the user in variables
housing = input("How much do you spend on housing (rent or mortgage)? ")
print(50 * "*" + "\n")
utilities = input("On utilities? (electric, cable, internet, gas, etc.) ")
print(50 * "*" + "\n")
groceries = input("On groceries? ")
print(50 * "*" + "\n")
transport = input("On trasnportation (gas, repairs, etc.)? ")
print(50 * "*" + "\n")
healthcare = input("On healthcare (premiums, deductible, out of pocket)? ")
print(50 * "*" + "\n")
personal = input("On personal care items? ")
print(50 * "*" + "\n")
clothes = input("On personal effects? ")
print(50 * "*" + "\n")
debt = input("On debt repayments? ")

# This section holds the math required to calculate the total of the variables
