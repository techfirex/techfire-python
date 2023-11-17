numbers = [1,2,3,4] # iterables
squares = map(lambda a : a**2, numbers) # iterator

print(numbers)
print(squares)

# for loop
for i in numbers:
    print(i)

# for j in squares:
#     print(j)

# how for loop works 
# for iterables it convert to iterator using iter function
numbers_iter = iter(numbers)
# after that next function will call until list is end
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
# print(next(numbers_iter)) # raise error for stop iteration


# we can direct run next function on iterator
print(next(squares))
print(next(squares))

