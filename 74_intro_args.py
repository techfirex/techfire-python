# flexible function
# * operator
# * args

# when define the function it is parameter
# when calling the function it is arguement

def sum(a,b):
    return a+b

print(sum(1,2)) # here we can only give two arguments only, if we give more then 2 raise an error

# to imrpove this we use * operator in our code


def total_sum(*args): # instead of args we can write anything, but according to convetion args is written. work done by * , we only give name as *args, we can write also *nums.
    print(args)
    print(type(args)) # it it tuple of input arguments

total_sum(1,2,3,4,5,6,7,8,9)



def total_sum_new(*args):
    total = 0
    for i in args:
        total += i
    return total

print(total_sum_new(1,2,3,4))
