# read file
# open function - to open file and make object for that
# read method - read text file
# seek method - change cursor position
# tell method - check cursor position
# readline method - read line by line 
# readlines method - give variables having all lines in list so we can use it or iterate using loops
# close method - close the file after read / work done.


# by default it is read mode
# f = open("file1.txt", "r") # r is open file for read, w for write, rw is for read and write both etc

# ---------------------

f = open("file1.txt")
# f = open(r"C:\new\file1.txt") # use r string for raw path and neglect escape char

# print(f"cursor postion - {f.tell()}")
# print(f.read())
# print(f"cursor postion - {f.tell()}")
# # print(f.read()) # it will only read ones beacuse it work with cursor position
# f.seek(0) # change cursor position
# print(f.read())

# print(f.readline(), end="")
# print(f.readline())
# print(f.readline())

# lines = f.readlines()
# print(lines)

# for line in lines:
#     print(line, end="")

# for line in f: # also read lines diredctly using f object then what the use of readlines method next example
#     print(line, end="")

# for line in f.readlines()[:2]: # realines method helps here in f onject 
#     print(line)

# data descripters line name and closed
print(f.name) # to see file name
print(f.closed) # to check file is close or not here false 
f.close()
print(f.closed) # here True becasue file is closed now