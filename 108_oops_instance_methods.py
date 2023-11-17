# function inside class - method // instance method

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above(self):
        return self.age > 18

p1 = Person("tushar", "makwana", 22)
p2 = Person("nupur", "vyas", 23)
print(p1)
print(p1.first_name)

print(p1.full_name())
print(p2.full_name())

print(Person.full_name(p1)) # same as print(p1.full_name())

print(p1.is_above())


# list case
l = [1,2,3,4]
# l.pop()
list.pop(l) # same as l.pop() // class.method(object)
print(l)

list.append(l, 10) # class.method(object, parameter) // same as l.append(10)
print(l)
