"""
    Create, Read, Update, Delete
"""
import os


def menu(user):
    try:
        print("Welcome, you have the following options.")
        choice = 0
        while choice != 5:
            # display options, accept number, then call functions
            print("1. Search for and display a record")
            print("2. Create a new record")
            print("3. Update an existing record")
            print("4. Delete a record")
            print("5. Quit")
            choice = int(
                input("Enter the number associated with your selection: "))
            if choice == 1:
                display_record(user)
            elif choice == 2:
                create_record(user)
            elif choice == 3:
                update_file(user)
            elif choice == 4:
                delete_record(user)
            elif choice == 5:
                print("Program terminated")
            else:
                print("Please enter a number between 1 and 5")
    except Exception as e:
        print(f"Error: {e}")


def check_for_file():  # used to check for file, gets list if it exists
    print("Checking if file exists...")
    try:
        with open("user_data.txt", 'r') as file:
            user = file.readlines()
            return user
    except FileNotFoundError:
        user = []
        return user
    except Exception as e:
        print(f"Error: {e}")


def create_record(user):
    # create record, call save_to_file to save to user_data.txt
    print("Creating record...")
    first_name = input("Enter the first name of person: ").capitalize()
    last_name = input("Enter the last name of person: ").capitalize()
    phone_number = input(
        "Enter the phone number of person, do not include country codes (USA = 1) and use hyphens (123-456-7890): ")
    record = first_name + "," + last_name + "," + phone_number + "\n"
    user.append(record)
    # print(user)
    save_to_file(user)


def save_to_file():
    # call when record is saved
    #
    print("Saving to file...")
    try:
        with open("user_data.txt", 'w') as file:
            for line in user:
                file.write(line)
        file.close()
        print(user)
        print("Saved successfully")
    except Exception as e:
        print(f"idk lmao, {e}")


# def read_file(user):
#     print("Reading file...")
# not really necessary for function, positional arguments are better
# low priority

def find_in_file(user):
    # find user, return index of user
    # search by phone number
    # TODO for V2 - allow searching by first/last name
    print("Finding record in file...")
    phone = input(
        "Please enter the phone number for the person you wish to find (include hyphens and do not include country code): ")
    my_index = 0
    for line in user:
        line = line.strip("\n")
        record = line.split(',')
        print("record")
        if record[2] == phone:
            print("Record found at index", line)
            return my_index
        else:
            my_index += 1
    print("Record not found for phone number: " + phone)


def update_file(user):
    print("Updating file...")
    find_in_file(user)


def delete_record(user):
    print("Deleting record from file...")


def display_record(user):
    print("Displaying record...")


def main():
    # menu for user
    # user will be the list of records
    user = check_for_file()  # check if file exists, yes = copy, no = create
    print(user)
    menu(user)

    # check_for_file()  # does it exist, else create

    # save_to_file()  # save list to file

    # create_record()  # creating new record

    # read_file()  # read from file

    # find_in_file()  # get record and display

    # update_file()  # change previous record

    # delete_record()  # delete record

    # display_record()  # display record


main()
