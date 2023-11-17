user = {}

name = input("enter name: ")
age = int(input("enter age: "))
fav_movies = input("enter fav movies comma separated: ").split(",")
fav_songs = input("enter fav songs comma separated: ").split(",")

user["name"] = name
user["age"] = age
user["fav_movies"] = fav_movies
user["fav_songs"] = fav_songs

for keys,values in user.items():
    print(f"{keys} : {values}")