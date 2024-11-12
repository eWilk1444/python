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

https://chatgpt.com/share/6732b18f-600c-800f-a508-24a4b32f89d3
"""
# Developer's note: It's been 4 hours since I started this accursed project. My patience wears thin and I feel the urge to give up. I am beginning to feel as though CS is not for me, but I know that to be untrue. I must perservere.
# This is about 30 mintues after my previous log. I over-relied on ChatGPT. It was finding errors where there were none because the program would've worked over an hour ago >:( A cautionary tale to be certain.

def main():
    # validates password by iterating through letters while checking for conditions and password length before asking for a re-entry of the password.
    valid = False
    capital = False
    lower = False
    number = False
    symbol = False
    not_too_short = False
    not_too_long = False

    while valid == False:
        password = input_password() # getting password
        
        if len(password) >= 8: # checking length
            not_too_short = True
        if len(password) <= 20:
            not_too_long = True
        
        for letter in password: # primary loop for checking conditions
            if letter.isupper():
                capital = True
            if letter.islower():
                lower = True
            if letter.isnumeric():
                number = True
            if letter in "!@#$%&*":
                symbol = True

        # error logs for the user to diagnose the problem with their password
        if not_too_long == False:
            print("\nThat password is too long.")
        if not_too_short == False:
            print("\nThat password is too short.")
        if capital == False:
            print("\nPlease include a capital letter.")
        if lower == False:
            print("\nPlease include a lowercase letter.")
        if number == False:
            print("\nPlease include a number.")
        if symbol == False:
            print("\nPlease include a symbol from the list.")
                    
        if capital and lower and number and symbol and not_too_short and not_too_long:
            valid = True # break loop if valid
        else:
            main() # re-do if not valid
            
    if valid == True:
        second_password = input("\nPlease re-enter your password:\n")
    
    if second_password == password:
        print("\nYour password has been set.")
    else:
        print("\nThe passwords did not match.\n")
        main()

def input_password():
    # this gets a password from the user to start, and when the user inputs an invalid password
    return input("\nPlease enter a password that:\nIs between 8 and 20 characters\nContains at least one capital letter\nContrains at least one lowercase letter\nIncludes at least one number\nContains one symbol from this list: '!@#$%&*'\n")

# invoking main
main()
