# function return two values - its return vales in tuple
def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply

print(func(2,3))
x = func(2,3) 
print(type(x)) # it is tuple

# but you can unpack tuple, for example
add, multiply = func(2,3) # now two values store into two variables
print(add)
print(multiply)