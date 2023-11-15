class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Sound")
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    def make_sound(self):
        print("Bark!")

d = Dog("doggy","Dog", "doggi")
d.make_sound()