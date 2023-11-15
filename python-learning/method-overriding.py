class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self): # method overriding
        return 3.14*self.r*self.r 

c = Circle(5)
print(c.area())