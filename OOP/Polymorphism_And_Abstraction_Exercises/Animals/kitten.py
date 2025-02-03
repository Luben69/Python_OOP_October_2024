from Animals.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender='Female')

    @staticmethod
    def make_sound():
        return "Meow"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age}" \
               f" year old {self.gender} {self.__class__.__name__}"