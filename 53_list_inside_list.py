# nested lists
# 2d lists and 3d lists

matrix = [[1,2,3], [4,5,6], [7,8,9]] # 2d list
# 3 items --> 3 lists
print(matrix)

for sublist in matrix: # nested loop // loop inside loop
    for items in sublist:
        print(items)

print(matrix[1][1]) # accessing data from 2d lists

# type function - checking  type of data
s = "string"
print(type(s))
print(type(matrix))
