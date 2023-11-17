# encapsulation
# data and functionality with that data are in same places
# for example in class Phone / init method section is data and make_call & full_name is functions which perform functionality / are at togather

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = price # tell use about private name
    
    def make_call(self, phone_number):
        print(f"calling .... {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def send_msg(self):
        pass
        # complex function (adding twilio, api's etc) use easily send msg but dont know how it works - abstraction

# abstraction - hide complexity
l = [2,5,6,4,3,7,1]
l.sort() # tim sort algorithm - complexity is hidden - but we use easily
print(l) 


# special naming convention
# in python every variable is public
# but to tell developer anything is private / dont change
# _name - convention of private name / variable / instances
# __name__ - dunder / magic methods

phone1 = Phone("nokia", 1100, 1000)
print(phone1._price)
phone1._price = -1000
print(phone1._price)


# name mangling - __name (not a convention) - python will automatically change the name of instance var
class Phone2:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price # __name
    
p1 = Phone("nokia", 1100, 1000)
# print(p1.__price) # __price will not print - it give error
print(p1.__dict__) # {'brand': 'nokia', 'model': 1100, '_price': 1000} see it store as _price not as __price
print(p1._price) # it will print
