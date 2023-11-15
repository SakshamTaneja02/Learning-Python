x = 4 # global variable

def hello():
    x = 10 # local variable, it gets destroyed as soon as the function ends
    print(f"The local x is {x}")

def hello2():
    global x # now x is a global variable
    x = 5
    print(f"The local x is {x}")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")
hello2()
print(f"The global x is {x}")