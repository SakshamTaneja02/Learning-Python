def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

print(factorial(7))

def fibo(n):
    if(n==0 or n==1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(10))