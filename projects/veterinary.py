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
    https://chatgpt.com/share/67350c84-d758-800f-9ced-04f469e0760c
    https://chatgpt.com/share/6738146a-aca8-800f-b965-513a20e1e04d 
    """

class Pet:

    # class variable
    vet_name = "Purr-fect Vetrinary Clinic"

    # initializing class
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # generated using 'Python Getter Setter' extention
    @property
    def owner_first_name(self):
        return self.__owner_first_name

    @owner_first_name.setter
    def owner_first_name(self, value):
        self.__owner_first_name = value

    @property
    def owner_last_name(self):
        return self.__owner_last_name

    @owner_last_name.setter
    def owner_last_name(self, value):   
        self.__owner_last_name = value

    @property
    def pet_id(self):
        return self.__pet_id

    @pet_id.setter
    def pet_id(self, value):
        self.__pet_id = value

    @property
    def pet_name(self):
        return self.__pet_name

    @pet_name.setter
    def pet_name(self, value):
        self.__pet_name = value

    @property
    def pet_type(self):
        return self.__pet_type

    @pet_type.setter
    def pet_type(self, value):
        self.__pet_type = value

    # method that prints individual pet object vars to terminal
    def display_pet_info(self):
        print("Pet details:", vars(self))

# checks pet for specific property
def check_property(pet, attribute):
    return hasattr(pet, attribute)


def main():
    pet_1 = Pet("John", "Doe", "902453", "Mr. Snake", "Bird")
    pet_2 = Pet("Jane", "Doe", "025304", "Spot")
    pet_3 = Pet("Mark", "Jacobs" , "657842",
                "GE Top-Loading Washing Machine", "Cat")
    
    # changing pet_type for Mr. Snake (pet_1)
    pet_1.pet_type = "Snake"

    # printing pets to terminal
    pet_1.display_pet_info()
    pet_2.display_pet_info()
    pet_3.display_pet_info()

    # checking properties
    print(f"pet_1 has a pet ID: {check_property(pet_1, 'pet_id')}.")
    print(f"pet_2 has the name of the vet attatched: {check_property(pet_2, "vet_name")}.") # class var so it should be 'True' as the class variable is always included in the objects
    print(f"pet_3 has an owner with the last name 'Donnerman': {check_property(pet_3, "Donnerman")}.")


main()
