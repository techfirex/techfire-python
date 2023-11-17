fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'kiwi']

# count method - count the items in the list
print(fruits.count('apple'))

# sort method - alphabetically sort the list and change 
# numbers = [1,2,10,7,13,3,19,4]
# numbers.sort()
# print(numbers)

# print(numbers.sort()) - this will give None

# sorted function - work as sort but not change list 
numbers = [1,2,10,7,13,3,19,4]
print(sorted(numbers))

# clear method - clear the list
fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'kiwi']
fruits.clear()
print(fruits)

# copy method - copy list to another list
fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'kiwi']
new_fruits = fruits.copy()
print(new_fruits)