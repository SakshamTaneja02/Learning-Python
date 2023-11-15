l = [3,5,6]
print(l)
l1 = [3, 5, 6, "Python", True] # we can have different data types in on list
print(l1[0])
print(l1[-3]) # equivalent to len(l1)-3

if 3 in l1:
    print("YES")
else:
    print("NO")
if 7 in l1:
    print("YES")
else:
    print("NO")

# if "arry" in "Harry":
#     print("YES")
# if "ary" in "Harry":
#     print("YES")

print(l1[:])
print(l1[1:])
print(l1[:-1])
print(l1[0:5:2])

#list comprehension: generating new list
lst = [i for i in range(4)]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Ana", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
name2 = [item for item in names if (len(item)>4)]
print(name2)