"""
Implement a custom exception class NotNumericError.
Write a Python script that prompts the user to input a number.
Use a try-except-else-finally block:
The try block should contain the logic to check if the input is a number. (isnumeric() )
The except block should catch the InvalidInputError and print an error message.
The else block should print a confirmation message if the input is valid.
The finally block should print a message indicating the end of the program's execution.
Ensure the program gracefully handles the exception and continues to prompt the user until a valid number is entered. (call the program again)
https://chatgpt.com/share/67450da2-d754-800f-81d3-91d433445867 
"""


class NotNumericNumber(Exception):
    def __init__(self, message="That is not a number. Please try again."):
        self.__message = message

    # generated using Python Getter Setter
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value


def test():

    valid = False
    while valid == False:
        number = input("Please enter a number: ")
        if number.isnumeric():
            valid = True
            return number
        else:
            raise NotNumericNumber()


def main():
    try:
        test()
    except NotNumericNumber as e:
        error_message = e.message
        print(error_message)
        main()
    else:
        print("That is a valid number.")
    finally:
        print("Program terminated.")


main()
