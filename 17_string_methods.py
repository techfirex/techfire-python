name = "TuSHaR MakWANa"

# len() function //it also count white speaces
print(len(name))

# lower() method
print(name.lower())

# upper() method
print(name.upper())

# title() method
print(name.title())

# count() method //it counprint(name.lower())t small a
print(name.count("a"))

# strip() method //solve problem related to white speaces
name = "    Tushar     "
dots = "----------------"
print(name+dots)
print(name.lstrip()+dots) # left strip method
print(name.rstrip()+dots) # right strip method
print(name.strip()+dots) # strip method

name = "tush    ar"
print(name.replace(" ", "")) # this remove all spaces by replacing

# replace() method
string = "she is beautiful and she is good singer."
print(string.replace(" ", "_"))
print(string.replace("is", "was"))
print(string.replace("is", "was", 1)) 

# find() method // find(sub, start, end)
print(string.find("is"))
print(string.find("is", 5))

is_pos1 = string.find("is")
is_pos2 = string.find("is", is_pos1+1)

# center() method
name = "TechFire"
print(name.center(12, "*")) # TechFire = 8 + 4 = 12 (left side 2 and right side 2)
print(name.center(10, "*"))

name = input("Enter your name: ")
print(name.center(len(name) + 8, "*"))