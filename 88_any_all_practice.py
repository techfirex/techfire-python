# def my_sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(my_sum(1,2,3,8.9))
# print(my_sum(1,2,3,8.9,"tushar")) # wrong input


# check input is right or wrong using all function
def my_sum(*args):
    if all([type(arg) == int or type(arg) == float for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "wrong input"

# print(my_sum(1,2,3,8.9))
print(my_sum(1,2,3,8.9,"tushar"))