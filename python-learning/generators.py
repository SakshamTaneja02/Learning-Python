# generator function allows us to generate value during the code instead of storing them thus helping us same memory and time
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))