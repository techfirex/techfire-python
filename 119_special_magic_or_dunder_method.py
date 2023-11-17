# special magic method or dunder method
# __init__, __repr___, __str__, __len__ etc

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def __str__(self): # used by normal use to see output or something else
        return f"{self.brand} {self.model}"
    
    def __repr__(self): # used by python developer to do something // return object which we defined
        return f"Phone(\'{self.brand}\', \'{self.model}\', {self._price})"
    
    def __len__(self):
        return len(self.full_name())

# l = [1,2,3] # l is object / instance
# print(l) # we can direct print object l

# list has len method to calculate length 
# print(len(l)) # lets define like in this in our class

my_phone = Phone("nokia", "1100", 1000) # my_phone is also object like l
# print(my_phone) # but cannot print my_phone like l

# to solve this use __str__ method
print(my_phone) # call like list object
# print(my_phone.__str__()) # same as above // we can call as function as we do
# print(my_phone.__repr__())

# also we can call like this
print(str(my_phone))
print(repr(my_phone))

print(len(my_phone))
print(my_phone.__len__()) # both are same

