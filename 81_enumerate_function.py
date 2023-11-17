# we use enumerate function with for loop to track position of our item in iterable

# doing without enumerate function
names = ["tushar", "milind", "chaitanya"]
# pos = 0
# for name in names:
#     print(f"{pos} ---> {name}")
#     pos += 1

# with enumerate function
for position,name in enumerate(names):
    print(f"{position} ---> {name}")


# define a function that take two arguments
# 1. list containing string
# 2. string that we want to find in our list
# this function will return the index of this string in our list and if string is not present that return -1

names = ["tushar", "milind", "chaitanya"]

def find_position(l, target_str):
    for position, string in enumerate(l):
        if string == target_str:
            return position
    return -1

print(find_position(names, "tushar"))
print(find_position(names, "chaitanya"))
print(find_position(names, "unknown"))