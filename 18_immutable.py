# strings are immutable = which cannot change
# we can modify original string and store it in new_string but original string remain same

string = "string"
print(string)

print(string.replace("t", "T"))
new_string = string.replace("t", "T")

print(new_string)
print(string)