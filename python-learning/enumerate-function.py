marks = [1, 2, 3, 4, 5, 6, 7]

index = 0
for mark in marks:
    print(mark)
    if(index==3):
        print("Luffy")
    index = index + 1
# a shorter way of writing this is given below

for index, mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Luffy")

# if we want a different starting index
for index, mark in enumerate(marks,start = 1):
    print(mark)
    if(index==3):
        print("Luffy")