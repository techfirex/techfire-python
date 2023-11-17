# we will discuss three existing problem in below example
# then we will solve using getter and setter decorator - this is also in other programming lang
# in python getter / property and setter is used

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        
        self._price = max(price, 0) # short way using max instead of below if else

        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0
    
        # self.full_specification = f"{self.brand} {self.model} and price is {self._price}"  
    
    @property # when we add this then we dont call as function like full_specification() direct use full_specification - it work like instance variable / attribute
    def full_specification(self):
        return f"{self.brand} {self.model} and price is {self._price}" 
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    def make_call(self, phone_number):
        print(f"calling .... {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1 = Phone("nokia", 1100, 1000)
print(p1.brand)
print(p1.model)
print(p1.price)
print(p1.full_specification)
# print(p1.full_specification())

p1.price = -50

print(p1.brand)
print(p1.model)
print(p1.price)
print(p1.full_specification)
# print(p1.full_specification())


# we cannot input negative price
# we cannot update price in negative manner
# updated price cannot show in full_specification after change
