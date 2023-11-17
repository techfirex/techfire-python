# input ["abc", "tuv", "xyz"]
# output ["cba", "vut", "xyx"]

l = ["abc", "tuv", "xyz"]

def reverse(l):
    empty = []
    for i in l:
        empty.append(i[::-1])
    return empty

print(reverse(l))
    