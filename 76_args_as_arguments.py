def multiply(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

# print(multiply(2,3,4))

# what if we pass the list inside this args
nums = [2,3,4]
# print(multiply(nums)
# output = [2,3,4] is return list because 1*[2,3,4] = [2,3,4]

# to solve this problem we use *args in argument
print(multiply(*nums)) # this * unpack the list (list unpacking) and work done, same work with tuple also
