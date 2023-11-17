from functools import wraps

def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data_types = []
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return function(*args, **kwargs)
        else:
            return "Invalid Input"
    return wrapper

@only_int_allow
def add_all(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# print(add_all(1,2,3,[1,3,4]))
print(add_all(1,2,3,4,5))



def only_int_allow_lc(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg)==int for arg in args]):
            return function(*args, **kwargs)
        return "Invalid Input"
    return wrapper

@only_int_allow_lc
def add_all(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add_all(1,2,3,[1,3,4]))
# print(add_all(1,2,3,4,5))