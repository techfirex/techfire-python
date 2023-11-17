# def func(a,b):
#     return a+b

# print(func(5,6)) # it will give answer 11
# print(func('5','6')) # it will give answer 56

# def func2(a,b):
#     if type(a) == int and type(b) == int:
#         return a+b
#     return "OOPs you are passing data type to function"
# print(func2('5','6'))

# now raise error
def func2(a,b):
    if type(a) == int and type(b) == int:
        return a+b
    raise TypeError ("OOPs you are passing data type to function")
print(func2('5','6'))