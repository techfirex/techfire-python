# fromkeys
d = {"name":"unknown", "age":"unknown"}
print(d)

d = dict.fromkeys(["name", "age"],"unknown")
print(d)

d = dict.fromkeys(range(1,11),"unknown")
print(d)

d = dict.fromkeys(["name", "age"], ["unknown", "unknown"])
print(d)

d = dict.fromkeys("abc","unknown") # input string abc
print(d)

# get method ---> handles keyerror
d = dict.fromkeys(["name", "age", "height"],"unknown")
print(d)

print(d["name"]) # normally we do
# print(d["names"]) # names not present so gives error

print(d.get("name")) # normally works
print(d.get("names")) # names not present but give None values and not raise keyerror

if "name" in d:
    print("present")
else:
    print("not present")

if d.get("name"):
    print("present")
else:
    print("not present")
# if None ---> False, else ---> True

# copy method
d = dict.fromkeys(["name", "age", "height"],"unknown")

d1 = d
# this will make two dictionary but memory is same 
# so d1 change than d also change and vice versa same
print(d1 is d) # this check memory of object is same or not
print(d1 == d) # this check all key value pair is same
# if we popitem from d1 than it also removes from d

d1 = d.copy() # this create d1 separate copy in memory // Shallow copy & deep copy concept (d1.deepcopy())
print(d1 is d) 
print(d1 == d)
# if we popitem from d1 than it will not affect the d

# clear method --> make dictionary empty
d.clear()
print(d)





