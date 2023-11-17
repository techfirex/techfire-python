# kwargs - keyword arguments
# **kwargs (double star operator)

# kwargs as parameter

# def func(**kwargs):
#     print(kwargs) # in the dict form
#     print(type(kwargs))

# func(fname = "tushar", lname = "makwana")


def func(**kwargs):
    print(kwargs) 
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}:{v}")

func(fname = "tushar", lname = "makwana")



# kwargs as a normal parameter
# def func(name,**kwargs): 
#     print(kwargs) 
#     print(type(kwargs))
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")

# func(name="hello", fname = "tushar", lname = "makwana") # we have to pass first normal parameter
# func("hello", fname = "tushar", lname = "makwana")


# dictionary unpacking
def func(**kwargs): 
    for k,v in kwargs.items():
        print(f"{k}:{v}")

d = {"name" : "tushar", "age" : 24}
func(**d) # unpacking dictionary