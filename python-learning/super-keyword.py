class Parent:
    def parent_method(self):
        print("This is the parent method")

class Child(Parent):
    def child_method(self):
        print("This is the child method")
        super().parent_method() # super is used to call the parent method from the child method

obj = Child()
obj.child_method()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
obj = Programmer("Luffy",1,"Python")
print(obj.name)
