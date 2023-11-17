# functions with all parameters

# PADK

# normal parameter
# *args
# default parameter
# **kwargs

def func(name, *args, last_name = "makwana", **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

# func("tushar", 1,2,3, a=1,b=1) #third default parameter is not given here
# func("tushar", 1,2,3, last_name="unknown", a=1,b=1)