"""
    Create the Pet Class:
        Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
        Implement get and set methods for each of these attributes.
        Add a method called print_details that prints the details of the pet.
    Create Instances:

    Create three objects of the Pet class with different kinds, breeds, and names.

    Call the print_details method for each object that you created
    Demonstrate a Special Method or Function:

    Choose three of the following and demonstrate its use with the Pet class instances:
        __name__: Display the name of the class.
        type(): Show the class used to instantiate a pet object.
         __module__: Return the module name in which the Pet class is defined.
        __bases__: Display the base classes of the Pet class (if any).
        getattr(): Use it to access an attribute of a Pet instance.
        isinstance(): Check if an instance is of the Pet class.

        https://chatgpt.com/share/67381c6a-b968-800f-a451-ca995a3aefa1 
"""

class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # generated using 'Python Getter Setter'
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, value):
        self.__breed = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # function that prints vars to terminal
    def print_details(self):
        print(f"Pet details: {vars(self)}")

    # checks attributes and prints to terminal
    def check_pet_info(self):
        print(f"The name of the class associated with pet_1 - pet_3 is: {self.__class__.__name__}")
        print(f"The module associated with the Pet class: {self.__class__.__module__}")
        print(f"Is this object an instance of the Pet class: {isinstance(self, Pet)}\n")


# main logic, creates pet objects and then uses methods to check specific attributes
def main():
    pet_1 = Pet("Dog", "Border Collie", "Piper")
    pet_2 = Pet("Cat", "Siamese Sealpoint", "Cookie")
    pet_3 = Pet("Dog", "Chocolate Labrador", "Kasey")

    # tuple because it doesn't change
    pets_tuple = (pet_1, pet_2, pet_3)
    for pet in pets_tuple:
        pet.print_details()
        pet.check_pet_info()

# invoking main
main()