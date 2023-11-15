#string are immutable

#upper and lower
a = "Saksham"
print(a.upper())
print(a.lower())

#strip: it removes any white space before and after the string
b = "   Hello   "
print(b)
print(b.strip())

#rstrip: removes any trailing charecters
c = "Yoo !!!"
print(c.rstrip("!"))

#replace: replace all occurences of a string with another string
d = "Spoon Spill Spit"
print(d.replace("Sp","M"))

#split: it splits given string at the specified instance and returns the seperated string as list items
e = "Messi is the GOAT"
print(e.split(" "))

#capitalize: makes first charecter capital and rest are turned to lowercase
f = "bye Bye SakshaM"
print(f.capitalize())

#center: aligns the string to center as per parameters given
g = "Welcome to the Console"
print(g.center(50))
print(g.center(50,"."))

#count: count the number of occurences the given has
h = "abracadarbra"
print(h.count("a"))

#ends with: check if given string ends with a given value
i = "Welcome to the Console !!!"
print(i.endswith("!!!"))
print(i.endswith("to",4,10))

#find: find the first occurence of given value and return the index
j = "His name is Don. He is a bad boy."
print(j.find("is"))
print(j.find("ish"))

#index: same as find but gives an error if string is not found instead of -1
# print(j.index("ish"))

#isalnum: returns true if string does not contain any punctuations or characters
k = "WelcometotheConsoleNo1"
print(g.isalnum())
print(k.isalnum())

#isalpha: returns true is string contains only alphabets
l = "Welcome"
print(l.isalpha())
print(k.isalpha())

#islower: returns true if all characters are in lowercase
m = "yoo"
print(m.islower())
print(l.islower())

#isprintable: return true if all characters are printable
n = "Welcome\n"
o = "Welcome"
print(n.isprintable())
print(o.isprintable())

#isspace: returns true if and only is string contains whitespace 
p = "     "
print(p.isspace())
print(j.isspace())

#istitle: return true if first word of each word is capital
q = "World Health Org"
print(q.istitle())

#isupper: returns true if all characters are in uppercase
r = "SAKSHAM"
print(r.isupper())

#startswith: check if given string starts with a given value
s = "Python is good"
print(s.startswith("Python"))

#swapcase: converts lowercase to uppercase and uppercase to lowercase
t = "Hello Bye"
print(t.swapcase())

#title: capitalize each letter os the word within the string
u = "He's is a good boy"
print(u.title())