"""
    This program will count how many people order food, the cost of the order,
    add taxes and tip, then divide the total bill equally
"""

# variables
cost = 0
count = 3
tax_rate = .06
tip_percent = .25
total = 0
cost_1 = float(input("how much was the cost of the first order? "))
cost_2 = float(input("how much was the cost of the second order? "))
cost_3 = float(input("how much was the cost of the third order? "))

cost = cost + cost_1 + cost_2 + cost_3
tax_amt = cost * tax_rate
tip_amt = cost * tip_percent
total = tax_amt + tip_amt + cost

# prints to terminal
print(f"Your total is: ${total:.2f} with a tip of {
      tip_amt:.2f} and tax of {tax_amt:.2f}")
print(f"Each person should pay: ${total/3:.2f}")
