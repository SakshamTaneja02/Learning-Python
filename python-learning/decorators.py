def greet(fx):
    def mfx(*args, **kargs):
        print("Good Morning")
        fx(*args, **kargs)
        print("Thanks for using this function")
    return mfx

# def hello():
#     print("Hello World")
# greet(hello)()
# this code is equivalent to code written below

@greet
def hello():
    print("Hello World")

hello()

@greet
def add(a,b):
    print(a+b)

add(1,2)