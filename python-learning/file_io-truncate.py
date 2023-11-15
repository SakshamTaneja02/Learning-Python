with open('/Users/sakshamtaneja/Desktop/python-learning/file3.txt', 'w') as f:
    f.write("Hello World") 
    f.truncate(5) # only first 5 characters are written to the file

with open('/Users/sakshamtaneja/Desktop/python-learning/file3.txt', 'r') as f:
    print(f.read())