"""
    Looping 
"""

# Dont!
# While True:

# Do
# count = 10

# while count >= 0:
#     print(count)
#     count -= 1

# in c++
# for (int i = 0; i >= 0; i++):

# for i in range(1, 12, 2):
#     print(i)

# weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday",
#             "Thursday", "Friday", "Saturday")

# for day in (weekdays):
#     print(day)

# for number in [1, 2, 3, 4, 5]:
#     if number == 3:
#         break
#     print(number)

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        continue
    print(number)

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed without break")
