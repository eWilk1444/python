"""
    This program will ask the user's age and determine 
    if they are old enough for a variety of age-related activities and benefits
"""

# variables
age = int(input("How old are you? "))  # asks user for their name as a integer
# all bools are false by default because I wanted to use booleans as opposed to manually putting the prints in
# this is more complicated than necessary but I felt like it so yeah
drive = bool(False)
vote = bool(False)
drink = bool(False)
senior = bool(False)

# logic
if age >= 65:  # checks if age is less than 16
    senior = bool(True)
    drink = bool(True)
    vote = bool(True)
    drive = bool(True)
elif age >= 21:  # checks if age is less than 18
    drink = bool(True)
    vote = bool(True)
    drive = bool(True)
elif age >= 18:  # checks if age is less than 21
    vote = bool(True)
    drive = bool(True)
elif age >= 16:  # checks if age is less than 65
    drive = bool(True)
else:  # catch-all for anybody under 16, all conditions are true by default therefore no change
    # this pass command returns the function with no edits to the bools (thanks Google!)
    pass

# logic for the booleans and printing to the terminal
if drive == bool(True):  # executes when user is over or is exactly 16
    print("You are old enough to drive.")
else:
    print("You cannot drive.")

if vote == bool(True):  # executes when user is over or is exactly 18
    print("You are old enough to vote")
else:
    print("You cannot vote.")

if drink == bool(True):  # executes when user is over or is exactly 21
    print("You can buy alchohol and tobacco")
else:
    print("You cannot purchase alchohol or tobacco")

if senior == bool(True):  # executes when user is over or is exactly 65
    print("You are eligible for a senior's discount")
else:
    print("You are not eligible for a senior's discount")
