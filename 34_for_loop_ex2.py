name = input("Enter name: ")

temp_char = ""

# this method for python
# for i in name:
#     if i not in temp_char:
#         temp_char += i
#         print(f"{i} : {name.count(i)}")
        
# this method work in any lang
for i in range(0, len(name)):
    if name[i] not in temp_char:
        temp_char += name[i]
        print(f"{name[i]} : {name.count(name[i])}")   