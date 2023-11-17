# list comprehension with if statement

# numbers = list(range(1,11))
# print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_nums = []
# for i in numbers:
#     if i%2 == 0:
#         even_nums.append(i)
# print(even_nums)

# even_nums_lc = [i for i in numbers if i%2 == 0]
# print(even_nums_lc)

even_nums_lc1 = [i for i in range(1,11) if i%2 == 0]
print(even_nums_lc1)

odd_nums_lc = [i for i in range(1,11) if i%2 != 0]
print(odd_nums_lc)