import math # if we do this then we have to use math.function_name()
from math import sqrt, pi # we can directly use the function name to use it 
# from math import * # is is used to import all the functions of maths, not a recommended approach
from math import floor as f # to import it using a short form 

result = math.sqrt(9)
print(result)

r = sqrt(pi)
print(f(r))

print(dir(math)) # to print all the functions in a module

# creating out own module and importing and using it
from importing_function import welcome, luffy
welcome()
print(luffy)