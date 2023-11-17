# def multiply(*args):
#     multiply = 1
#     for i in args:
#         multiply *= i
#     return multiply

# print(multiply(1,2,3,4))



# def multiply(num, *args): # here we passed normal parameter and args
#     multiply = 1
#     for i in args:
#         multiply *= i
#     return multiply

# print(multiply(2,3,4)) # so 2 treat as normal parameter and 3,4 is *args
# output is 3*4 = 12 
# first argument is for num



# def multiply(*args):
#     multiply = 1
#     for i in args:
#         multiply *= i
#     return multiply

# print(multiply()) # if we dont pass any arguements then it will not rais error
# output = () empty tuple and 1 which is already defined



def multiply(nums, *args): # if we write normal parameter
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply(2,3,4)) # then we must have to pass that normal parameter arguement
# 2 is must pass which is first positional arguement other wise it will give errror
# if we dont pass 3,4 which is *arguements then it will not give error

# def multiply(*args, nums): # do not write function like this, *args is always after the normal parameter

