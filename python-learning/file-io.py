f = open('/Users/sakshamtaneja/Desktop/python-learning/file.txt', 'r') # r mode: for reading only, if file does not exist it
# gives an error, its the default mode, rb: reads file in binary mode, rt: default mode
text = f.read()
print(text)

f1 = open('/Users/sakshamtaneja/Desktop/python-learning/file2.txt', 'w') # w mode: for writing only,
#if file foes not exist it creates the file
f1.write("Hello my name is Zoro. I am going to be the strongest swordsman in the world.")

f2 = open('/Users/sakshamtaneja/Desktop/python-learning/file.txt', 'a') # a mode: to append text to file, create file if does not exist
f2.write("I am going to be the king of pirates")

f.close() # it is important to close the file
f1.close()
f2.close()

# we can use the with statement as we dont have to close the file after we are done using it
with open('/Users/sakshamtaneja/Desktop/python-learning/file2.txt', 'a') as f:
    f.write("I am lost.")