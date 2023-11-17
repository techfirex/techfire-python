import os

# os.getcwd() # get current working directory
print(os.getcwd())

# os.mkdir("movies") # make directory if dir already exists then give error

# print(os.path.exists("movies"))

# if os.path.exists("movies"):
#     print("already exists")
# else:
#     os.mkdir("movies")

# create file - best way to create file it will not give error if file already there
# open("new_file.txt", "a").close()

#  os.mkdir(r"F:\movies") # give full path

# os.chdir(r"F:\movies") # change directory

# print(os.listdir())
# print(os.listdir(r"F:\movies")) # full path to work in other dir
 
# for items in os.listdir():
#     print(items)

# for items in os.listdir(): 
#     full_path = os.path.join(os.getcwd(), items)
#     print(full_path)

for items in os.listdir(r"/home/tushar"): # is you need pass other path in listdir() to work in other dir
    full_path = os.path.join(os.getcwd(), items)
    print(full_path)