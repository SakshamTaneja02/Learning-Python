a = 4
b = "4"
print(a == b) # compares value
print(a is b) #compares exact location of object in memory

c = [1,2,43]
d = [1,2,43]
print(c is d)
print(c==d)

e = 3
f = 3
print(e is f) # gives true as they are immutable and are formed in same memory space, same for tuple
print(e == f)

g = (1,2,3)
h = (1,2,3)
print(g is h)
print(g==h)

i = None
print(i is None)