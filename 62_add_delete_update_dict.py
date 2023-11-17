user_info = {
    "name": "Tushar",
    "age": 21,
    "fav_movies": ["movies1", "movies2"],
    "fav_tunes": ["Music1", "Music2"],
}

# add data
user_info["fav_tunes"] = ["tune1", "tune2", "tune3"]
print(user_info)

# pop method ---> removes perticular given arguement from dict and also returns
popped = user_info.pop("fav_tunes")
print(user_info)
print(popped)
print(type(popped))

# popitem method ---> randomly deletes data from dict and returns // key value pair tuple // no needs of passing argument
popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))

# update method
user_info = {
    "name": "Tushar",
    "age": 21,
    "fav_movies": ["movies1", "movies2"],
    "fav_tunes": ["Music1", "Music2"],
}

more_info = {
    "state" : "Gujarat",
    "hobbies" : ["coding", "reading"],
}

user_info.update(more_info)
print(user_info)

user_info.update({}) # adding empty dict will not affect the original dict // no data update

# if both data has same keys then, keys values will update and overwrite the new value to that key
# for example both has name keys
user_info = {
    "name": "Tushar",
    "age": 21,
    "fav_movies": ["movies1", "movies2"],
    "fav_tunes": ["Music1", "Music2"],
}

more_info = {
    "name" : "Tushar Makwana",
    "state" : "Gujarat",
    "hobbies" : ["coding", "reading"],
}

user_info.update(more_info) # now name key has value of more_info data
print(user_info)