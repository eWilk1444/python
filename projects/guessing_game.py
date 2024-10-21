"""
    randomly generates number for user to guess and provides feedback
"""

import random


def number_generator():
    number = random.randint(0, 101)
    return number


def user_input():
    try:
        guessed_number = int(
            input("\nGuess a number between 1 and 100, including 1 and 100. "))
    except ValueError:
        print(f"\nError! Please enter a whole number. ")
        user_input()
    except TypeError as t:
        print(f"\nError! Please enter a number. ")
        user_input()
    else:
        return guessed_number


def main():
    gen_number = number_generator()
    guessed_number = user_input()
    absolute = abs(guessed_number - gen_number)

    if absolute == 0:
        print(f"\nCongrats! {gen_number} was the number!")
    elif absolute <= 5:
        print("\nVery Hot!")
        main()
    elif absolute <= 15:
        print("\nHot.")
        main()
    elif absolute <= 25:
        print("\nCool..")
        main()
    else:
        print("\nCold...")
        main()


main()
