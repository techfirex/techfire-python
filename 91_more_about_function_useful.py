# what are doc strings
# how to write doc strings
# how to see doc strings
# what is help function

def add(a,b):
    """this will take 2 argument and give sum of two """
    # ''' this will take 2 argument and give sum of two '''
    return a + b

print(add(2,3))


print(add.__doc__)

# built in function like len,sum,max,min,sorted
print(len.__doc__)


# help function to see help of func
# print(help(sum))
