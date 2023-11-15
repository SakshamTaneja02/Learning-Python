class Employee:
    def __init__(self, name, id, occ, food):
        self.name = name # public variable, by default all variables in python are public
        self.id = id #public variable
        self.__occ = occ # private variable, any variable with __ at the start is a private variable
        self._food = food # protected variable
    def __fun(self): #private function
        print(self.name)

a = Employee("Luffy",1,"Pirate","Meat")
print(a.name)
# print(a.__occ) # gives error as cannot be accessed directly
print(a._Employee__occ) # method to indirectly access private variable, this is called name mangling
# print(a.food) # gives error
print(a._food) #method to indirectly access the protected variable


# __(double underscore) and _(single underscore) are just naming convention that just leads to name mangling, it does not 
# specify private or protected 
