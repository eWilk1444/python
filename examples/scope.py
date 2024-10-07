"""
    Scope and its applications
"""

global TAX_RATE
TAX_RATE = 0.07  # Set the global tax rate to 7%

# Function to calculate tax based on the price


def calculate_tax(price):
    demo = "Demonstration"
    # 'tax' is a local variable inside this function.
    # It uses the global variable 'TAX_RATE' to calculate the tax.
    tax = price * TAX_RATE
    return tax  # Returns the calculated tax value.


# Function to calculate the total price (price + tax)


def calculate_total(price):
    # 'total' is a local variable in this function.
    # It calls 'calculate_tax' to compute the tax and adds it to the original price.
    total = price + calculate_tax(price)
    return total  # Returns the total price after adding the tax.

# Main part of the program


# Input from user, converted to float (decimal number)
price = float(input("Enter a price: "))


# Calls 'calculate_total' function and formats the output to 2 decimal places
# The formatted string is displayed to the user
print(f"The total price is ${calculate_total(price):,.2f}")

# Displays the tax rate by converting it to a percentage and formatting to 2 decimal places
print(f"The tax rate is {(TAX_RATE * 100):,.2f}%")
tax = ("Taxes are way too high!")
