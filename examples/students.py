# Class definition
class Student:
    # Class variable
    school_name = "McHenry County College"

    def __init__(self, first_name, last_name, student_id, grade_level="Freshman"):
        # Instance variables
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade_level = grade_level

    # generated with 'Python Getter and Setter' extention
    @property
    def _first_name(self):
        return self.__first_name

    @_first_name.setter
    def _first_name(self, value):
        self.__first_name = value

    @property
    def _last_name(self):
        return self.__last_name

    @_last_name.setter
    def _last_name(self, value):
        self.__last_name = value

    @property
    def _student_id(self):
        return self.__student_id

    @_student_id.setter
    def _student_id(self, value):
        self.__student_id = value

    @property
    def _grade_level(self):
        return self.__grade_level

    @_grade_level.setter
    def _grade_level(self, value):
        self.__grade_level = value

    def student_info(self):
        print(f"{self.__first_name}, {self.__last_name}, Student ID: {
              self.__student_id}, {self.__grade_level}")

        # Method to print student details
    def print_student_details(self):
        print("Student Details:", vars(self))


def main():
    me = Student("Ducktor", "Quacksalot", "009234", "Sophmore")
    me.student_info()
    me.print_student_details()

    me._grade_level("Ducktorate")
    me.student_info()

    student = Student("Jane", "Doe", "12345")

    print(hasattr(student, "_Student__first_name"))  # True
    print(hasattr(student, "middle_name"))  # False


main()
