# create two sets A and B of your choice
A = {"apple", "banana", "cherry"}
B = {1, 5, 7, 9, 3}

print(A)
print(B)
print(type(A))
print(type(B))

# print each set separately using for loop
for i in A:
	print(i)

for i in B:
	print(i)

# add new item in set A using add() method
A.add("orange")
print(A)

# add elements from another set using update() method
A = {"apple", "banana", "cherry"}
C = {"kiwi", "orange"}

A.update(C)
print(A)

# remove one item from any set using remove() method
A = {"apple", "banana", "cherry"}
A.remove("apple")
print(A)

# remove item using pop() method
A = {"apple", "banana", "cherry"}
A.pop()
print(A)

# use clear() method to delete all the items. Also use del() funtion and see the difference.
A = {"apple", "banana", "cherry"}
A.clear()
print(A)

# del() function
A = {"apple", "banana", "cherry"}
del A

# find the result after union(), intersection() and difference of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)


# ------------------------------------------------------
# create Disctionaries with proper data for ....
Employee = {
  "EmpId": "001",
  "Name": "Kishan",
  "Designation": "SDE",
  "JoiningDate": "15-12-2000",
  "Salary": "20000"
}
print(Employee)

Student = {
  "RollNo": "002",
  "Name": "Jaydip",
  "Branch": "Science",
  "City": "Gandhinagar",
  "Mobile": "+9123245567789"
}
print(Student)

Book = {
  "BookId": "003",
  "Title": "Psychology of Money",
  "Author": "unknown",
  "Publisher": "pub-kk",
  "Price": "150",
  "NoOfPages": "400"
}
print(Book)

# print all keys of dictionary using for loop and the keys() method
for x in Employee.keys():
  print(x)

for x in Student.keys():
  print(x)

for x in Book.keys():
  print(x)

# print all values of dictionary using for loop and the values() method
for x in Employee.values():
  print(x)

for x in Student.values():
  print(x)

for x in Book.values():
  print(x)

# add new item in the dictionary and remove one	item from it //direct method and update() method //pop() method & popitem() method
Employee = {
  "EmpId": "001",
  "Name": "Kishan",
  "Designation": "SDE",
  "JoiningDate": "15-12-2000",
  "Salary": "20000"
}
print(Employee)

Employee["DOB"] = "15-30-1975"
print(Employee)
Employee.pop("Salary")
print(Employee)

# print all the items in key=>value format
for x, y in Book.items():
  print(f"{x} : {y}")

# implement sallow copy and deep copy in the dictionary
# sallow copy
Student = {
  "RollNo": "002",
  "Name": "Jaydip",
  "Branch": "Science",
  "City": "Gandhinagar",
  "Mobile": "+9123245567789"
}
new_student = Student.copy()
new_student["Branch"] = "Arts"
print(new_student)

# deep copy
Book = {
  "BookId": "003",
  "Title": "Psycology of Money",
  "Author": "unknown",
  "Publisher": "pub-kk",
  "Price": "150",
  "NoOfPages": "400"
}

import copy
otherBook = copy.deepcopy(Book)
otherBook["NoOfPages"] = 100
print(otherBook)