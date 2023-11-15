s1 = {1,2,3,4}
s2 = {2,4,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1)

s3 = {1,2,3,4}
s4 = {2,4,6,7}
print(s3.intersection(s4))

s5 = {1,2,3,4}
s6 = {2,4,6,7}
print(s5.symmetric_difference(s6))

s7 = {1,2,3,4}
s8 = {2,4,6,7}
print(s7.difference(s8))

s9 = {1,2,3,4}
s10 = {2,4,6,7}
s11 = {5,6,7,8}
s12 = {2,4}
print(s9.isdisjoint(s10))
print(s9.isdisjoint(s11))
print(s9.issuperset(s12))
print(s9.issuperset(s10))
print(s12.issubset(s9))
print(s12.issubset(s11))

s9.add(12)
print(s9)
s9.remove(12)
print(s9)

#pop: removes any item from the set
print(s9.pop())
print(s9)

# del: to delete the entire set
del s9
# print(s9) error 

s10.clear()
print(s10)

if 10 in s11:
    print("YES")
else: print("NO")