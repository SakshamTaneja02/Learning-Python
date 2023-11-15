# tuples are immutable, to change them we have to first make them into a list
countries = ("Spain", "Argentina", "India", "Brazil")
temp = list(countries)
temp.append("Chile")
temp.pop(3)
temp[0]="Uruguay"
countries = tuple(temp)
print(countries)

countries2 = ("Spain", "Germany", "France")
football = countries + countries2
print(football)

#count
tup = (1,2,3,3,2,2,3,3,3,2)
print(tup.count(3))

print(tup.index(2,4,7))