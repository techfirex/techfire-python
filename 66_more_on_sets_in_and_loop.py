# in keyword in set and for loop

# in keyword to check if item is present or not
s = {"a", "b", "c"}

if "a" in s:
    print("present")
else:
    print("not present")


# for loop
for item in s:
    print(item)


s1 = {1,2,3,4}
s2 = {3,4,5,6}

# union {1,2,3,4} using pipe | sign
# intersection {3,4} using and & sign

union_set = s1 | s2
print(union_set)

print(s1 & s2)
