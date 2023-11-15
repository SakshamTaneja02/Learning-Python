import time

# def whileLoop():
#     i = 0
#     while(i<100):
#         i = i + 1

# def forLoop():
#     for i in range(0,100):
#         i = i + 1

# t = time.time()
# whileLoop()
# print(time.time()-t)
# t2 = time.time()
# forLoop()
# print(time.time()-t2)

# print("Hello")
# time.sleep(3)
# print("This is printed after three seconds")

t = time.localtime()
temp = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(temp)
