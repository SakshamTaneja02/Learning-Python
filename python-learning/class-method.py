class Employee:
    company = "Apple"
    def show(self):
        print(self.name, self.company)
    @classmethod
    def changeCompany(cls, new_comp): # cls stands for class
        cls.company = new_comp

e1 = Employee()
e1.name = "Luffty"
e1.show()
e1.changeCompany("Tesla") 
e1.show()
print(Employee.company)