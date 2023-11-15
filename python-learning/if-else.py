age = int(input("Enter your age: "))
if(age>=18):
    print("You can drive")
else:
    print("You cannot drive")

if(age<0):
    print("Enter a valid age")
elif(age<18):
    print("You cannot drive the car")
else:
    print("You can drive the car")

num = 10
if(num<0):
    print("Negative Number")
elif(num>0):
    if(num==10):
        print("Number is special")
    else:
        print("Number is not special")
else:
    print("Number is zero")