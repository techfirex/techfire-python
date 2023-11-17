# in keyword and iterations (looping)

user_info = {
    "name": "Tushar",
    "age": 21,
    "fav_movies": ["movies1", "movies2"],
    "fav_tunes": ["Music1", "Music2"],
}

# check if key is exist
if "name" in user_info:
    print("present")
else:
    print("not present")

# check if values is exist ---> values method
if "Tushar" in user_info.values():
    print("present")
else:
    print("not present")

if "24" in user_info.values():
    print("present")
else:
    print("not present")

# loops in dictionary
for key in user_info:
    print(key)

for values in user_info.values():
    print(values)

# values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

for i in user_info:
    print(user_info[i])

# keys method
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# items method
user_info_items = user_info.items()
print(user_info_items)
print(type(user_info_items))

for i in user_info.items():
    print(i)

for keys,values in user_info.items():
    print(f"keys is {keys} and values is {values}")