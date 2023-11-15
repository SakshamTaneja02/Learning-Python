double = lambda x : x*2
print(double(5))

avg = lambda x,y: (x+y)/2
print(avg(10,5))

def apply(fx, value):
    return 6+fx(value)
# print(apply(double,2))
print(apply(lambda x : x * 2, 2))
# lambda func are useful when we have to pass a function as argument