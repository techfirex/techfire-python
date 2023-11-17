# function returning function / closures / first class function

def outer_func():
    def inner_func():
        print("inside inner function")
    return inner_func # here we can also call inner_func() so we dont need to store in var

var = outer_func()
var()


def outer_func2(msg):
    def inner_func2():
        print(f"msg is {msg}")
    return inner_func2

var2 = outer_func2("im msg")
var2()