a = True
# print(a=False) # gives an error
print(a:=False) #:= is the walrus operator that lets us change the value of variable within an expression

numbers = [1,2,3,4,5]
while (n:=len(numbers))>0:
    print(numbers.pop())

foods = list()
# while True:
#     food = input("Enter your fav food: ")
#     if(food=="quit"):
#         break
#     foods.append(food)
# print(foods)
# another way to write this is

while (food:=input("Enter your fav food: ")) != "quit":
    foods.append(food)
print(foods)