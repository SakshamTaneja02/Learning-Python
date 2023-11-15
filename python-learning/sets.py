s = {2,4,2,6,"H","S","H",True}
print(s)

# sets are unordered collection of data items, unchangeable and do not contain duplicate items

s1 = {}
print(type(s1))
# this gives dictionary instead of set, to correct this we do
s2 = set()
print(type(s2))

for value in s:
    print(value)