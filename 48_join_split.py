# split method
# convert string to list
userinfo = "Tushar 24".split()
print(userinfo)

userinfo = "Tushar,24".split(",") # specify seprater
print(userinfo)

name, age = "Tushar,24".split(",")
print(name)
print(age)

name, age = input("Enter name and age comma separated: ").split(",")
print(name)
print(age)

# join method
# convert list to string
userinfo = ["Tushar", "26"] # 24 is in string
print(",".join(userinfo))