# append method - adding data at the end
# fruits = ["grapes", "apples"]
# print(fruits)
# fruits.append("mangoes")
# print(fruits)

# majoriry time we use method using blank list
# fruits = []
# fruits.append("banana")
# fruits.append("raspbery")
# print(fruits)

# insert method - adding data at particular position
# fruits = ["grapes", "apples"]
# fruits.insert(2, "orange")
# print(fruits)

# concatenate/list joining
# fruits1 = ["grapes", "apples"]
# fruits2 = ["banana", "orange"]
# fruits = fruits1 + fruits2
# print(fruits)

# extend method - join list to another list at the end or extend list by other list
# fruits1.extend(fruits2)
# print(fruits1)

# difference between append and extend
# fruits1.append(fruits2)
# print(fruits1)


# pop method - it will delete the data from end
# if we pass index as arguement then it will delete that indexed data

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
# fruits.pop()
# fruits.pop(2) # removing second position item
# print(fruits)
# removed = fruits.pop() # we get store removed item uisng pop
# print(removed)

# del - operater or statement for removing
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
# del fruits[2]
# print(fruits)

# remove method - remove items using item name rather than index
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
# fruits.remove('apple')
# print(fruits)

# what if there is two same item
fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'kiwi']
fruits.remove('apple') # it will remove first indexed apple
print(fruits)

# methods
# append, extend, insert
# pop, remove, del
