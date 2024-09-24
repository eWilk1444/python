"""
    Asks user for two integers
    compares them and prints results of multiple
    tests to screen
"""

# creating variables for storing user input
num1 = int(input("Please enter an integer: "))
num2 = int(input("\nPlease enter another integer: "))

print("Are both integers less than 0? ")
if num1 < 0 and num2 < 0:
    print("True")
else:
    print("False")

print("are both integers even? ")
if num1 % 2 == 0 and num2 % 2 == 0:
    print("True")
else:
    print("False")
# got some help from Chat GPT https://chatgpt.com/share/66f2192b-1c1c-800f-8964-8585c047bace, helped me understand precedence

print("Are either integers the number 42? ")
if num1 == 42 or num2 == 42:
    print("True")
else:
    print("False")

print("Are either integers less than 1000? ")
if num1 < 1000 or num2 < 1000:
    print("True")
else:
    print("False")

print("Are the integers the same? ")
if not num1 == num2:
    print("False")
else:
    print("True")

print("Is the first integer larger than the second, but also larger than 3? ")
if not num1 > num2 > 3:
    print("True")
else:
    print("False")