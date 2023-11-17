# looping in tuples
# tuple with one element
# tuple without paranthesis
# tuple unpacking
# list inside tuple
# some funtions that you can use with tuple

mixed = (1,2,3,4,5.0)
print(mixed)

# looping in tuple
for i in mixed:
    print(i)
# while loop also works same as

# tuple with one element
num1 = (1) # this is not tuple // int
num2 = (1,) # this is tuple // for single element you must use , sign
word1 = ('word') # this is string
word2 = ('word',) # this is tuple
print(type(num1))
print(type(num2))
print(type(word1))
print(type(word2))

# tuple without parenthesis
example = "one", "two", "three"
print(type(example))

# tuple unpacking
first, second, third = (example)
print(first)
print(second)
print(third)

# list inside tuple
list_inside_tuple = (1, 2, "one", ["Monday", "Tuesday", "Wednsday"], 5)
# list inside tuple has normal method which we can apply
# list is on 3rd position
list_inside_tuple[3].pop() # last item from list is removed // Wednsday
print(list_inside_tuple)
list_inside_tuple[3].append("Sunday")
print(list_inside_tuple)
# list can modily which is inside tuple

# some funtions for tuples
# min(), max(), sum(), len()
print(min(mixed)) 