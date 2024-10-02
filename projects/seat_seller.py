"""
    Creates a list of 1-20 seats, and prompts user to select seats to purchase
"""

available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
all_wanted_seats = []

print("\nHello! Please choose a seat from the following list and enter it as a integer. Thank you for your cooperation.\n")
wanted_seat = 21

while len(available_seats) > 0 and wanted_seat != 0:
    print(f"The available seats are: {available_seats}")
    wanted_seat = int(input("What seat would you like to purchase? "))
    if wanted_seat in available_seats:
        available_seats.remove(wanted_seat)
        all_wanted_seats.append(wanted_seat)
        print(f"\nYou have reserved seat {
              wanted_seat}. Enter 0 if you are finished with your purchase.")
    # if wanted_seat in available_seats:
    #     available_seats.remove(wanted_seat)
    #     all_wanted_seats.append(wanted_seat)
    #     print(f"\nYou have reserved seat {
    #           wanted_seat}. Enter 0 if you are finished with your purchase.")
    # https://chatgpt.com/share/66f45d4c-d1c0-800f-a4fe-60fec9e8e4aa
    elif wanted_seat == 0:
        print(f"\nThe seat(s) you have reserved are: {all_wanted_seats}.")
        print("\nThank you for your patronage.\n")
    else:
        print("\nSorry, that seat is unavailable.\n")
