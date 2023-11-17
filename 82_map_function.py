# map function

numbers = [1,2,3,4]

def square(a):
    return a**2

square_list = list(map(square, numbers))
print(square_list)
# map function will take one function and list to work as above

# we can also use lambda expression instead of making square function
square_list_lambda = list(map(lambda a : a**2, numbers))
print(square_list_lambda)

# using list comprehension
square_list_lc = [i**2 for i in numbers]
print(square_list_lc)

# using normal method
empty_list = []
for num in numbers:
    empty_list.append(num**2)
    # or # empty_list.append(square(num)) 
print(empty_list)


# map function with built in functions
strings = ["abc", "abcd", "abcde"]
# map(len, strings) # finding length # it will give map object which can iterate only once, you can convert to list for iterate more times (for looping more than one time)

print(map(len, strings))
length = map(len, strings)
print(length)

for i in length:
    print(i)

for j in length: # this will not work because map object iterate only once
    print(j)

length_list = list(map(len, strings)) # after convert to list we can iterate more than once
print(length_list)