def calculate(a,b):
    temp = (a*b)/(a+b)
    print(temp)

def greater(a,b):
    if(a>b):
        print("First is greater")
    elif(a<b):
        print("Second is greater")
    else:
        print("Both are equal")

def lesser(a,b):
    pass

calculate(10,11)
calculate(10,20)
greater(10,10)
greater(10,21)