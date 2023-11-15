class Person:
    # name = "Shanks"
    # bounty = 1000000000000
    def __init__(self, name, bounty):
        print("Hey i am a person")
        self.name = name
        self.bounty = bounty
    def info(self):
        print(f"{self.name} bounty is {self.bounty}")

a = Person("Luffy", 1000000000)
a.info()