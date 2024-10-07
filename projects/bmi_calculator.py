"""
    Calculates BMI based on user input
"""

# global variables

# converts from pounds to kilos
global KILO_CONVERSION
KILO_CONVERSION = 0.453592
# converts from inches to meters
global METER_CONVERSION
METER_CONVERSION = 0.0254

# main function


def main():

    # get data from user
    user_weight = float(input("\nWhat is your weight in pounds? "))
    user_height = float(input("\nHow tall are you in inches? "))

    # using conversions
    user_weight_metric = user_weight * KILO_CONVERSION
    user_height_metric = user_height * METER_CONVERSION

    # calculating BMI
    bmi = user_weight_metric / (user_height_metric ** 2)

    print(f"\nYou have a BMI of {bmi:.2f}")

    # categorizes user BMI and prints category to terminal
    if bmi < 18.5:
        print("\nYou are underweight.\n")
    elif 18.5 <= bmi <= 24.9:
        print("\nYou are a normal weight.\n")
    elif 25 <= bmi <= 29.9:
        print("\nYou are overweight.\n")
    else:
        print("\nYou are obese.\n")


# call main function
main()
