"""
Python program that prompts the user to enter a password and validates it against specific criteria

Set up your program in a main() function
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.
"""


def main():
    password = str(input("Please enter a password that:\nIs between 8 and 20 characters\nContains at least one capital letter\nContrains at least one lowercase letter\nIncludes at least one number\nContains one symbol from this list: '!@#$%&*'\n"))
    bool(capital) = False
    bool(lower) = False
    bool(number) = False
    bool(symbol) = False
    for letter in password:
        if letter.isupper() = True:
            capital = True
        else:
            capital = False
        if letter.islower() = True:
            lower = True
        else:
            lower = False
        if letter is int:
            number = True

# iterates through each letter and sets a flag if condition is true, otherwise it's false

    if 8 > len(password):
        print("The password is too short. Please try again.")
        main()
    elif 20 < len(password):
        print("The password is too long. Please try again.")
    elif password


main()
