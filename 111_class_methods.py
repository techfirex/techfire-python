class Person:
    count_instance = 0 # class variable or class attribute
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.count_instance += 1
        
    
    @classmethod # for class method create
    def count_instances(cls): # use cls keyword here
        return f"you have created {cls.count_instance} instances of {cls.__name__} class."

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above(self):
        return self.age > 18

p1 = Person("tushar", "makwana", 22)
p2 = Person("nupur", "vyas", 23)

print(Person.count_instances())