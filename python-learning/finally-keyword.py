# try:
#     l = [1,2,3,4]
#     i = int(input("Enter index: "))
#     print(l[i])
# except:
#     print("Error")
# finally:
#     print("I am always executed")

def func():
    try:
        l = [1,2,3,4]
        i = int(input("Enter index: "))
        print(l[i])
        return 0
    except:
        print("Error")
        return 1
    finally:
        print("I am always executed")
        #finally is still going to be executed even after return has called

x = func()
print(x)