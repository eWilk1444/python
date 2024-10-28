"""
    Fidning the ASCII values of strings
"""


def main():
    user_input = input("Enter a character: ")
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")


main()
