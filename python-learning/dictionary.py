dict = {
    "Harry": "Human Being",
    "Spoon": "Object"
}
print(dict)
print(dict["Harry"])

emp = {
    1: "Saksham",
    2: "Luffy",
    3:"Zoro",
    4:"Sanji"
}
print(emp[2])
# print(emp[5]) gives error 
print(emp.get(5)) #does not give an error, gives None as output

print(emp.keys())
for keys in emp.keys():
    print(keys)

print(emp.values())
for value in emp.values():
    print(value)
for keys in emp.keys():
    print(f"The value corresponding to the key {keys} is {emp[keys]}")

print(emp.items())
for key,value in emp.items():
    print(key, value)