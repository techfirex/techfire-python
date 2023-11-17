# class method related to class
# instance method related to instance / object
# static method releated to normal function in class with some logic'

class Person:
    count_instance = 0 # class variable or class attribute
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.count_instance += 1

    @staticmethod
    def hello():
        print("hello, static method is called")
    
    @classmethod # using this cls we input string which create object for us
    def is_string(cls,string):
        first, last, age = string.split(",")
        return cls(first,last,age)
        
    @classmethod # for class method create
    def count_instances(cls): # use cls keyword here
        return f"you have created {cls.count_instance} instances of {cls.__name__} class."

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above(self):
        return self.age > 18

p1 = Person("tushar", "makwana", 22)
p2 = Person("nupur", "vyas", 23)

# print(Person.count_instances())
# print(p1)
Person.is_string("tushar,makwana,23") # same as print(p1)
print(p2.full_name())

Person.hello()