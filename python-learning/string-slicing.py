#string slicing
name = "Saksham,Messi"
print(len(name)) #length of string
print(name[0:5]) # including 0 but not 5
print(name[:4]) # this is equivalent to print(name[0:4])
print(name[1:6])
print(name[0:-3]) # this is equivalent to print(name[0:len(name)-3])
print(name[-1:-3]) # no output
print(name[-3:-1])