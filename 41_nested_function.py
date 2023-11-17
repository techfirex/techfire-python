# function inside function
# 'kiss' rule - keep it simple, stupid

def greater(a, b):
    if a>b:
        return a 
    return b 

# def greatest(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     return c
# print(greatest(5,6,7))
# print(greatest(67,100,45))

# from above using function one (greater) inside another function and making funtion work like greatest function
# def new_greatest(a,b,c):
#     bigger = greater(a,b)
#     return greater(bigger, c) 

# or making code short
def new_greatest(a,b,c):
    return greater(greater(a,b), c)
print(new_greatest(67,100,45))
print(new_greatest(67,100,450))