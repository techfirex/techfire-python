# advance min() and max()

numbers = [1,2,3,4,5,6,7,8]
print(max(numbers))
print(min(numbers))


# write function for calculate length
def func(item):
    return len(item)

# find max lengh of names
names = ["tushar", "milind", "chaitanya"]
# print(max(names, key = func))
# print(min(names, key = func))

# using lambda expression
# print(max(names, key = lambda item : len(item)))



students = {
    "tushar" : {"score":85, "age":21},
    "milind" : {"score":95, "age":25},
    "chaitanya" : {"score":90, "age":23}
}

print(max(students, key = lambda item : students[item]["score"]))
print(min(students, key = lambda item : students[item]["score"]))


students2 = [
    {"name":"tushar", "score":85, "age":21},
    {"name":"chaitanya", "score":90, "age":23},
    {"name":"milind", "score":95, "age":25},
]


# print(max(students2, key = lambda item : item.get("score")))
# print(max(students2, key = lambda item : item.get("score"))["name"])