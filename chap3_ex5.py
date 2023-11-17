# example - Tushar Makwana
# output - 
# T : 1
# u : 1
# s : 1
# h : 1
# a : 4
# r : 1
#   : 1
# M : 1
# k : 1
# w : 1
# n : 1

name = input("Enter your name: ")

temp_char = ""
i = 0

while i < len(name):
    if name[i] not in temp_char:
        temp_char += name[i] 
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
