"""
    User inputs values for specific categories of expenses
     then program totals them up and shows the percentages each category contributed
"""

# This greets the user and establishes what data to enter
print("Welcome!")
print(50 * "*")
print("Please enter the amount of money you spend on each category annually.")
print("\nDo not include non-number characters (like $ or €) and round to the nearest cent.")
print(50 * "*")

# This section holds the input of the user in variables as floats
housing = float(input("How much do you spend on housing (rent or mortgage)? "))
print(50 * "*") # creating space for legibility, I like the ASCII aesthetic of the star lines but if they are annoying to you, let me know.
utilities = float(input("On utilities? (electric, cable, internet, gas, etc.) "))
print(50 * "*")
groceries = float(input("On groceries? "))
print(50 * "*")
transport = float(input("On trasnportation (gas, repairs, etc.)? "))
print(50 * "*")
healthcare = float(input("On healthcare (premiums, deductible, predicted out of pocket)? "))
print(50 * "*")
personal = float(input("On personal care items? "))
print(50 * "*")
clothes = float(input("On personal effects? "))
print(50 * "*")
debt = float(input("On debt repayments? "))
print(50 * "*")

# Combining user input into total annual budget
annual_budget = float(housing + utilities + groceries + transport + healthcare + personal + clothes + debt)
print(f"Your annual budget is: ${annual_budget:.2f}")
print(50 * "*")

# computes and prints percentages of budget to terminal for each category
print(f"Housing is {(housing/annual_budget):.2%} of your total budget")
print(f"Utilities are {(utilities/annual_budget):.2%} of your budget")
print(f"Groceries are {(groceries/annual_budget):.2%} of your budget")
print(f"Transportation is {(transport/annual_budget):.2%} of your budget")
print(f"Healthcare is {(healthcare/annual_budget):.2%} of your budget")
print(f"Personal care items are {(personal/annual_budget):.2%} of your budget")
print(f"Clothing is {(clothes/annual_budget):.2%} of your budget")
print(f"Debt repayments are {(debt/annual_budget):.2%} of your budget")
print(50 * "*")