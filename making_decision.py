"""
    This program will ask the user's age and determine 
    if they are old enough for a variety of age-related activities and benefits
"""

# variables
age = input("How old are you? ")
senior = False
alchohol = False
vote = False
drive = False

print(senior)

# logic
if int(age) >= 65:
    senior = True
elif age >= 21:
    alchohol = True
elif age >= 18:
    vote = True
elif age >= 16:
    drive = True
else:
    senior = False
    alchohol = False
    vote = False
    drive = False
