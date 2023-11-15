class Person:
    name="Saksham"
    occupation="Newbie"
    bounty=0
    def info(self):
        print(f"Hey my name is {self.name}. I am {self.occupation}. My bounty is {self.bounty}")

a = Person()
print(a.name)

a.name = "Luffy"
a.occupation = "King of the Pirates"
a.bounty = 5000000000000
print(a.name, a.occupation, a.bounty)
a.info()