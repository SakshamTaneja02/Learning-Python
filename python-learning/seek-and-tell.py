with open('/Users/sakshamtaneja/Desktop/python-learning/file3.txt', 'r') as f:
    print(type(f)) 
    f.seek(10) # move to 10th byte in file
    print(f.tell()) # tells the current position of pointer
    data = f.read(5) # read the next 5 bytes
    print(data)