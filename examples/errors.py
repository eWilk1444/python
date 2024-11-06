"""
    errors and stuff
"""


def main():
    try:
        number = float(input("Enter a number: "))
        result = 10 / number
        print(float(result))
    except ZeroDivisionError:
        print("Oops! Can't divide by zero. Try a different number.")
        main()
    except ValueError:
        print("oh no! That isn't a number! Please enter a number")
        main()
    except:
        print("That isn't a valid input!")
        print("idk why this crashed lmao")
        main()


main()
