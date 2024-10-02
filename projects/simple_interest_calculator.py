"""
    Calculates annual simple interest
"""

# greets user
print("*" * 50)
print("Hello. Thank you for using our interest calculating software.")
print("*" * 50)

# prompts user to input necessary data
principal = float(input(
    "\nPlease enter the principal amount: "))
rate = float(input(
    "\nPlease enter the annual rate, for example, 5% would be entered as '5': "))
time = float(input(
    "\nPlease enter the amount of years the principal will be accruing interest: "))


def calculate_interest(principal, rate, time):
    """This function calculates simple interest from user-inputted data

    Args:
        principal (float): amount of money
        rate (float): whole number representation of a percent
        time (float): number of years the principal has accrued non-compounding interest

    Returns:
        float: result of simple interest formula
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest


# invoking interest calculating function and print to terminal
simple_interest_total = calculate_interest(principal, rate, time)
print(f"The simple interest for a principal amount of ${principal:.2f} \
at an interest rate of {rate}%, over a period of {time} years is \
${simple_interest_total:.2f}. ")

# wasn't very helpful... https://chatgpt.com/share/66fd97fb-a538-800f-8230-ebeaad6ceeac
# It peeves me to have the text in the same indent as the print function but it works so whatever
