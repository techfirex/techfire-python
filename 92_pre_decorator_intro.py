# you have to complete understanding of functions
# fist class function / closures
# then finally we will learn about decorators

def square(a):
    return a**2

print(square(5))

s = square
print(s(2))


print(s.__name__)
print(square.__name__)

print(square)
print(s)
