#sort
l1 = [3,5,6,7,2,3,4,2,-1]
l1.sort() # for increasing order
l1.sort(reverse=True) # for decreasing order
print(l1)

#append
l1.append(10)
print(l1)

#reverse
l1.reverse()
print(l1)

#index
print(l1.index(3))
# print(l1.index(20)) gives error

#count
print(l1.count(3))

# m = l1
# m[0] = 0
# print(l1)
# value of l1 also changes when we change the value of m[0] as m is just a reference to l1, so we do not use this method

#copy
m = l1.copy()
m[0] = 0
print(m)
print(l1)

#insert
l1.insert(5,12) # inserts at 5th index ie l1[5]
print(l1)

#extend
n = [900,100,1000]
l1.extend(n)
print(l1)

#concat
k = l1+m+n
print(k)