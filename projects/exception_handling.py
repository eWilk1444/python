"""
    This program works, but I really want to have an independent function specifically for error checking.
    I would greatly appreciate it if you could show me how to do that for this specific program.
    (if you're reading this during the week of 10/14, hope you feel better soon!)
"""


# Simple Python program to calculate the square of a number

def square_number():
    """
    This function squares a inputted number and checks for bad input
    """
    number = input("Enter a number to square: ")
    try:  # ChatGPT was pretty unhelpful, but worth a shot anyways https://chatgpt.com/share/670d6e2f-6838-800f-ac70-2b48e8291c6a
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:  # when error is recieved, ask if they want to try again
        print(
            f"ERROR: Non-number input has been detected.")
        try_again = input(
            "Would you like to try again? Please type 'Yes' or 'No' to proceed. ")
        try_again_upper = try_again.upper()
        if try_again_upper == "YES":  # if yes, invoke main
            main()
        elif try_again_upper == "NO":  # if no, leave
            exit()
        else:  # if bad input, ask again with further clarification
            print(
                "Please enter 'Yes' to attempt entering another number, or 'No' to end the program.")

# calling function square_number


def main():
    square_number()


# invoking main
main()
