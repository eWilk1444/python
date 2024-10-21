"""
    Calculates factorials of numbers inputted by user
"""

# calculates factorial using a recursive loop
def calculate_factorial(number):
    if number < 0:
        return number
    elif number == 0:
        return 1
    else:
        return (number * calculate_factorial(number - 1))

# main logic invokes calculate_factorials function, prints results to terminal
def main():
    number = int(input("\nPlease enter a integer to find the factorial of. "))
    total = calculate_factorial(number)
    print(f"\nThe factorial of {number} is {total}. \n")
# https://chatgpt.com/share/670dc529-49d4-800f-8b40-e131e5385f03 ChatGPT loves to write code, need to tell it everytime to not do it!
# It did remind me to store data in the main function, so that was helpful.

# invoking main function
main()