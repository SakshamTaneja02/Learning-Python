x = [1,2,3]
print(dir(x)) # dir gives all the method available for an object in this case a list

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("Luffy",19)
print(p.__dict__) # __dict__ returns a dictionary representation of an object's attributes

# print(help(str)) # help is used to get the documentation for an object
# print(help(Person))