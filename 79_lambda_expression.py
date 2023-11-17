# lambda expression (anonymous function)

def add(a,b):
    return a+b

print(add(2,3))


add2 = lambda a,b : a+b # here add2 is not name of the function
print(add2(3,4))


def multiply(a,b):
    return a*b

print(multiply(2,3))


multiply2 = lambda a,b : a*b # here multiply2 is not name of the function
print(multiply2(2,3))


# we not call but lets see memory location and name of functions
print(add)
print(add2) # no named
print(multiply)
print(multiply2) # no named

# we use lambda function or expression directly with other buit in functions like map, reduce, filter etc
