# decorators - enhance the functonality of function
# @ - use for decorator - synthetic sugar

# create decorator function
def decorator_function(any_function):
    def wrapper_function():
        print("this is awsome function")
        any_function()
    return wrapper_function


# in above there problem we pass argument to our new func
# example
@decorator_function
def func(a):
    print(f"this is function with argument {a}")

# func(7) # positinal argument error

# to solve use args and kwargs
def decorator_function2(any_function):
    def wrapper_function(*args, **kwargs):
        print("this is awsome function")
        any_function(*args, **kwargs)
    return wrapper_function

@decorator_function2
def func(a):
    print(f"this is function with argument {a}")

func(7)


# there is on more error
@decorator_function2
def add(a,b):
    return a+b

add(2,3) # it will not print 5 sum because we return a+b 
print(add(2,3)) # so when we print this so this return None not give sum 5 



# to solve this we have to return our given function in decorator
def decorator_function_final(any_function):
    def wrapper_function(*args, **kwargs):
        print("this is awsome function")
        return any_function(*args, **kwargs) # return to solve problem of None
    return wrapper_function

@decorator_function_final
def add(a,b):
    return a+b
print(add(2,3)) # after print returning on our function we get 5