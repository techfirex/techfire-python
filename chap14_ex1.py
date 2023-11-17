from functools import wraps
import time

def calc_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"executing {function.__name__}")
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        print(f"This function took {t2-t1} seconds.")
        return returned_value
    return wrapper


@calc_time
def cube_finder(n):
    return [i**3 for i in range(1,n+1)]

cube_finder(1000)
# print(cube_finder(10))
