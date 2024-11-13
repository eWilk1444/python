"""
    Define a Pet Class:
Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
Set a default value for pet_type as "Dog".
Implement getter and setter methods for all properties.
Include a class variable vet_name set to the name of your veterinary office.
Add a method display_pet_info to print all details of the pet and owner.
Create Pet Objects:
Instantiate at least three pet objects with different details.
Show the use of setter methods for at least one pet object.
Implement Property Existence Check:
Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
Display Information:
Use display_pet_info to print details for each pet.
Show examples of check_property being used on various properties and pets.
    """


class Pet:

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # generated using 'Python Getter Setter' extention
    @property
    def _owner_first_name(self):
        return self.__owner_first_name

    @_owner_first_name.setter
    def _owner_first_name(self, value):
        self.__owner_first_name = value

    @property
    def _owner_last_name(self):
        return self.__owner_last_name

    @_owner_last_name.setter
    def _owner_last_name(self, value):
        self.__owner_last_name = value

    @property
    def _pet_id(self):
        return self.__pet_id

    @_pet_id.setter
    def _pet_id(self, value):
        self.__pet_id = value

    @property
    def _pet_name(self):
        return self.__pet_name

    @_pet_name.setter
    def _pet_name(self, value):
        self.__pet_name = value

    @property
    def _pet_type(self):
        return self.__pet_type

    @_pet_type.setter
    def _pet_type(self, value):
        self.__pet_type = value

    def print_pet_details(self):
        print("Pet details:", vars(self))


def main():
    pet_1 = Pet("John", "Doe", "902453", "Mr.Scaly", "Reptile")
    pet_2 = Pet("Jane", "Doe", "025304", "Spot")
    pet_3 = Pet("Mark", "Konnerman", "657842",
                "GE Top-Loading Washing Machine", "Cat")
    pet_1._pet_type("Cat")
    print(print_pet_details())


main()
