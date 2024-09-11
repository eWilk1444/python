"""
    This program will assign a letter grade - A through F - to the user based on the integer they enter.
"""

# variables
grade_number = int(input("Enter your grade as a whole number"))
# logic
if grade_number < 60:
    print("The equivilent letter grade would be a: F")
elif grade_number <= 69:
    print("The equivilent letter grade would be a: D")
elif grade_number <= 79:
    print("The equivilent letter grade would be a: C")
elif grade_number <= 89:
    print("The equivilent letter grade would be a: B")
elif grade_number >= 90:
    print("The equivilent letter grade would be a: A")
else:
    pass
