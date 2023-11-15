#tuple are immutable
tup = (1,2,3,"green","red",True)
print(type(tup))
print(tup)

# temp = (1)
# print(type(temp))
# python considers the (1) as of type int to make it a tuple we have to add a comma at the end
temp = (1,) 
print(type(temp))

print(tup[0])
print(tup[-3])

if "green" in tup:
    print("YES")
else:
    print("NO")

print(tup[0:3:2]) # a new tuple is formed before printing, the orginal remains the same
print(tup[1:])
print(tup[:-2])