# any - if any one is true then true
# all - if all values true then true otherwise false

numbers1 = [2,4,6,8,10]
numbers2 = [1,2,3,4,5,6,7]

even1 = []
for num in numbers1:
    even1.append(num%2==0)

print(even1)
# [True, True, True, True, True]

print(all([True, True, True, True, True]))
# True
print(all([True, True, False, True, True]))
# False

print(all([num%2==0 for num in numbers1])) # True
print(all([num%2==0 for num in numbers2])) # False

print(any([num%2==0 for num in numbers2])) # True



