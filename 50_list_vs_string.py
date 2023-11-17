# list is mutable
# string is immutable

s = "string"
print(s)
s.title()
print(s)
change = s.title()
print(change)

l = ["word1", "word2", "word3", "word4", "word5"]
print(l)
l.pop()
print(l)
l.append("word5")
print(l)