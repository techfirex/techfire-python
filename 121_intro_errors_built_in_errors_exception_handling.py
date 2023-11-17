# some built in errors
# Exception handling
# raise own errors, debugging, etc


# SyntaxError
# def func() # forget : sign after function
#     print("Hello world")
# func()

# IndentationError
# def func():
# print("hello world") # not given indenation
# func()

# NameError
# print(name) # name is not defined in above code

# TypeError 
# print(5 + "tushar") # wrong concatination

# IndexError
# l = [1,2,3,4] # there is only three index not 4 so cant access
# print(l[4])

# ValueError
# s = "a" # passed wrong value in string
# print(int(s)) # so does not conver to int

# AttributeError
# l = [1,2,3] 
# l.push(1) # there is no method like push in list

# KeyError
d = {"name":"Tushar"}
print(d["age"]) # age is not key in given dict