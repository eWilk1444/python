"""
    randomly generates number for user to guess and provides feedback
"""

import random
global GEN_NUMBER
GEN_NUMBER = random.randint(0, 101)


def user_input():
    try:
        guessed_number = int(
            input("\nGuess a number between 1 and 100, including 1 and 100: "))
    except ValueError:
        print(f"\nError! Please enter a whole number: ")
        user_input()
    except TypeError as t:
        print(f"\nError! Please enter a number: ")
        user_input()
    else:
        return guessed_number


def main():
    guessed_number = user_input()
    distance_from_guess = abs(guessed_number - GEN_NUMBER)

    if distance_from_guess == 0:
        print(f"\nCongrats! {guessed_number} was the number!\n")
    elif distance_from_guess <= 5:
        print("\nVery Hot!")
        main()
    elif distance_from_guess <= 15:
        print("\nHot.")
        main()
    elif distance_from_guess <= 25:
        print("\nCool..")
        main()
    else:
        print("\nCold...")
        main()


main()
