# how to create class
# what is init method / constructor
# what are attributes and instance variables
# how to create object of class

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print("every time init method called when object is created of this class")
        self.fname = first_name
        self.lname = last_name
        self.age = age

p1 = Person("tushar", "makwana", 22)
p2 = Person("nupur", "vyas", 22)

print(p1.fname)
print(p2.fname)
