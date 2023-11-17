# decorators - enhance the functonality of function
# @ - use for decorator - synthetic sugar

# create decorator function
def decorator_function(any_function):
    def wrapper_function():
        print("this is awsome function")
        any_function()
    return wrapper_function

def func1():
    print("this is function 1")
# func1()


def func2():
    print("this is function 2")
# func2()

# var = decorator_function(func1) # we can give any name to var like func1
# var()

# also we can use @ as short cut to remove above stuff and call decorator func1
@decorator_function # short cut
def func3():
    print("this is function 3")

func3()