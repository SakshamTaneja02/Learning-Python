class Employee:
    company_name = "StrawHats" # this is a class variable
    crew_members = 0
    def __init__(self, name):
        self.name = name
        self.raise_variable = 0.02 # this is an instance variable
        Employee.crew_members = Employee.crew_members + 1
    def show(self):
        print(f"{self.name} raise amount is {self.raise_variable} and he is a part of {self.company_name} and his crew has {self.crew_members} members")

emp1 = Employee("Luffy")
emp1.raise_variable = 0.03
emp1.company_name = "StrawHatsPirates" # the variable will only be changed for emp1 not for emp2 as it becomes an instance variable
print(emp1.show())
emp2 = Employee("Zoro")
print(emp2.show())
print(Employee.company_name)
Employee.company_name = "StrawhatsP" # this will change it for everybody but not for emp1 as company_name is an instance variable for it
print(emp2.show())
print(emp1.show())
emp3 = Employee("Nami")
print(emp3.show())