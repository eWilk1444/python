"""
Assignment Part 1: Defining Classes
File 1: Write an Employee class with the following attributes:

Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class.

Assignment Part 2: Implementing and Testing


Part 2: Write a script to:

Create an instance of ProductionWorker.
Prompt the user for each attribute's data.
Store and then display the data using the object's methods.
https://chatgpt.com/share/673e4291-21f0-800f-a78c-af87e58cd820 
"""


class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # generated using Python Getter Setter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    def __str__(self):
        return f"Employee(Name: {self.__name}, Employee Number: {self.__number}"

# subclass of Employee


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    # generated using Python Getter Setter
    @property
    def shift(self):
        return self.__shift

    @shift.setter
    def shift(self, value):
        self.__shift = value

    @property
    def pay_rate(self):
        return self.__pay_rate

    @pay_rate.setter
    def pay_rate(self, value):
        self.__pay_rate = value

    def __str__(self):
        return f"{super().__str__()}, Shift: {self.__shift}, Wage: {self.__pay_rate})"


def main():

    try:
        name = input("\nPlease enter employee's name: ")
        number = input("\nPlease enter employee's number: ")
        shift = int(input(
            "\nPlease employee's shift time - enter 1 for daytime, or 2 for nighttime: "))
        pay_rate = input(
            "\nPlease enter employee hourly wage, do not enter symbols such as the dollar sign: ")
    except ValueError:
        print("\nPlease enter 1 for daytime shift, or 2 for nighttime shift.")
        main()

    prod_worker_1 = ProductionWorker(name, number, shift, pay_rate)
    print(prod_worker_1)


main()
