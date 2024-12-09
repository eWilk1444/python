"""
    Create, Read, Update, Delete
"""
import os


def menu(user):
    try:
        user = check_for_file()
        print(customer)  # for errors
        print("Welcome, you have the following options:")
        choice = 0
        while choice != 5:
            # display options, accept selection, then call functions
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
    email = input(
        "Enter the email of person, including the @ sign and web address ending (@gmail.com, @hotmail.com, etc.): ")
    record = first_name + "," + last_name + "," + email + "\n"
    user.append(record)
    # print(user) # testing function
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
        print(f"idk lmao something broke, {e}")


# def read_file(user):
#     print("Reading file...")
# not really necessary for function, positional arguments are better
# low priority

def find_in_file(user):
    # find user, return index of user
    # search by email number
    # TODO for V2 - allow searching by first/last name
    print("Finding record in file...")
    email = input(
        "Please enter the email for the person you wish to find: ")
    my_index = 0
    for line in user:  # each line in user, this loop happens
        line = line.strip("\n")
        # seperates each element (first name, last name, email)
        record = line.split(',')
        print("record")
        # if email from record is same as email input, print confirmation and return index
        if record[2] == email:
            print("Record found at index", line)
            return my_index
        else:  # otherwise, continue until end of list
            my_index += 1
    print("\nRecord not found for email:" + email)
    return "I'm sorry, that record does not exist\n"


def update_file(user):
    try:
        print("Updating file...")
        desired_user = find_in_file(user)
        new_user_details = user[desired_user].split(",")
        for item in new_user_details:
            print(item)
        if isinstance(user, str):
            print(desired_user)
        if isinstance(user, int):
            print("Account found!")
            print(f"The record is: {user[desired_user]}")
        else:
            print(f"Record not found! {user}")

        # changing items in list menu
        choice = True
        while choice:
            print("1: Change First Name\n2:Change Last Name\nChange Email\n")
            choice = int(
                input("Please select an option from the list above: "))

            if choice == 1:
                first_name = input("Enter new first name: ")
                new_user_details[0] = first_name
                choice = False
            elif choice == 2:
                last_name = input("Enter new last name: ")
                new_user_details[1] = last_name
                choice = False
            elif choice == 3:
                email = input("Enter new email: ")
                new_user_details[2] = email
                choice = False
            else:
                print("That is not a valid choice.")
                choice = False

        print(new_user_details, "Is the updated record")
        user_details = (",").join(new_user_details)
        user[desired_user] = user_details
        save_to_file(user)

    except Exception as e:
        print(f"Invalid menu choice, {e}")


def delete_record(user):
    print("Deleting file...")
    find_in_file(user)
    # call search, get index
    # pop index
    # call save, passing 'user'


def display_record(user):
    print("Displaying record...")
    my_index = find_in_file(user)
    # call search, get index
    # print formatted record


def main():
    # menu for user
    # user will be the list of records
    print(user)
    menu()

    # check_for_file()  # does it exist, else create

    # save_to_file()  # save list to file

    # create_record()  # creating new record

    # read_file()  # read from file

    # find_in_file()  # get record and display

    # update_file()  # change previous record

    # delete_record()  # delete record

    # display_record()  # display record


main()
