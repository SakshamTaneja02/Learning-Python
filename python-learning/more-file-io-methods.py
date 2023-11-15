# f = open('/Users/sakshamtaneja/Desktop/python-learning/file.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

f = open('/Users/sakshamtaneja/Desktop/python-learning/file3.txt', 'r')
while True:
    line = f.readline()
    temp = line.split(",")
    print(temp)
    if not line:
        break
    print(line)
f.close()

f = open('/Users/sakshamtaneja/Desktop/python-learning/file3.txt', 'w')
lines = ['12,13,14', '100,100,100', '344,243,982']
for line in lines:
    f.write(line + '\n')
f.writelines(lines)
f.close()