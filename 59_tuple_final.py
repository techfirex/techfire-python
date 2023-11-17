# tuple, list, str

num = tuple(range(1,11))
print(num)
# same way list also created

numx = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we can convert list into tuple
list_convert_tuple = tuple(numy)
print(list_convert_tuple)

x = str(numx)
y = str(numy)
print(type(x))
print(type(y))
# see both are string but look like same as list and tuple so be carefull.
# output is like 
# "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)" -- string but having tuple
# "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" -- string but having list