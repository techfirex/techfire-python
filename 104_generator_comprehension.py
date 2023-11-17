# square = [i**2 for i in range(1,11)]
# print(square)

# generator comprehension is same as list comprehension but instead [] use () this bracket

square = (i**2 for i in range(1,11))
print(square)

for i in square:
    print(i)

for i in square: # it will not get output in 2nd time because it is already generated and give result through first loop
    print(i)