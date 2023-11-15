a = input("Enter your Number: ")
print(f"The multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except Exception as e:
    print("Sorry some error occured")
    print(e)

print("some imp line of code")
print("end of program")

try:
    a = int(input("Enter your number"))
    num = [6,3]
    print(num[a])
except ValueError:
    print("number is not an integer")
except IndexError: # we can use multiple except
    print("Index error")