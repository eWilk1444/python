
class Dog:
    # super classs for herding dog
    def __init__(self, color, coat, size):
        self.color = color
        self.coat = coat
        self.size = size

    def __str__(self):
        return f"Dog(Color: {self.color}, Coat: {self.coat}, Size: {self.size})"

    # include getters and setters

    def bark(self):
        print("Woof!")

    def happy(self):
        print("Wag wag")


class HerdingDog(Dog):
    def herding(self):
        print("Go over here!")

    def __init__(self, color, coat, size, name, favorite_toy):
        super().__init__(color, coat, size)
        self.__name = name
        self.__favorite_toy = favorite_toy

    def __str__(self):
        return f"{super().__str__()} {self.__name}, {self.__favorite_toy}, with herding skills"


def main():

    bouvier = Dog("fawn", "long rough", "large")
    bouvier.bark()
    bouvier.happy()

    shepherd = HerdingDog("black", "short", "large",
                          "Rin tin tin", "Minty World Ball")
    print(shepherd)


main()
