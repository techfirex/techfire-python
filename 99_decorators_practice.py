from functools import wraps

def print_function_data(any_function):
    @wraps(any_function)
    def wrapper(*args, **kwargs):
        print(f"you are calling {any_function.__name__} function")
        print(f"{any_function.__doc__}")
        return any_function(*args, **kwargs)
    return wrapper

@print_function_data
def add(a,b):
    """This function take two numbers as argument and return their sum"""
    return a+b

print(add(2,3))