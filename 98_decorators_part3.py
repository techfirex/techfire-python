# to solve doc string problem
from functools import wraps
    
def decorator_function_final(any_function):
    @wraps(any_function) # we add to solve problem of doc strings
    def wrapper_function(*args, **kwargs):
        """ this is wrapper function """
        print("this is awsome function")
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function_final
def add(a,b):
    """ this is add funtion """
    return a+b
# print(add(2,3))

# its shows doc string and func name of decorators
print(add.__doc__)
print(add.__name__) 

# to solve this we import module functools