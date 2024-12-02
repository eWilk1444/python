"""
Your program must be contained within a main() function.
Use the Python input() function to ask the user for their birth month (as an integer).
Ensure your program can handle invalid inputs gracefully.
Use Python's datetime module to find the current year.
Generate and display the calendar for the user's birth month in the current year.
Format the calendar output so it is easy to read and understand.


Steps
Start by importing the necessary modules: calendar and datetime.
Create a main() function where your program's logic will reside.
Inside main(), get the current year using datetime.datetime.now().year.
Ask the user to enter their birth month and store it in a variable.
Validate the user input to ensure it's an integer between 1 and 12.
Use the Calendar module to generate the calendar for the given month and year.
Print the calendar to the console in a readable format.
Don't forget to call the main() function at the end of your script.

    """


import calendar
import datetime


def main():
    try:
        current_year = datetime.datetime.now().year  # get current year
        cal = calendar.Calendar()  # initalize calender object for convenient formatting
        birth_month = int(
            input("\nPlease enter your birth month: Jan = 1, Feb = 2, etc.  "))
        if 1 <= birth_month <= 12:  # makes sure that birth_month is a legitimate value for a calender to display
            print(calendar.month(current_year, birth_month))
        else:
            raise ValueError  # if not, it's not a real, positive number so raise exception
    except ValueError:
        print("\nPlease only enter positive, real numbers.")
    except Exception as e:  # catches if they turn off the computer or their CPU explodes or something
        print(f"\nError: {e}")


# invoking main
main()
