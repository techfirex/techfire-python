numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = list(range(1,11))

def square_list_items(list_items):
    squared_list = []
    for items in list_items:
        squared_list.append(items**2)
    return squared_list

print(square_list_items(numbers)) 