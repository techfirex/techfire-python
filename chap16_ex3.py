class Person:
    count_instance = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.count_instance += 1

p1 = Person("tushar","makwana")
p2 = Person("nupur","vyas")
p3 = Person("nupur","vyas")

print(Person.count_instance)