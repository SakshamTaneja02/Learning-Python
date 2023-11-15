class Math:
    def __init__(self, n):
        self.n = n
    def addNum(self, num):
        self.n = self.n + num
    @staticmethod # we dont have to pass self in static methods
    def add(a,b):
        return a+b
    
a = Math(5)
print(a.add(7,2))
print(Math.add(7,2)) # we can call static methods without and with using the object of the class