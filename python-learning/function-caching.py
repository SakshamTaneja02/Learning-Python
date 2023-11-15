from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if(n==0 or n==1): return n
    return fib(n-1)+fib(n-2)

print(fib(40))