# tuples
# store any type of data
# immutable - cannot change/update after created

# methods not applied like, (list is mutable so all update method apply)
# no append, no pop, no insert, no remove

example = ('one', 'two', 'three')
print(example)

# tuples are used for data which is not changed over time
# for example
days = ("Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday",)
# tuples are faster than list

# methods which are used in tuples
# count, index
# len()
# slicing same as list
print(days[:2])

# we cannot assign/update new value to tuple, for example
example[0] = 'zero'
print(example)
# this gives an error