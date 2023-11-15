class Employee:
    def __init__(self, name):
        self.name = name
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self):
        return f"The name of employee is {self.name}"
    def __call__(self):
        print("Yoo")
obj = Employee("Zoro") # calls the __init__ dunder method
print(len(obj)) # calls the __len__ dunder method
print(obj) # calls the __str__ dunder method
obj() # calls the __call__ dunder method