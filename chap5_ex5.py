# common finder
# input [1,2,5,8] [1,2,7,6]
# output [1,2]



l = [1,2,5,8]
k = [1,2,7,6,8]
x = []
        
# def common_find(l,k):
#     for i in l:
#         for j in k:
#             if i == j:
#                 x.append(i)
#     return x

# print(common_find(l,k))

# second solution
def common_find(l,k):
    output = []
    for i in l:
        if i in k:
            output.append(i)
    return output
print(common_find(l,k))
    
    