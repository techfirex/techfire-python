name, char = input("Enter name and single character (comma separated): ").split(",")
print(len(name))
print(name.strip().lower().count(char.strip().lower()))

# name.strip().lower().count(char.strip().lower()) //this solve the problem of spaces here
