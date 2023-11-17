# filter function 
# same as map function

numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(a):
    return a%2==0

evens = list(filter(is_even, numbers)) # dont call the function write only name is_even
print(evens)

# also we can use normal method, lambda expression, list comprehension etc lots of ways as we do in map function earlier