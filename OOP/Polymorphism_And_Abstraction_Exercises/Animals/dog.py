from Animals.animal import Animal


class Dog(Animal):
    @staticmethod
    def make_sound():
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age}" \
               f" year old {self.gender} {self.__class__.__name__}"