"""
    Creates a list of 1-20 seats, and prompts user to select seats to purchase
"""

available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
all_wanted_seats = []

print("\nHello! Please choose a seat from the following list and enter it as a integer. Thank you for your cooperation.\n")
wanted_seat = 21

# if seats are available and they haven't finished their purchase, ask what seat they want
# while len(available_seats) > 0 and wanted_seat != 0:
#     print(f"The available seats are: {available_seats}")
#     wanted_seat = int(input("\nWhat seat would you like to purchase? "))
#     if wanted_seat in available_seats and wanted_seat != 0:
#         available_seats.remove(wanted_seat)
#         all_wanted_seats.append(wanted_seat)
#         print(f"\nYou have reserved seat {
#               wanted_seat}. Enter 0 if you are finished with your purchase.")
#         # https://chatgpt.com/share/66f45d4c-d1c0-800f-a4fe-60fec9e8e4aa
#     else:
#         print("\nSorry! That seat is unavailable. Please select another seat or enter 0 to end the transaction.\n")

while len(available_seats) > 0:
    print(f"The available seats are: {available_seats}")
    wanted_seat = int(input("What seat would you like to purchase? "))
    if wanted_seat in available_seats:
        available_seats.remove(wanted_seat)
        all_wanted_seats.append(wanted_seat)
        print(f"\nYou have reserved seat {
            wanted_seat}. Enter 0 if you are finished with your purchase.")
    # https://chatgpt.com/share/66f45d4c-d1c0-800f-a4fe-60fec9e8e4aa
    elif wanted_seat == 0:
        print(f"The seat(s) you have reserved are: {all_wanted_seats}.")
        print("Thank you for your patronage.")
    else:
        print("\nSorry, that seat is unavailable.\n")

# if wanted_seat != 0:
#     wanted_seat in available_seats and wanted_seat != 0:
#     available_seats.remove(wanted_seat)
#     all_wanted_seats.append(wanted_seat)
#     print(f"\nYou have reserved seat {
#         wanted_seat}. Enter 0 if you are finished with your purchase.")
#     # https://chatgpt.com/share/66f45d4c-d1c0-800f-a4fe-60fec9e8e4aa
#     else:
#         print("\nSorry! That seat is unavailable. Please select another seat or enter 0 to end the transaction.\n")

# while len(available_seats) > 0:
#     wanted_seat = int(input("\nWhat seat would you like to purchase? "))

# # if no seats available, gives message to user
# if len(available_seats) == 0:
#     print("\nSorry! This venue has been completely booked.")
