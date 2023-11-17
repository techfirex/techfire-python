# define function
# input
# num, iterable (tuple or list) containing number as args

# example
# nums = [1,2,3]
# to_power(3,*nums)

# output
# list >> [1,8,27]

# if user did not pass any args then give user a msg "hey you didn't pass args"

# else
# return list

# use list comprehension


def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "hey you didn't pass args"

nums = [1,2,3]
print(to_power(3,*nums))
# print(to_power(4,*[2,3,4])) # we can also pass like this
