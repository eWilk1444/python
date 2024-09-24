"""
    Checks number 1 through 300 to see if they are divisble by 7, then prints them.
"""
# variable to store numbers in the list below
number = 300

# Main logic/loop
for number in range(1, 300):
    if number % 7 == 0:
        print(number)
    else:
        continue  # skips numbers with modulus remainder not == to 0
