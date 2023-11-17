# zip function - return object of tuple - zipped list/items together
# same like map and filter function but little bit different

user_id = ["user1", "user2", "user3"]
names = ["tushar", "milind", "chaitanya"]

print(zip(user_id, names))
print(list(zip(user_id, names))) # convert to list
print(dict(zip(user_id, names))) # convert to dict possible in two values tuples 
# [('user1', 'tushar'), ('user2', 'milind'), ('user3', 'chaitanya')] like this


# example
example = [("a", 1), ("b", 2)]
print(dict(example))
# if there is three list zipped then dictionary making is not possible

# for example
user_id = ["user1", "user2", "user3"]
first_names = ["tushar", "milind", "chaitanya"]
last_names = ["mak", "makw", "makwana"]

print(zip(user_id, first_names, last_names))
print(list(zip(user_id, first_names, last_names))) # list possible
# print(dict(zip(user_id, first_names, last_names))) # dict not possible due to three values


# reverse process

# * operater with zip function
l1 = [1,3,5,7]
l2 = [2,4,6,8]

l = [(1,2), (3,4), (5,6), (7,8)] # from l to make l1 and l2

print(list(zip(*l)))
l1, l2 = zip(*l) # seperating tuples
print(l1)
print(l2)

print(list(l1))


# after zipping find which is max from both values like 1,2 > 2 or 3,4 > 4 # obvious it will give l2
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)

