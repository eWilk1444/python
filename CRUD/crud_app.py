"""
    Create, Read, Update, Delete
"""


def menu(user):
    print("Welcome, please select an option from the following.")
    # display options, accept number, then call functions
    print("1. Search for and display a record")
    print("2. Create a new record")
    print("3. Update an existing record")
    print("4. Delete a record")
    print("5. Quit")


def check_for_file():
    print("Checking if file exists...")


def save_to_file():
    print("Saving to file...")


def create_record():
    print("Creating record...")


def read_file():
    print("Reading file...")


def find_in_file():
    print("Finding record in file...")


def update_file():
    print("Updating file...")


def delete_from_file():
    print("Deleting record from file...")


def display_record():
    print("Displaying record...")


def main():
    # menu for user
    # user will be the list of records
    user = check_for_file()  # check if file exists, yes = copy, no = create
    menu(user)

    # check_for_file()  # does it exist, else create

    # save_to_file()  # save list to file

    # create_record()  # creating new record

    # read_file()  # read from file

    # find_in_file()  # get record and display

    # update_file()  # change previous record

    # delete_from_file()  # delete record

    # display_record()  # display record


main()
