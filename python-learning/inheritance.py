class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"{self.name}'s ID is {self.id}")

class Programmer(Employee):
    def showLang(self):
        print("The default lang is Python")

obj = Employee("Luffy", 420)
obj.showDetails()
# obj.showLang() gives error
temp = Programmer("Zoro", 421)
temp.showLang()
temp.showDetails()