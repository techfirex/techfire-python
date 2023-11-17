# list comprehension in in nested list
example = [[1,2,3],[1,2,3],[1,2,3]]

nested_list_comprehension = [[i for i in range(1,4)] for j in range(3)]
print(nested_list_comprehension)


nest_list = []
for j in range(3):
    nest_list.append([1,2,3])
print(nest_list)