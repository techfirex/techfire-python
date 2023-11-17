# sort method - list
fruits = ["grapes", "mango", "apple"]
fruits.sort()
print(fruits) # alphabetically sort and change list

# sorted function - tuple - immutable - cannot change - assign new list auto
fruits2 = ("grapes", "mango", "apple")
print(sorted(fruits2)) # new - return list
print(fruits2) # original

# sorted function - set
fruits3 = {"grapes", "mango", "apple"}
print(sorted(fruits3)) # new - return list
print(fruits3)


# advance sorted
guitars = [
    {"model":"yamaha f310", "price":8400},
    {"model":"faith neptune", "price":50000},
    {"model":"faith apollo venus", "price":35000},
    {"model":"taylor 814ce", "price":450000}
]

print(sorted(guitars, key = lambda d : d["price"])) # low to high
print(sorted(guitars, key = lambda d : d["price"], reverse = True)) # high to low