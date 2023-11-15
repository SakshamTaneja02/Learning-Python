# 9 and 1 are default arguments
def average(a=9, b=9):
    print((a+b)/2)
average()
average(5,10)
average(a=10)
average(b=9)
average(b=1,a=10) # keyword arguments: here we cann change the order in which we are providing the input to the function

def func2(a,b):
    print(a+b)
# here a and b are required arguments

def func(*numbers):
    # numbers here act as a tuple
    sum =  0
    for num in numbers:
        sum=sum+num
    return sum
func(10,10,23,43,56)
d = func(10,20,30,405,505)
print(d)
