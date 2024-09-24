"""
    Logs steps for each day
"""

days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []

print("\nHello! Please enter the amount of steps you took on each of the days of the week.\n")
# user data entered into list 'steps' for each day in list 'days'
for i in range(len(days)):
    day = days[i]
    steps.append(input(f"How many steps did you take on {day}? "))

print()  # for spacing
# prints 'steps' list to terminal
for i in range(len(steps)):
    day = days[i]
    step = steps[i]
    # prints each iteration to terminal
    print(f"You took {step} steps on {day}.")
print()

# grabs steps and averages them
for i in range(len(steps)):
    total = total + steps[i]
    print(total)

average = round(total / len(steps))
