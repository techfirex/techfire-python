name = "Tushar"

# this will work in all lang
for i in range(len(name)):
    print(name[i])

print("----------------")

# for python easy syntax
# string is iterable
for i in name:
    print(i)
    
print("----------------")

num = input("Enter number to sum: ")
sum = 0
for i in num:
    sum += int(i)
print(sum)