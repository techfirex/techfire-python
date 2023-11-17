# because of limitation of lists
# for real life data dictionary is good

# example of list with real life Data
user = ["Tushar", 21, ["movies1", "movies2"], ["Music1", "Music2"]]
# this list contents username, age, fav movies, fav music but this is not good way to represent data in list

# Dictionary
# Unordered collection of data in key:value pair

user_dict = {"name": "Tushar", "age": 21}
print(user_dict)
print(type(user_dict))

# second method to create dict
user_dict1 = dict(name="Milind", age=24)  # here name is direct not in string
print(user_dict1)
print(type(user_dict1))

# how to access data from dictionary
print(user_dict["name"])
# dict is unordered data collection // no indexing options // so we use key to access data

# which type of data a dictinoary can store
# anything
# numbers, list, string, dictionary
# complex data storing //  complex data modeling

user_info = {
    "name": "Tushar",
    "age": 21,
    "fav_movies": ["movies1", "movies2"],
    "fav_tunes": ["Music1", "Music2"]
}
print(user_info["fav_movies"])

# user_data = {
#     user1 = {

#     },
#     user2 = {

#     },
# }

# how to add data to emplty dictionary
user_info2 = {}
user_info2["name"] = "Hacker"
user_info2["age"] = 22

print(user_info2["name"])
print(user_info2["age"])

