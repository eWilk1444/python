# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week

from datetime import datetime


def main():

    print("")
    try:
        today = datetime.today()
        birth_year = int(
            input("What year were you born? (4 digits, ex. 1985)  "))
        month = int(
            input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output)

        delta = today - birthday  # total time between today and birthday
        print(f'Difference is {delta.days} days')
        # calculate time intervals for print statements
        delta_years = delta.days // 365.2425
        delta_months = delta.days // 30.41
        delta_weeks = delta.days // 7
        # let user know calculations
        print(f'Difference is {delta_weeks} weeks')
        print(f'Differnece is {delta_months} months')
        print(f'You are {delta_years} years old')

    except ValueError:  # for when user enters letters/symbols instead of numbers
        print("\nPlease only enter numbers. ")
        main()

    except Exception as e:
        print(f"\nooooops!!!:  {e}")
        main()


main()
