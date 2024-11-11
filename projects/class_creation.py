"""
Creates the 'Person' class
"""


class Person:
    # initalize private variables
    def __init__(self, name, address, age, phone):
        """initalizing name, address, age, and phone variables

        Args:
            name (str): name of the person
            address (str): address of the person
            age (int): age of the person
            phone (str): phone number of the person
        """
        self.__name = name          # private var for name
        self.__address = address    # private var for address
        self.__age = age            # private var for age
        self.__phone = phone        # private var for phone number

    # getter for name
    def get_name(self):
        return self.__name

    # getter for address
    def get_address(self):
        return self.__address

    # getter for age
    def get_age(self):
        return self.__age

    # getter for phone
    def get_phone(self):
        return self.__phone

    # setter for name
    def set_name(self, name):
        self.__name = name

    # setter for address
    def set_address(self, address):
        self.__address = address

    # setter for age
    def set_age(self, age):
        self.__age = age

    # setter for phone
    def set_phone(self, phone):
        self.__phone = phone


def main():
    # name and age will be real, other things will not be
    person_1 = Person("Ethan", "123 Alphabet Road", "21", "815-422-1836")
    person_2 = Person("Matt", "224 North Randall Road", "25", "224-598-1444")
    person_3 = Person("Dilan", "1346 West Northbrook Court",
                      "20", "630-273-4381")
    print(  # i'm aware that this phrasing is clunky, but the assignment wanted each bit of information printed
        f"{person_1.get_name()}'s name is: {person_1.get_name()} \
        \n{person_1.get_name()}'s address is: {person_1.get_address()} \
        \n{person_1.get_name()}'s age is: {person_1.get_age()} \
        \n{person_1.get_name()}'s phone number is: {person_1.get_phone()}\n"
    )
    print(
        f"{person_2.get_name()}'s name is: {person_2.get_name()} \
        \n{person_2.get_name()}'s address is: {person_2.get_address()} \
        \n{person_2.get_name()}'s age is: {person_2.get_age()} \
        \n{person_2.get_name()}'s phone number is: {person_2.get_phone()}\n"
    )
    print(
        f"{person_3.get_name()}'s name is: {person_3.get_name()} \
        \n{person_3.get_name()}'s address is: {person_3.get_address()} \
        \n{person_3.get_name()}'s age is: {person_3.get_age()} \
        \n{person_3.get_name()}'s phone number is: {person_3.get_phone()}\n"
    )


main()
