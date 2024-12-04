

def main_menu():
    print("Menu:")
    while True:
        try:
            print("\\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")


def check():
    print("Checking the system...")


def create():
    print("Creating a new entry...")


def read():
    print("Reading an entry...")


def update():
    print("Updating an entry...")


def delete():
    print("Deleting an entry...")


def check():
    try:
        file = open("customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []


def create():
    customer = check()
    fname = input("Please enter the customer\'s first name: ")
    lname = input("Please enter the customer\'s last name: ")
    phone = input("Please enter the customer\'s phone: ")
    email = input("Please enter the customer\'s email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\\n"
    customer.append(entry)
    save(customer)


def save(output):
    file = open("customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.")
