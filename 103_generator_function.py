# create generator, two method
# 1. using generator function
# 1. using generator comprehension

# generator function

# normal method
# def nums(n):
#     for i in range(1,n+1):
#         print(i)

# nums(10)

# generator
def nums(n):
    for i in range(1,n+1):
        yield(i) # use yield keyword for generator // we can also write yield i only
 
# print(nums(10)) # generator object // we can loop it once because its generator step by step and discard earlier numbers from memory, so use less memory and more performance

# in case of list // it first create and then store in memory as whole and then perform so time increased to perform

for i in nums(10): # above nums() generator function
    print(i)

# numbers = nums(10) # here we already generate the values so second time loop dont work but we use loop directly then it works every time on generator of object - iterator

for i in nums(10): # it cannot run second time because all elements discarded/remove after use and if we want to run again and again then convert it into list but after doing that we can not get benifit of generators // list(nums(10))
    print(i)