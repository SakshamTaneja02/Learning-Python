name="Saksham"
friend='Saksham'
print("Hello", name)
# a = "He said "Hello" " this gives an error
a = "He said \"Hello\" "
print(a)
b = 'He said "Hello" '
print(b)
# both a and b are write ways of writing the above statements
 
# for a multiline string 
c = '''Hello
My name is Saksham'''
print(c)
d = """Hello
My name is Saksham"""
print(d)

#accessing charecters in a string
print(name[0])
print(name[1])

#for loop in string
for char in name:
    print(char)
for char in c:
    print(char)