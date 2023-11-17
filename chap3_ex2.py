name = input("Enter you name: ")
age = int(input("Enter you age: "))

# x = name[0].lower()
# print(x)

# if name[0].lower()=='a' and age>=10:
#     print("You can watch coco")
# else:
#     print("sorry, you cannot watch")
    
if age>=10 and (name[0]=="a" or name[0]=="A"):
    print("You can watch coco")
else:
    print("sorry, you cannot watch")