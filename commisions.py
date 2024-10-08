"""
    This program will get the total dollar value of sales for the week,
    and the number of sales from the user. Commisions are based on dollar value
    (under 1k, 5%, 1k-2.5k, 7.5%, over 2.5k, 10%).
    Every 10 sales provides a $25 bonus, regardless of value, with a maximum of $250 of bonus
"""

# variables
name = input("Please enter employee's name: ")
sales_count = int(input(f"How many sales did {name} have last week "))
sales_total = float(input(f"What was the gross revenue? "))
bonus = 0
commission = 0

# logic
if sales_count < 10:
    bonus = 0
elif sales_count < 20:
    bonus = 25
elif sales_count < 30:
    bonus = 50
elif sales_count < 40:
    bonus = 75
elif sales_count < 50:
    bonus = 100
elif sales_count < 60:
    bonus = 125
elif sales_count < 70:
    bonus = 150
elif sales_count < 80:
    bonus = 175
elif sales_count < 90:
    bonus = 200
elif sales_count < 100:
    bonus = 225
else:
    bonus = 250

if sales_total < 1000:
    commission = .05
elif sales_total < 2500:
    commission = .075
else:
    commission = .1

commission_amount = commission * sales_total

print(f"{name} will receive ${bonus} bonus for sales volume")
print(f"With a sales total of ${sales_total}, {
      name} will recieve ${commission_amount}")
