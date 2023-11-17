x = 5 # global variable
# def func():
#     x = 7 # local variable (functional scope)
#     return x
# print(x)
# print(func())

def func1():
    global x # use global variable
    x = 7
    return x

print(x)
print(func1())
print(x)