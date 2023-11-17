class Laptop:
    discount = 10
    def __init__(self, brand_name, model_name, price):
        # instance_variables - unique for every class object
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + " " + model_name

    def apply_discount(self):
        return (self.price - (self.price*Laptop.discount)/100) 
        # return (self.price - (self.price*self.discount)/100) # if we want to change discount for object letter then we use self.discount instead of Laptop.discount 


# Laptop.discount = 20 # change discount for all from 10 to 20%
lap1 = Laptop("Dell", "Inspiron 3558", 40000)
lap2 = Laptop("Lenovo", "Ideapad Slim 3i", 95000)

# if we to add special offer to special laptop object
lap2.discount = 50 # but did not work it use class variable 


# if we want to see which instance varibles object has
print(lap1.__dict__)
print(lap2.__dict__)

print(lap1.apply_discount())
print(lap2.apply_discount())