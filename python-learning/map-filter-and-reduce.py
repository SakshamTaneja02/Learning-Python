def cube(x):
    return x*x*x
 
l = [1,2,4,5,6]

# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)
# a smaller way to do this is by using map

newl=list(map(cube,l))
print(newl)

def filter_func(a):
    return a>4
newll = list(filter(filter_func,l))
print(newll)

from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)