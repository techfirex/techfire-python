# set data type
# unordered collection (no indexing as dict) of unique items

s = {1,2,3}

# s = {1,1.0,1.1,2.3,"string"} # here 1 and 1.0 treat as same # cannot store list [] and dict {}

print(s)

# remove duplicates from list
l = [1,2,2,2,3,4,4,4,5,5,6,6,6,7,8]
s2 = set(l)
print(s2)

# set methods
# add
s.add(4)
print(s)

# remove
s.remove(3) # remove the value but if not present then give error
print(s)

# discard
s.discard(5) # discard/remove the value it will not give error for example 5 is not present then return same value
print(s)

# copy
s1 = s.copy()
print(s1)

# clear
s1.clear()
print(s1)

