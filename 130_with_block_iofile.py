# normal method 
# f = open("file1.txt")
# print(f.read())
# f.close()


# with block
# context manager
# no need to close file

with open("file1.txt") as f:
    data = f.read()
    print(data)

print(f.closed)