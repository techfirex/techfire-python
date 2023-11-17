# generate list using range function
# numbers = list(range(1,11))
# print(numbers)

# somthing more about pop method
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# popped_item = numbers.pop()
# print(popped_item)

# index method - finding index of item
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 7, 8, 11, 2, 1, 4, 6, 9, 1]
# print(numbers.index(1)) # finding position of 1 from list // defalt search start from 0 index
# .index(search, start, end)
# print(numbers.index(1,3)) # start from 3 index so it comes at 10
# print(numbers.index(1,11)) # after 10 it comes at 15
# print(numbers.index(1,11,14)) # between 11 & 14 index there is no 1 item so gives error

# pass list to function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def negative_number(l): # as input take list
    negative = []
    for i in l:
        negative.append(-i) # append negative number to list 
    return negative

print(negative_number(numbers))
        