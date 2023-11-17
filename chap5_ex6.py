# create function
# [1, 2, 3, [1, 2], [1, 2]] input
# 2 - count inner list number

numbers = [1, 2, 3, [1, 2], [1, 2],  [1, 2, 3]]
# print(numbers)
# j = 0
# for i in numbers:
     # print(i)
    
#     if type(i) == list:
         # print(i)
         # print(j)
#         j += 1
#     else:
#         pass
# print(j)

def list_count(l):
    j = 0
    for i in l:
        if type(i) == list:
            j += 1
    print(j)
    
list_count(numbers)