class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"Name: {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"Dance: {self.dance}")

class DancerEmployee(Dancer , Employee): # dancer comes first in MRO
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

o = DancerEmployee("Bon","Disco") 
o.show() # As we have providied Dancer as the first argument to DancerEmployee the show of that class will be called
print(DancerEmployee.mro())