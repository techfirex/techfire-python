# list comprehension
# with the help of lc we can create of list in one line

# create a list of squares from 1 to 10
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)
    
squares_lc = [i**2 for i in range(1,11)]
print(squares_lc)

# negative from 1 to 10
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

negative_lc = [-i for i in range(1,11)]
print(negative_lc)


# first character print
names = ["Tushar", "Milind", "Chaitanya"]
# new_list = ["T","M","C"]

new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

new_list_lc = [name[0] for name in names]
print(new_list_lc)